"""
portfolio art projects view.

!!!!For now since I don't have a lot of projects we can combine them on one projects page!!!!!

URLs include:
/
"""
import flask
import portfolio


@portfolio.app.route('/artworks/')
def show_artworks():
    """Display the homepage with all projects."""
    # Connect to database
    connection = portfolio.model.get_db()

    # Query all projects
    cur = connection.execute(
    """
    SELECT artid, title, description, image_url
    FROM artworks
    ORDER BY artid DESC
    """
    )
    artworks = cur.fetchall()


    # Build context for template
    context = {
        "artworks": artworks
    }

    return flask.render_template("artworks.html", **context)
