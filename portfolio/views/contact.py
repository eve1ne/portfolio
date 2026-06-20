"""
portfolio Contact view.

URLs include:
/
"""
from urllib import request

import flask
import portfolio


@portfolio.app.route('/contact/')
def show_contact():
    """Display the contact page."""
    # Connect to database
    connection = portfolio.model.get_db()

    # Build context for template
    context = {}

    return flask.render_template("contact.html", **context)

@portfolio.app.route('/contact/', methods=['POST'])
def submit_contact_form():
    """Handle contact form submission."""
    # Process form data
    name = flask.request.form.get('name')
    email = flask.request.form.get('email')
    message = flask.request.form.get('message')

    portfolio.app.logger.info(f"Received contact form submission: Name={name}, Email={email}, Message={message}")

    # Redirect or render success page
    return flask.redirect(flask.url_for('show_contact'))
