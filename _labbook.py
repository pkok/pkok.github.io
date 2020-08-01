#!/usr/bin/env python3
"""
A tool to help you manage a labbook in Jekyll.

Author: Patrick de Kok
License: BSD 3-clause
"""

LABBOOK_VERSION = "0.1.0"

import argparse
import configparser
import datetime
import os
import re
import subprocess

HOME = os.getenv("HOME")
CONFIG_FILE = os.path.abspath(
        os.path.join(HOME, ".config", "labbook", "config"))

IS_INTERACTIVE = False

POST_TEMPLATE = """---
title: {title}
layout: post
categories:
  - thesis
---

"""

def __parse_arguments():
    """
    """
    parser = argparse.ArgumentParser(
            description=__doc__,
            epilog="If no option is provided, '--open 0' is assumed.")
    group = parser.add_mutually_exclusive_group(required=False)
    parser.add_argument("-v", "--version", action="store_true",
            help="Print version and exit")
    parser.add_argument("-n", "--name", metavar="NAME",
            default=configparser.DEFAULTSECT,
            help="Name of the labbook to work on")
    parser.add_argument("title", metavar="TITLE", type=str,
            nargs=argparse.REMAINDER,
            help="Optional title of the labbook entry.")
    group.add_argument("-o", "--open", metavar="DAYS_AGO",
            nargs="?", const=0,
            help="Open the labbook entry of DAYS_AGO")
    group.add_argument("-O", "--open-new", action="store_true",
            help="Open a new post")
    group.add_argument("-g", "--git-commit", metavar="COMMIT_MSG",
            help="Commit the changed labbook entries to its git repository")
    group.add_argument("-l", "--list-entries", action="store_true",
            help="List all labbook entries")
    group.add_argument("-ln", "--list-names", action="store_true",
            help="List all labbook names")
    group.add_argument("-s", "--search", action="store_true",
            help="Search and open lab book entry")
    group.add_argument("-j", "--jekyll", action="store_true",
            help="Start the local Jekyll server")
    group.add_argument("-c", "--config", action="store_true",
            help="Enter configuration mode")

    return parser.parse_args()

def print_info(msg):
    global IS_INTERACTIVE
    if IS_INTERACTIVE:
        print(msg)

def print_warning(msg):
    global IS_INTERACTIVE
    if IS_INTERACTIVE:
        yellow = "\033[0;33m"
        regular = "\033[0m"
        print("{}{}{}".format(yellow, msg, regular))

def print_error(msg):
    global IS_INTERACTIVE
    if IS_INTERACTIVE:
        red = "\033[0;31m"
        regular = "\033[0m"
        print("{}{}{}".format(red, msg, regular))

def pager(msg):
    if IS_INTERACTIVE:
        import pydoc
        pydoc.pager(msg)


class Labbook:
    RequiredConfiguration = {
        "dir": "The project's home directory"
    }

    OptionalConfiguration = {
        "editor": "The text editor",
        "posts_dir": "The directory containing labbook entries (default: ./_posts)"
    }

    def __init__(self, labbook_name):
        self._labbook_name = labbook_name
        self._global_config = self._load_config()


    def _load_config(self):
        """
        Load the configuration file.
        """
        if not os.path.isfile(CONFIG_FILE):
            CONFIG_DIR, _ = os.path.split(CONFIG_FILE)
            os.makedirs(CONFIG_DIR, exist_ok=True)
        
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        return config


    def check_minimal_config(self):
        """
        Check if the configuration file is setup for the current labbook.
        """
        known_name = self._labbook_name in self._global_config
        global_config = bool(len(self._global_config))
        default_config = bool(len(self._global_config[configparser.DEFAULTSECT]))

        if not (known_name and global_config and default_config):
            raise RuntimeError("No labbook configuration found. "
                    + "You can add this with the --config option.")
        self._config = self._global_config[self._labbook_name]
        return True


    def setup_configuration(self):
        """
        Go into an IS_INTERACTIVE mode to initialize configuration.
        """
        global IS_INTERACTIVE
        if not IS_INTERACTIVE:
            raise RuntimeError("Must run in interactive mode to "
                    + "call Labbook.setup_configuration")
        if self._labbook_name not in self._global_config:
            self._global_config.add_section(
                    self._labbook_name)
        config = self._global_config[self._labbook_name]
        print("Starting IS_INTERACTIVE configuration for labbook '{}'."
                .format(self._labbook_name))
        print("")
        print("Required parameters")
        print("-----")
        print("Whenever you want to keep an old value, just press enter.")
        for k, v in self.RequiredConfiguration.items():
            old = config.get(k)
            answer = ''

            if old is not None:
                msg = "{} (now: '{}'): ".format(v or k, old)
            else:
                msg = "{}: ".format(v or k)

            while True:
                answer = input(msg).strip()
                if len(answer) != 0 or old is not None:
                    if len(answer) == 0:
                        answer = old
                    break
            config[k] = answer
        print("")
        print("Optional parameters")
        print("-----")
        for k, v in self.OptionalConfiguration.items():
            old = config.get(k)
            answer = ''

            if old is not None:
                msg = "{} (now: '{}'): ".format(v or k, old)
            else:
                msg = "{}: ".format(v or k)

            while True:
                answer = input(msg).strip()
                if old is not None:
                    answer = old
                break
            if len(answer) != 0:
                config[k] = answer
        with open(CONFIG_FILE, 'w') as f:
            self._global_config.write(f)


    def _get_posts_dir(self):
        """
        Find the directory that contains the labbook posts.

        Search order:
          - config['posts_dir']
          - abspath(config['posts_dir'])
          - config['dir']/config['posts_dir]
          - config['dir']/_posts

        If none of these is a directory, raise a RuntimeError.
        """
        candidates = []
        if 'posts_dir' in self._config:
            posts_dir = self._config['posts_dir']
            candidates.append(posts_dir)
            candidates.append(os.path.abspath(posts_dir))
            candidates.append(os.path.join(
                self._config['dir'],
                self._config['posts_dir']))
        candidates.append(os.path.join(
            self._config['dir'],
            '_posts'))
        for candidate in candidates:
            if os.path.isdir(candidate):
                return candidate
        raise RuntimeError("""posts_dir not found.  Candidates did not point to
                a directory: {}""".format(candidates))


    def _get_entry_title(self, post_path):
        """
        Get the title of a labbook entry by parsing the file.
        """
        YAML_SEPARATOR = '---+\s*'
        entry_title = ''
        with open(post_path, 'r') as f:
            line = f.readline()
            if re.match(YAML_SEPARATOR, line):
                for line in f:
                    if re.match(YAML_SEPARATOR, line):
                        break
                    m = re.match('\s*title\s*:\s*', line, re.I)
                    if m is not None:
                        entry_title = line[m.end():].strip()
                        break
        return entry_title


    def _get_entry_filename(self, date, title):
        """
        Return the filename matching date and title.
        """
        BASE_ENTRY_FILENAME = "{date:%Y-%m-%d}-{title}.md"
        posts_dir = self._get_posts_dir()
        title = re.sub("\s+", "-", title)

        filename_with_title = os.path.join(
                posts_dir,
                BASE_ENTRY_FILENAME.format(date=date, title=title))
        filename_no_title = os.path.join(
                posts_dir,
                BASE_ENTRY_FILENAME.format(date=date, title=''))

        if os.path.isfile(filename_with_title):
            return filename_with_title

        if os.path.isfile(filename_no_title):
            file_title = self._get_entry_title(filename_no_title)
            if title != file_title:
                return filename_with_title
        return filename_no_title


    def _get_editor(self):
        """
        Return the command for the text editor.
        """
        root_fs = os.path.abspath(os.sep)
        default_editor = os.path.join(root_fs, 'usr', 'bin', 'vi')
        external_editor = os.getenv('VISUAL') or os.getenv('EDITOR')
        config_editor = self._config.get('editor')

        return config_editor or external_editor or default_editor


    def list_entries(self):
        """
        Print & return a list of entries in the labbook.
        """
        posts_dir = self._get_posts_dir()
        entries = []
        msg = "Entries:\n"
        for post in os.listdir(posts_dir):
            if not post.endswith('.md'):
                continue
            entry_title = self._get_entry_title(os.path.join(posts_dir, post))
            if entry_title:
                msg += "  - {}: {}\n".format(post, title)
            else:
                msg += "  - {}\n".format(post)
            entries.append((post, entry_title))
        entries.sort()
        pager(msg)
        return entries


    def list_names(self):
        """
        Print & return a list of known labbooks.
        """
        names = []
        all_sections = [configparser.DEFAULTSECT] + \
                self._global_config.sections()
        for name in all_sections:
            if len(self._global_config[name]) > 0:
                names.append(name)
        if names:
            msg = "Known labbooks:\n"
            for name in names:
                msg += "  - {}\n".format(name)
            pager(msg)
        else:
            print_error("No labbooks known.")
        return names


    def open_entry(self, days_ago, title):
        """
        Open a labbook entry of days_ago by a title with the text editor.
        """
        days_ago = datetime.timedelta(days=days_ago)
        date = datetime.date.today() - days_ago
        entry_file = self._get_entry_filename(date, title)

        editor = self._get_editor()
        # If we open a new file, first fill it with some info
        is_new = False
        if not os.path.isfile(entry_file):
            with open(entry_file, 'w') as f:
                f.write(POST_TEMPLATE.format(title=title))
            is_new = True
        if is_new:
            created_time = os.stat(entry_file).st_mtime
            subprocess.run(args=[editor, '+', entry_file])
            updated_time = os.stat(entry_file).st_mtime
            if created_time == updated_time:
                os.remove(entry_file)
        else:
            subprocess.run(args=[editor, entry_file])

        return entry_file


    def run_jekyll(self):
        """
        Start the local Jekyll server.
        """
        source_dir = self._config['dir']
        destination_dir = os.path.join(source_dir, "_site")
        subprocess.run(args=["jekyll", "s",
            "--source", source_dir,
            "--destination", destination_dir])


def __cli():
    """
    The command line interface for the labbook tool.
    """
    # Turn paging for long output on for IS_INTERACTIVE mode.
    global IS_INTERACTIVE
    INTERACTIVE_OLD = IS_INTERACTIVE
    IS_INTERACTIVE = True

    args = __parse_arguments()
    if args.version:
        return print_info("labbook version {}".format(LABBOOK_VERSION))

    labbook = Labbook(args.name)
    try:
        if args.config:
            return labbook.setup_configuration()
        if args.list_names:
            return labbook.list_names()

        labbook.check_minimal_config()
        if args.jekyll:
            return labbook.run_jekyll()
        if args.list_entries:
            return labbook.list_entries()
        if args.git_commit or args.search:
            return print_warning("This feature is not yet implemented.")

        # If no other flags are provided, we assume opening the latest post.
        title = " ".join(args.title)
        days_ago = 0
        if args.open is None:
            if args.title and args.title[0].isdigit():
                days_ago = int(args.title[0])
                title = " ".join(args.title[1:])
        else:
            if args.open.isdigit():
                days_ago = int(args.open)
            else:
                title = " ".join([args.open, title])
        return labbook.open_entry(days_ago, title)

    except RuntimeError as e:
        print_error("Error: {}".format(e))

    IS_INTERACTIVE = INTERACTIVE_OLD


if __name__ == "__main__":
    __cli()
