#!/usr/bin/python3
# the second file 
""" module doc """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """the root page"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """the hbnb page"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)