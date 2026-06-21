"""
portfolio index (work) view.

URLs include:
/
"""
import flask
import portfolio


@portfolio.app.route('/work/cs')
def show_cs():
    connection = portfolio.model.get_db()
    active_filter = flask.request.args.get('filter', 'all')

    section = connection.execute(
        "SELECT * FROM work_sections WHERE type = 'cs'"
    ).fetchone()

    skills = connection.execute(
        """
        SELECT skill FROM section_skills
        WHERE sectionid = ?
        ORDER BY skillid
        """, (section['sectionid'],)
    ).fetchall()

    if active_filter == 'all':
        projects = connection.execute(
        """
            SELECT p.*, GROUP_CONCAT(DISTINCT pr.role) as roles, MIN(pr.role) as default_role
            FROM cs_projects p
            JOIN cs_project_roles pr ON p.projectid = pr.projectid
            WHERE p.is_visible = 1
            GROUP BY p.projectid
            ORDER BY p.display_order
        """
        ).fetchall()
    else:
        projects = connection.execute(
        """
            SELECT p.*, GROUP_CONCAT(DISTINCT pr.role) as roles, ? as default_role
            FROM cs_projects p
            JOIN cs_project_roles pr ON p.projectid = pr.projectid
            WHERE p.is_visible = 1 AND pr.role = ?
            GROUP BY p.projectid
            ORDER BY p.display_order
        """, 
        (active_filter, active_filter)).fetchall()

    section = connection.execute(
        "SELECT * FROM work_sections WHERE type = 'cs'"
    ).fetchone()

    return flask.render_template("work/cs.html", projects=projects, section=section, skills=skills, active_filter=active_filter)


@portfolio.app.route('/work/design')
def show_design():
    connection = portfolio.model.get_db()

    section = connection.execute(
        "SELECT * FROM work_sections WHERE type = 'design'"
    ).fetchone()

    skills = connection.execute(
        """
        SELECT skill FROM section_skills
        WHERE sectionid = ?
        ORDER BY skillid
        """, (section['sectionid'],)
    ).fetchall()

    projects = connection.execute(
    """
        SELECT * FROM art_projects
        WHERE type = 'design' AND is_visible = 1
        ORDER BY display_order
    """
    ).fetchall()
    section = connection.execute(
        "SELECT * FROM work_sections WHERE type = 'design'"
    ).fetchone()
    return flask.render_template("work/design.html", projects=projects, section=section, skills=skills)


@portfolio.app.route('/work/animation')
def show_animation():
    connection = portfolio.model.get_db()

    section = connection.execute(
        "SELECT * FROM work_sections WHERE type = 'animation'"
    ).fetchone()

    skills = connection.execute(
        """
        SELECT skill FROM section_skills
        WHERE sectionid = ?
        ORDER BY skillid
        """, (section['sectionid'],)
    ).fetchall()

    projects = connection.execute(
    """
        SELECT * FROM art_projects
        WHERE type = 'animation' AND is_visible = 1
        ORDER BY display_order
    """
    ).fetchall()
    section = connection.execute(
        "SELECT * FROM work_sections WHERE type = 'animation'"
    ).fetchone()
    return flask.render_template("work/animation.html", projects=projects, section=section, skills=skills)


@portfolio.app.route('/work/media')
def show_media():
    connection = portfolio.model.get_db()
    active_filter = flask.request.args.get('filter', 'all')

    section = connection.execute(
        "SELECT * FROM work_sections WHERE type = 'media'"
    ).fetchone()

    skills = connection.execute(
        """
        SELECT skill FROM section_skills
        WHERE sectionid = ?
        ORDER BY skillid
        """, (section['sectionid'],)
    ).fetchall()

    if active_filter == 'all':
        projects = connection.execute(
        """
            SELECT * FROM art_projects
            WHERE type IN ('video', 'photo') AND is_visible = 1
            ORDER BY display_order
        """
        ).fetchall()
    else:
        projects = connection.execute(
        """
            SELECT * FROM art_projects
            WHERE type = ? AND is_visible = 1
            ORDER BY display_order
        """, 
        (active_filter,)).fetchall()

    section = connection.execute(
        "SELECT * FROM work_sections WHERE type = 'media'"
    ).fetchone()
    return flask.render_template("work/media.html", projects=projects, section=section, skills=skills, active_filter=active_filter)
