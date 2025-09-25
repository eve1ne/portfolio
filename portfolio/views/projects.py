"""
portfolio projects view.

URLs include:
/
"""
import flask
import portfolio

from functools import wraps
from flask import session, redirect, url_for, request, render_template, flash

from portfolio.config import INTERNSHIP_PASSWORD

@portfolio.app.route("/login", methods=["GET","POST"])
def login():
    """Password login."""
    if request.method == "POST":
        if request.form.get("password") == INTERNSHIP_PASSWORD:  # secure password
            session["authorized"] = True
            # Redirect back to the internship project if desired
            return redirect(url_for("show_project_detail", projectid=1))
        flash("Wrong password")
    return render_template("login.html")


@portfolio.app.route("/logout")
def logout():
    session.pop("authorized", None)
    return redirect(url_for("login"))


# Decorator to protect specific project(s)
def password_protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if the project is the internship project
        projectid = kwargs.get("projectid")
        if projectid == 1:
            if not session.get("authorized"):
                return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


@portfolio.app.route('/projects/')
def show_projects():
    """Display all projects."""
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

    return flask.render_template("projects.html", **context)


@portfolio.app.route("/projects/<int:projectid>/")
@password_protected
def show_project_detail(projectid):
    """Display contents of specific project."""
    connection = portfolio.model.get_db()

    cur = connection.execute(
        """
        SELECT projectid, title, description, image_url, repo_url, doc_url, demo_url, created_at
        FROM projects
        WHERE projectid = ?
        """, 
        (projectid,)
    )

    project = cur.fetchone()
    if project is None:
        flask.abort(404)

    return flask.render_template("project_detail.html", project=project)



@portfolio.app.route('/artworks/<int:artid>/')
def show_artwork_detail(artid):
    """Display contents of specific art project."""

    connection = portfolio.model.get_db()

    cur = connection.execute(
        """
        SELECT artid, title, description, image_url, video_url, medium, created_at
        FROM artworks
        WHERE artid = ?
        """, 
        (artid,))

    artwork = cur.fetchone()

    if artwork is None:
        flask.abort(404)

    return flask.render_template("artwork_detail.html", artwork=artwork)
