"""
portfolio projects view.

URLs include:
/
"""
import flask
import portfolio


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


@portfolio.app.route('/projects/<int:projectid>/')
def show_project_detail(projectid):
    """Display contents of specific project."""

    connection = portfolio.model.get_db()

    cur = connection.execute(
        """
        SELECT projectid, title, description, image_url, repo_url, doc_url, demo_url, created_at
        FROM projects
        WHERE projectid = ?
        """, 
        (projectid,))

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
