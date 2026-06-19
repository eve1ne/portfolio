"""
portfolio index (work) view.

URLs include:
/
"""
import flask
import portfolio
import os
from flask import send_from_directory


@portfolio.app.route('/work/cs')
def show_cs():
    return flask.render_template("work-fields/cs.html")

@portfolio.app.route('/work/design')
def show_design():
    return flask.render_template("work-fields/design.html")

@portfolio.app.route('/work/animation')
def show_animation():
    return flask.render_template("work-fields/animation.html")

@portfolio.app.route('/work/media')
def show_media():
    return flask.render_template("work-fields/media.html")

