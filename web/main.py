from bottle import route, run, template


@route('/')
def root():
    return template("index")


@route('/hello')
def hello():
    return "Hello World!"

run(host='0.0.0.0', port=8080, debug=True)
