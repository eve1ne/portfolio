"""
portfolio projects view.

URLs include:
/
"""
import flask
from functools import wraps
from datetime import datetime, timedelta, timezone
from flask import session, redirect, url_for, request, render_template, flash

import portfolio



@portfolio.app.route("/login", methods=["GET", "POST"])
def login():
    internship_password = portfolio.app.config['INTERNSHIP_PASSWORD']
    if request.method == "POST":
        if request.form.get("password") == internship_password:
            session["authorized"] = True
            session["expires_at"] = (datetime.now(timezone.utc) + timedelta(minutes=30)).timestamp()
            return redirect(url_for("show_project_detail", projectid=1))
        flash("Wrong password")
    return render_template("login.html")


@portfolio.app.route("/logout")
def logout():
    session.pop("authorized", None)
    session.pop("expires_at", None)
    flash("You have been logged out.")
    return redirect(url_for("login"))


# Decorator to protect specific project(s)
def password_protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        projectid = kwargs.get("projectid")
        if projectid == 1:
            expires_at = session.get("expires_at")
            if (
                not session.get("authorized")
                or not expires_at
                or datetime.now(timezone.utc).timestamp() > expires_at
            ):
                session.pop("authorized", None)
                session.pop("expires_at", None)
                flash("Your session has expired. Please log in again.")
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
    SELECT artid, title, description, image_url1, medium
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
        SELECT artid, title, description, image_url1, image_url2, image_url3, video_url1, video_url2, video_url3, medium, created_at
        FROM artworks
        WHERE artid = ?
        """, 
        (artid,))

    artwork = cur.fetchone()

    if artwork is None:
        flask.abort(404)

    return flask.render_template("artwork_detail.html", artwork=artwork)
