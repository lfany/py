#!/usr/bin/env python

import argparse
import optparse
import getopt

from optparse import OptionParser

import sys

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
parser.add_option("-x", "--x")

(options, args) = parser.parse_args()

if not len(args):
    parser.print_help()
    print(sys.argv)
    print(options)
    print(args)
