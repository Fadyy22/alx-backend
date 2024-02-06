#!/usr/bin/env python3
"""basic Flask app with single route"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """render 0-index.html page"""
    return render_template('0-index.html')


app.run()
