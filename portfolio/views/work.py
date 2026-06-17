"""
portfolio index (work) view.

URLs include:
/
"""
import flask
import portfolio
import os
from flask import send_from_directory


@portfolio.app.route('/work/frontend')
def show_frontend():
    return flask.render_template("work-fields/frontend.html")

@portfolio.app.route('/work/ux')
def show_ux():
    return flask.render_template("work-fields/ux.html")

@portfolio.app.route('/work/design')
def show_design():
    return flask.render_template("work-fields/design.html")

@portfolio.app.route('/work/animation')
def show_animation():
    return flask.render_template("work-fields/animation.html")

@portfolio.app.route('/work/photo-video')
def show_photo_video():
    return flask.render_template("work-fields/photo_video.html")

