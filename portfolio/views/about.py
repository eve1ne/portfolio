"""
portfolio index (main) view.

URLs include:
/
"""
import flask
import portfolio


@portfolio.app.route('/about/')
def show_about():
    """Display the homepage with all projects."""
    # Connect to database
    connection = portfolio.model.get_db()

    # Build context for template
    context = {}

    return flask.render_template("about.html", **context)
