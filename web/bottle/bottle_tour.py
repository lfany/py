#!/usr/bin/env python3

from bottle import Bottle, run, static_file, request

app = Bottle()


@app.route('/hello/<name>')
def index(name='Stranger'):
    return 'hello world! {xx} '.format(xx=name)


@app.error(code=404)
def file_not_found(error):
    return 'file not found'


@app.route('/test/<param>')
def test(param):
    return 'test %s' % param


@app.route('/code')
@app.route('/code/')
def code():
    return static_file(root='./', filename='myspider.py')


@app.get('/login')  # 或 @route('/login')
def login_form():
    return '''<form method="POST" action="/login">
<input name="name" type="text" />
<input name="password" type="password" />
<input type="submit" />
</form>'''


def check_login(name, password):
    pass
    return True


@app.post('/login')  # 或 @route('/login', method='POST')
def login_submit():
    name = request.forms.get('name')
    password = request.forms.get('password')
    if check_login(name, password):
        return "<p> 登录成功 </p>"
    else:
        return "<p> 登录失败 </p>"


run(app=app, host='localhost', port=44, debug=True, reloader=True)
