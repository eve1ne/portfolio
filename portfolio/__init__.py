"""portfolio package initializer."""
import flask
from dotenv import load_dotenv
import os

# Load .env file in the project root
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Load config values from environment variables (from .env)
app.config['INTERNSHIP_PASSWORD'] = os.getenv('INTERNSHIP_PASSWORD')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['FLASK_ENV'] = os.getenv('FLASK_ENV', 'production')

app.config.from_envvar('PORTFOLIO_SETTINGS', silent=True)

import portfolio.views  # noqa: E402  pylint: disable=wrong-import-position
import portfolio.model  # noqa: E402  pylint: disable=wrong-import-position
