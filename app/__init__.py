#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""Sample helo woekd Flask App"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloi():
    return "<h1>Hello, world!<h1>"