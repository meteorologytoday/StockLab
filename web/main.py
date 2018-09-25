from bottle import route, run, template, static_file
import os.path

root = os.path.dirname(os.path.realpath(__file__))
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=os.path.join(root, "static"))

@route('/')
def root():
    return template("index")


@route('/hello')
def hello():
    return "Hello World!"

run(host='0.0.0.0', port=8080, debug=True)
