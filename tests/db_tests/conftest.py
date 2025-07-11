"""
Shared test fixtures.

Pytest will automatically run the db_setup_teardown() function before a
test.  A test should use "db_connnection" as an input, because the name of the
fixture is "db_connection".

EXAMPLE:
>>> def test_simple(db_connection):
>>>     schema_sql = pathlib.Path("sql/schema.sql").read_text(encoding='utf-8')
>>>     data_sql = pathlib.Path("sql/data.sql").read_text(encoding='utf-8')
>>>     db_connection.executescript(schema_sql)
>>>     db_connection.executescript(data_sql)
>>>     db_connection.commit()

Pytest docs:
https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions
"""
import sqlite3
import pytest


@pytest.fixture(name="db_connection")
def db_setup_teardown():
    """
    Create an in-memory sqlite3 database.

    This fixture is used only for the database tests, not the insta485 tests.
    """
    # Create a temporary in-memory database
    db_connection = sqlite3.connect(":memory:")

    # Configure database to return dictionaries keyed on column name
    def dict_factory(cursor, row):
        """Convert database row objects to a dict keyed on column name."""
        return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    db_connection.row_factory = dict_factory

    # Foreign keys have to be enabled per-connection.  This is an sqlite3
    # backwards compatibility thing.
    db_connection.execute("PRAGMA foreign_keys = ON")

    # Transfer control to test.  The code before the "yield" statement is setup
    # code, which is executed before the test.  Code after the "yield" is
    # teardown code, which is executed at the end of the test.  Teardown code
    # is executed whether the test passed or failed.
    yield db_connection

    # Verify foreign key support is still enabled
    cur = db_connection.execute("PRAGMA foreign_keys")
    foreign_keys_status = cur.fetchone()
    assert foreign_keys_status["foreign_keys"], \
        "Foreign keys appear to be disabled."

    # Destroy database
    db_connection.close()
