#!/usr/bin/env python3

from bottle import SimpleTemplate


tpl = SimpleTemplate('hello {{name}}')

print(tpl.render(name='world'))
