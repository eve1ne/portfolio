"""
portfolio index (main) view.

URLs include:
/
"""
import flask
import portfolio



@portfolio.app.route('/')
def show_index():
    """Display the Homepage."""
    # Connect to database
    connection = portfolio.model.get_db()

    currProjects = connection.execute(
        "SELECT * FROM cs_projects WHERE end_date = ? ORDER BY display_order",
        ("Present",)
    ).fetchall()

    artCurrProjects = connection.execute(
        "SELECT * FROM art_projects WHERE end_date = ? ORDER BY display_order",
        ("Present",)
    ).fetchall()

    # Build context for template
    return flask.render_template("index.html", currProjects=currProjects, artCurrProjects=artCurrProjects)

