"""portfolio package initializer."""
import flask
from dotenv import load_dotenv
import os

# project root: /srv/portfolio
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', 'var', '.env'))

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Load config values from environment variables (from .env)
app.config['INTERNSHIP_PASSWORD'] = os.getenv('INTERNSHIP_PASSWORD')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['FLASK_ENV'] = os.getenv('FLASK_ENV', 'production')
app.config['DATABASE_FILENAME'] = os.getenv('DATABASE_FILENAME', 'var/portfolio.sqlite3')



import portfolio.views  # noqa: E402  pylint: disable=wrong-import-position
import portfolio.model  # noqa: E402  pylint: disable=wrong-import-position
