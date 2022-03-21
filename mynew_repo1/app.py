from flask import flask

app = Flask(_name_)

@app.route("/hello")
def hello_world():
    return "Hello world!"

