#!/usr/bin/env python3

import pip
import sys

list = pip.get_installed_distributions()
list.reverse()

for i in list:
    print(i)
