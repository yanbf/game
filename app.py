from flask import Flask
app = Flask(__name__)

@app.route('/hello_word')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return 'Hello, World!'
