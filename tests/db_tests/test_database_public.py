"""
Test student-created SQL scripts.

EECS 485 Project 2

Andrew DeOrio <awdeorio@umich.edu>
"""
import pathlib


def test_sql_schema(db_connection):
    """Verify schema.sql produces correct tables.

    Note: 'db_connection' is a fixture fuction that provides an empty,
    in-memory sqlite3 database.  It is implemented in conftest.py and reused by
    many tests.  Docs: https://docs.pytest.org/en/latest/fixture.html
    """
    # Load student schema.sql
    schema_sql = pathlib.Path("sql/schema.sql").read_text(encoding='utf-8')
    assert "PRAGMA foreign_keys = ON" in schema_sql
    db_connection.executescript(schema_sql)
    db_connection.commit()

    # Verify column names in users table
    cur = db_connection.execute("PRAGMA table_info('users')")
    schema = cur.fetchall()
    columns = [i["name"] for i in schema]
    assert set(columns) == set((
        'username', 'fullname', 'email', 'filename', 'password', 'created',
    ))

    # Verify column names in posts table
    cur = db_connection.execute("PRAGMA table_info('posts')")
    schema = cur.fetchall()
    columns = [i["name"] for i in schema]
    assert set(columns) == set(('postid', 'filename', 'owner', 'created'))

    # Verify column names in following table
    cur = db_connection.execute("PRAGMA table_info('following')")
    schema = cur.fetchall()
    columns = [i["name"] for i in schema]
    assert set(columns) == set(('username1', 'username2', 'created'))

    # Verify column names in comments table
    cur = db_connection.execute("PRAGMA table_info('comments')")
    schema = cur.fetchall()
    columns = [i["name"] for i in schema]
    assert set(columns) == set((
        'commentid', 'owner', 'postid', 'text', 'created',
    ))

    # Verify column names in likes table
    cur = db_connection.execute("PRAGMA table_info('likes')")
    schema = cur.fetchall()
    columns = [i["name"] for i in schema]
    assert set(columns) == set(('owner', 'likeid', 'postid', 'created'))


def test_likeids(db_connection):
    """Verify data.sql produces correct likeids.

    Tests later, includes in project 3, will rely on certain likes having
    certain likeids.

    Note: 'db_connection' is a fixture fuction that provides an empty,
    in-memory sqlite3 database.  It is implemented in conftest.py and reused by
    many tests.  Docs: https://docs.pytest.org/en/latest/fixture.html
    """
    # Load student schema.sql and data.sql
    schema_sql = pathlib.Path("sql/schema.sql").read_text(encoding='utf-8')
    data_sql = pathlib.Path("sql/data.sql").read_text(encoding='utf-8')
    assert "PRAGMA foreign_keys = ON" in schema_sql
    assert "PRAGMA foreign_keys = ON" in data_sql
    db_connection.executescript(schema_sql)
    db_connection.executescript(data_sql)
    db_connection.commit()

    # Verify data in likes table
    cur = db_connection.execute(
        "SELECT likeid, owner, postid FROM likes ORDER BY likeid"
    )
    likes = cur.fetchall()
    assert likes == [
        {'likeid': 1, 'owner': 'awdeorio', 'postid': 1},
        {'likeid': 2, 'owner': 'michjc', 'postid': 1},
        {'likeid': 3, 'owner': 'jflinn', 'postid': 1},
        {'likeid': 4, 'owner': 'awdeorio', 'postid': 2},
        {'likeid': 5, 'owner': 'michjc', 'postid': 2},
        {'likeid': 6, 'owner': 'awdeorio', 'postid': 3},
    ]


def test_posts_autoincrement(db_connection):
    """Verify database uses AUTOINCREMENT for postids."""
    # Load student schema.sql
    schema_sql = pathlib.Path("sql/schema.sql").read_text(encoding='utf-8')
    assert "PRAGMA foreign_keys = ON" in schema_sql
    db_connection.executescript(schema_sql)
    db_connection.commit()

    # Add user awdeorio
    db_connection.execute(
        "INSERT INTO users(username, fullname, email, filename, password) "
        "VALUES ('awdeorio', 'Andrew DeOrio', 'awdeorio@umich.edu', "
        "'dummy.jpg', 'dummy'); "
    )

    # Add one new post and check postid
    db_connection.execute(
        "INSERT INTO posts(owner, filename) "
        " VALUES('awdeorio', '122a7d27ca1d7420a1072f695d9290fad4501a41.jpg')"
    )
    cur = db_connection.execute("SELECT postid FROM posts")
    postids = cur.fetchall()
    assert postids == [{'postid': 1}]

    # Delete post
    db_connection.execute("DELETE FROM posts")
    db_connection.commit()

    # Add one new post and check postid, it should *not* reuse deleted postids
    db_connection.execute(
        "INSERT INTO posts(owner, filename) "
        " VALUES('awdeorio', '122a7d27ca1d7420a1072f695d9290fad4501a41.jpg')"
    )
    cur = db_connection.execute("SELECT postid FROM posts")
    postids = cur.fetchall()
    assert postids == [{'postid': 2}]


def test_sql_data_users_posts(db_connection):
    """Verify data.sql produces correct tables: users, posts.

    Note: 'db_connection' is a fixture fuction that provides an empty,
    in-memory sqlite3 database.  It is implemented in conftest.py and reused by
    many tests.  Docs: https://docs.pytest.org/en/latest/fixture.html
    """
    # Load student schema.sql and data.sql
    schema_sql = pathlib.Path("sql/schema.sql").read_text(encoding='utf-8')
    data_sql = pathlib.Path("sql/data.sql").read_text(encoding='utf-8')
    assert "PRAGMA foreign_keys = ON" in schema_sql
    assert "PRAGMA foreign_keys = ON" in data_sql
    db_connection.executescript(schema_sql)
    db_connection.executescript(data_sql)
    db_connection.commit()

    # Verify data in users table
    cur = db_connection.execute(
        "SELECT username, email, fullname, filename, password FROM users"
    )
    users = cur.fetchall()
    assert users == [
        {
            'username': 'awdeorio',
            'email': 'awdeorio@umich.edu',
            'fullname': 'Andrew DeOrio',
            'filename': 'e1a7c5c32973862ee15173b0259e3efdb6a391af.jpg',
            'password': ('sha512$34e94a05cdf247db92a84bc590950336$'
                         '7eaca2b4169e042120f015666115856c717343f1c75'
                         'd1c1bd1bf469bd1cd439eb152ccda6a0b8703706dfb'
                         'cb861b3cef9208325c31f436e8edb9563f01176c48'
                         ),
        },
        {
            'username': 'jflinn',
            'email': 'jflinn@umich.edu',
            'fullname': 'Jason Flinn',
            'filename': '505083b8b56c97429a728b68f31b0b2a089e5113.jpg',
            'password': ('sha512$673d22398b0141c7929f987efee061e6$'
                         '187dd68d62574a29b40513467cb5376849d6e7651db'
                         'd19850b853b912f44d940a42ef6bb96f4bafa82a6b4'
                         '0072ed980bfad377c65faa096281369210841f2b73'
                         ),
        },
        {
            'username': 'michjc',
            'email': 'michjc@umich.edu',
            'fullname': 'Michael Cafarella',
            'filename': '5ecde7677b83304132cb2871516ea50032ff7a4f.jpg',
            'password': ('sha512$d7cde81ee4614141b68fbe8ff5fffa76$'
                         '8b432b218b18554e58a949a40367a0d0e731dc8f8a4'
                         '6ecaa3ea0aca39169b3a97f12246d2840d6e9c32764'
                         '907ed7b1951dfc16f213cb7fd4a6a96dc43f52f67b'
                         ),
        },
        {
            'username': 'jag',
            'email': 'jag@umich.edu',
            'fullname': 'H.V. Jagadish',
            'filename': '73ab33bd357c3fd42292487b825880958c595655.jpg',
            'password': ('sha512$0b2b8d18beba4c2ba7dad0365d1dd885$'
                         '130546cafab793f769a86607466fb07476b03c5de1f'
                         '32f666c1e72e8b48b5e7e08494ec85ede12df72d259'
                         '112bca3d5783983937361fe0aa2c341ae7bd0c2da4'
                         ),
        },
    ]

    # Verify data in posts table
    cur = db_connection.execute("SELECT postid, owner, filename FROM posts")
    posts = cur.fetchall()
    assert posts == [
        {
            'filename': '122a7d27ca1d7420a1072f695d9290fad4501a41.jpg',
            'owner': 'awdeorio',
            'postid': 1,
        },
        {
            'filename': 'ad7790405c539894d25ab8dcf0b79eed3341e109.jpg',
            'owner': 'jflinn',
            'postid': 2,
        },
        {
            'filename': '9887e06812ef434d291e4936417d125cd594b38a.jpg',
            'owner': 'awdeorio',
            'postid': 3,
        },
        {
            'filename': '2ec7cf8ae158b3b1f40065abfb33e81143707842.jpg',
            'owner': 'jag',
            'postid': 4,
        }
    ]
