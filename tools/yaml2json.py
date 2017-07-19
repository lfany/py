#!/usr/bin/env python

import os
import sys

import json
import yaml

__VERSION__ = 'v 0.1'
__AUTHOR__ = 'by huaixiaoz<hello@ifnot.cc>'


def version():
    return os.path.basename(sys.argv[0]) + os.altsep + __VERSION__ + os.altsep + __AUTHOR__


def usage():
    print(f"Usage: {sys.argv[0]} <yaml filename>")
    print(version())


def parse_yaml(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            load = yaml.load(f)
            return json.dumps(load)
    except Exception as e:
        print(e)
        exit(-1)


def __main__():
    if len(sys.argv) != 2:
        usage()
    else:
        print(parse_yaml(sys.argv[1]))


if __name__ == '__main__':
    __main__()
