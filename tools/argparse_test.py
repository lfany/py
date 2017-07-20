#!/usr/bin/env python

import argparse
import optparse
import getopt

# from optparse import OptionParser
#
# import sys
#
# parser = OptionParser()
# parser.add_option("-f", "--file", dest="filename",
#                   help="write report to FILE", metavar="FILE")
# parser.add_option("-q", "--quiet",
#                   action="store_false", dest="verbose", default=True,
#                   help="don't print status messages to stdout")
# parser.add_option("-x", "--x")
#
# (options, args) = parser.parse_args()
#
# if not len(args):
#     parser.print_help()
#     print(sys.argv)
#     print(options)
#     print(args)


import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# args = parser.parse_args()

args = parser.parse_args()
print(args.accumulate(args.integers))
parser.print_help()

