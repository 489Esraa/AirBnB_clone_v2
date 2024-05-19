#!/usr/bin/python3
""" module doc """
#  script that starts a Flask web application:
#Your web application must be listening on 0.0.0.0, port 5000
#Routes:
#/: display “Hello HBNB!”
#You must use the option strict_slashes=False in your route definition
#strict_slashes=False parameter allows the route to be accessed with or without a trailing slash.
#function Flask_web_app ():Define the Route Handler is defined to handle requests to the /
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def doc """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)