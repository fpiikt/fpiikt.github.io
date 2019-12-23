from flask import Flask, escape, request, redirect, url_for
from flask import abort

from flask import Response

from werkzeug.exceptions import InternalServerError

from middleware import login_required

app = Flask(__name__)

@app.route('/')
def index():
	return "Привет мир!"


@app.route('/response')
def index2():
    resp = Response("Привет мир!")
    resp.headers['Content-Type'] = 'text/html; charset=utf-8'
    resp.headers['Server'] = 'myserver'
    resp.headers['x-powered-by'] = ''

    return resp
# curl -iX GET http://localhost:4321/response
# ...
# Content-Type: text/html; charset=utf-8
# ...
# Server: myserver
# x-powered-by:

@app.errorhandler(404)
def page_not_found(error):
	return 'Пока нет!', 404


@app.route('/e')
def server_error_demo1():
	abort(500) # or return (1, ) + 1


@app.errorhandler(InternalServerError)
def handle_500(e):
    return f"Ошибка {e}", 500


@app.route('/login', methods=['GET', 'POST'])
def login():
    from flask import g

    if request.method == 'POST':
        g.username = request.form['username']
        return redirect(url_for('secret'))
    return '''
        <form method="post">
            <p><input type=text name=username></p>
            <p><input type=submit value=Login></p>
        </form>
    '''

@app.route('/secret')
@login_required
def secret():
    from flask import g
    username = ''
    if 'username' in g:
        username = g.username

    resp = Response(f"Секрет, {username} ")
    return resp


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='4321')
