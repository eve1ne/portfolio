"""
portfolio individual project view.

URLs include:
/
"""
import flask
import portfolio


@portfolio.app.route('/work/cs/<int:projectid>')
def show_cs_project(projectid):
    connection = portfolio.model.get_db()

    project = connection.execute(
        "SELECT * FROM cs_projects WHERE projectid = ?", (projectid,)
    ).fetchone()

    roles = connection.execute(
        "SELECT * FROM cs_project_roles WHERE projectid = ? ORDER BY display_order",
        (projectid,)
    ).fetchall()

    sections_raw = connection.execute(
        "SELECT * FROM cs_project_sections WHERE projectid = ?", (projectid,)
    ).fetchall()
    sections = {s['role']: s for s in sections_raw}

    active_tab = flask.request.args.get('tab', roles[0]['role'] if roles else 'frontend')

    active_section = sections.get(active_tab)
    highlights = []
    if active_section:
        highlights = connection.execute(
        """
            SELECT * FROM cs_section_highlights
            WHERE sectionid = ?
            ORDER BY display_order
        """, 
        (active_section['sectionid'],)).fetchall()

    return flask.render_template("projects/cs_project.html", project=project, roles=roles, sections=sections, active_tab=active_tab, highlights=highlights)


@portfolio.app.route('/work/<string:section>/<int:projectid>')
def show_art_project(section, projectid):
    connection = portfolio.model.get_db()

    project = connection.execute(
        "SELECT * FROM art_projects WHERE projectid = ?", (projectid,)
    ).fetchone()

    media = connection.execute(
    """
        SELECT * FROM art_project_media
        WHERE projectid = ?
        ORDER BY display_order
    """, 
    (projectid,)).fetchall()

    return flask.render_template("projects/art_project.html", project=project, media=media)
