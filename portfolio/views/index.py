"""
portfolio index (main) view.

URLs include:
/
"""
import flask
import portfolio
import os
from flask import send_from_directory


@portfolio.app.route('/')
def show_index():
    """Display the Homepage."""
    # Connect to database
    connection = portfolio.model.get_db()

    # Build context for template
    context = {}
    return flask.render_template("index.html", **context)

