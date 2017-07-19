#!/usr/bin/env python

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(
    sys.modules['__main__'].__file__)))

sys.path.insert(0, os.path.join(ROOT, 'src'))

VERSION = '1.0.0'

for m in ('multiprocessing', 'billiard'):
    try:
        __import__(m)
    except ImportError:
        pass

IS_LIGHT_BUILD = os.environ.get('IS_LIGHT_BUILD') == '1'
