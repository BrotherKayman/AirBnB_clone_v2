#!/usr/bin/python3

"""
This script defines a simple Flask web application.

The application listens on 0.0.0.0, port 5000, and includes two routes:
- '/' : This route displays "Hello HBNB!" when accessed.
- '/hbnb' : This route displays "HBNB" when accessed.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Display "Hello HBNB!" when accessing the root URL.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" when accessing the '/hbnb' route.

    Returns:
        str: A message indicating the route.
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
