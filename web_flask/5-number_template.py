#!/usr/bin/python3
""" Starts a Flash Web Application Python is Cool"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_nbnb():
    """ Prints a Message when / is called """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Prints a Message when /hbnb is called """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Prints a Message when /c is called """
    return "C " + text.replace('_', '')

@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Prints a Message when /python is called """
    return "Python " + text.replace('_', '')

@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    """ Prints a Message when /number is called only if n is an int"""
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temblate(n):
    """ Prints a Message when /number is called only if n is an int"""
    return render_template('5-number.html', Number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)