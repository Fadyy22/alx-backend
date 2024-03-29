#!/usr/bin/env python3
"""basic Flask app with single route"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from pytz import timezone, UnknownTimeZoneError
from typing import Dict, Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """flask babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """returns user data by id passed in login_as query string"""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """functions the executes before every request
    and puts the user data in global var g"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """returns the locale of a web page"""
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    elif g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """returns the timezone of a web page"""
    req_timezone = request.args.get('timezone', '')
    if not req_timezone and g.user:
        req_timezone = g.user.get('timezone')
    try:
        return timezone(req_timezone).zone
    except UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/")
def home() -> str:
    """render index.html page"""
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
