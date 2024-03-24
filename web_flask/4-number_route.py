#!/usr/bin/python3
"""flask projects"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def greet():
    """ Returns Hello HBNB! """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def _text(text):
    """ Returns C """
    return 'C ' + {text.replace("_", " ")}


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """This function handles the '/python'
    route and the '/python/<text>' route."""
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Function returns n, if n is an integer"""
    return f"{n} is a number"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
