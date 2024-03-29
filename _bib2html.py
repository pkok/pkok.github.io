#!/usr/bin/env python
import argparse
import re
import subprocess
import sys

def parse_args():
    parser = argparse.ArgumentParser(
            description="I use this program to generate a bibtex overview for my blog.")
    parser.add_argument('--input', default="_bibliography.bib")
    parser.add_argument('--output', default="./_includes/bibliography.html")
    return parser.parse_args()

def bib2html(bibliography, html_filename):
    command = "bibtex2html"
    options = [
        "-html-entities",
        #"-nobibsource",
        "-single",
        "-nodoc",
        "-nokeys",
        "-o %s" % ".".join(html_filename.split(".")[:-1]),
        bibliography,
    ]
    subprocess.call(command + " " + " ".join(options), shell=True)


def html2jekyll(html_str):
    html_str = html_str.split('<hr>')[0]
    html_str = re.sub(r'<!--[\S\s]*-->', r'', html_str)
    html_str = re.sub(r'\n\n+', r'\n', html_str)
    html_str = re.sub(r'<p><a name="(?P<key>[^"]+)"></a>',
                  r'{% if keys contains "\g<key>" or keys.size == 0 %}\n<li id="\g<key>">',
                  html_str)
    html_str = re.sub(r'<a name="(?P<key>[^"]+)"></a><pre>',
                  r'[&nbsp;<a href="#\g<key>_bib">bib</a>&nbsp;]<pre id="\g<key>_bib"><code>',
                  html_str)
    matchstr = r'(?P<bib>]<pre id="[^"]*">([\s\S](?!</pre>))*url\s*=\s*{<a href="(?P<url>[^"]*(?P<filetype>.[A-z0-9]{3,5}))")'
    html_str = re.sub(matchstr,
                  r'|&nbsp;<a href="\g<url>">\g<filetype></a>&nbsp;\g<bib>',
                  html_str)
    matchstr = r'(?P<bib>]<pre id="[^"]*">([\s\S](?!</pre>))*doi\s*=\s*{(?P<doi>[^}]*)})'
    html_str = re.sub(matchstr,
                  r'|&nbsp;<a href="http://dx.doi.org/\g<doi>">DOI</a>&nbsp;\g<bib>',
                  html_str)
    html_str = re.sub(r'</pre>',
                  r'</code>\n</pre>',
                  html_str)

    html_str = re.sub(r'</p>\s*', r'</li>\n{% endif %}', html_str)
    html_str = re.sub(r'{{', r'{ {', html_str)

    jekyll_str = """
{% assign keys = include.keys | split: "," %}

<section>
<h3 class="no_toc">References</h3>
<ul class="bibliography">
"""
    jekyll_str += html_str
    jekyll_str += """
</ul>
</section>
"""
    return jekyll_str

if __name__ == "__main__":
    args = parse_args()
    bib2html(args.input, args.output)

    with open(args.output, 'r') as file_:
        html = file_.read()

    jekyll = html2jekyll(html)

    with open(args.output, 'w') as file_:
        file_.write(jekyll)
