#!/usr/bin/python3
""" Starts a Flash Web Application Python is Cool"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_nbnb():
    """ Prints a Message when / is called """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Prints a Message when /hbnb is called """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)