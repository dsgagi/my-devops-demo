from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Devtech from dsgagi! v2'
