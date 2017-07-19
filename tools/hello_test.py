#!/usr/bin/env python

"""
D:\py36\python.exe E:/py/tools/hello_test.py
argv: ['E:/py/tools/hello_test.py']
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.getcwd()))

from package_hello import main

if __name__ == '__main__':
    main()
