#!/usr/bin/env python3

RUN = "Run"
RMS_ATE = r"RMS\_ATE"
MEAN = "Mean"
MEDIAN = "Median"
STD = "Std"
MIN = "Min"
MAX = "Max"
LEFT_ALIGN = "---------:"
RIGHT_ALIGN = ":---------"

DIVIDE_BY = MEAN
SORT_BY = MEAN
LABELS = [RUN, MEAN, RMS_ATE, MEDIAN, STD, MIN, MAX]

FORMAT = {"number": "{:>9.6f} ",
          "label": " {:8s} ",
          "dash": " {:>8s} ",
          "percentage": "  {:>6.2f}% "}
DASH = FORMAT["dash"].format("-")


def str2lists(table):
    t = []
    for row in table:
        row = row.split("|")[1:-1]
        r = []
        for cell in row:
            c = cell.strip()
            r.append(cell.strip())
        t.append(r)
    return t


def strs2floats(table):
    t = []
    for row in table:
        r = []
        for cell in row:
            try:
                r.append(float(cell))
            except:
                r.append(cell)
        t.append(r)
    return t


def process_buffer(table, outfile):
    table = str2lists(table)
    header = table[0]
    data = strs2floats(table[2:])

    column = {}
    for label in LABELS:
        column[label] = header.index(label)

    data[1:] = sorted(data[1:],
                      key=lambda k: k[column[SORT_BY]])

    new_header = []
    align_line = []
    for label in LABELS:
        fmt = "label"
        new_header.append(FORMAT[fmt].format(label))
        if label == RUN:
            align_line.append(LEFT_ALIGN)
        else:
            align_line.append(RIGHT_ALIGN)

        if label not in [RUN, DIVIDE_BY]:
            new_header.append(FORMAT[fmt].format(""))
            align_line.append(RIGHT_ALIGN)
    new_header = "|" + "|".join(new_header) + "|"
    align_line = "|" + "+".join(align_line) + "|"

    new_data = []
    for d in data:
        row = []
        for label in LABELS:
            format_ = "number"
            if label == RUN:
                format_ = "label"
            try:
                row.append(FORMAT[format_].format(d[column[label]]))
            except:
                row.append(DASH)
            if label not in [RUN, DIVIDE_BY]:
                try:
                    percentage = 100. * d[column[label]] / d[column[DIVIDE_BY]]
                    row.append(FORMAT["percentage"].format(percentage))
                except:
                    row.append(DASH)
        new_data.append("|" + "|".join(row) + "|")
    table = [new_header, align_line]
    table.extend(new_data)
    table_str = "\n".join(table)
    output.write(table_str + "\n\n")


if __name__ == "__main__":
    table_buffer = []
    buffering = False
    with open("2021-05-12-.md", mode="r") as input_:
        with open("2021-05-17-.md", mode="w") as output:
            for line in input_:
                if line.startswith("|"):
                    buffering = True
                    table_buffer.append(line)
                elif buffering:
                    process_buffer(table_buffer, output)
                    buffering = False
                    table_buffer = []
                else:
                    output.write(line)
