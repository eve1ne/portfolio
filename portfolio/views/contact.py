"""
portfolio Contact view.

URLs include:
/
"""
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
