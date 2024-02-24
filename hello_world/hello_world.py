from flask import Blueprint, redirect, render_template

helloword_bp = Blueprint('hellowworld', __name__, template_folder='templates')

@helloword_bp.route('/')
def index():
    return "Hello World"

@helloword_bp.route('/hello')
def hello():
    return "Hello World Again"

@helloword_bp.route('/hello1')
def hello_name():
    return render_template('hello.html')