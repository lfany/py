#!/usr/bin/env python3

from bottle import Bottle, run

app = Bottle()


@app.route('/hello/<name>')
def index(name):
    return 'hello world! {xx} '.format(xx=name)


@app.error(code=404)
def file_not_found(error):
    return 'file not found'


@app.route('/test/<param>')
def test(param):
    return 'test %s' % param


run(app=app, host='localhost', port=44, debug=True, reloader=True)
