#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description='Pipe to a python one-liner')
parser.add_argument('--before', default="",
                    help='code to run before the loop. in "python -c" format.')

parser.add_argument('--per-line', required=True,
                    help='the code to run on each line. in "python -c" format. "_line" is the line of data and the index of the line is "_i"')

parser.add_argument('--after', default="",
                    help='the code to run after the loop. in "python -c" format')

args = parser.parse_args()

_veryunlikelyvarname = sys.stdin.readlines()

exec(args.before)

for _i, _line in enumerate(_veryunlikelyvarname):
    _line = _line[:-1] # remove newline at the end
    exec(args.per_line)

exec(args.after)
