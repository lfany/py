#!/usr/bin/env python3

from bottle import route, run

@route('/')
def index():
    return "hello world!"
run(host='localhost', port=44)