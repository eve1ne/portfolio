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
    """Display the homepage with featured/current projects."""
    # Connect to database
    connection = portfolio.model.get_db()

    # Query all projects
    cur = connection.execute(
    """
    SELECT projectid, title, description, image_url
    FROM projects
    ORDER BY projectid DESC
    """
    )
    projects = cur.fetchall()

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
        "projects": projects,
        "artworks": artworks
    }

    return flask.render_template("index.html", **context)

