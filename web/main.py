from bottle import route, run, template, static_file
import os.path
import pandas as pd

root_dir = os.path.dirname(os.path.realpath(__file__))

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=os.path.join(root_dir, "static"))

@route('/')
def root():
    print("ROOT")
    return template("index")


@route('/hello')
def hello():
    return "Hello World!"

@route('/analysis/<filename>')
def analysis(filename):
    df = pd.read_csv(os.path.join(root_dir, "static", filename))
    return template("analysis", data=df)

run(host='0.0.0.0', port=8080, debug=True)
