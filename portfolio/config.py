"""portfolio development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\x11)\xcd\x9a)\x05\xcd\x1c\xd0~\xb1\x14Vfrl\x82\xd3\xba\xad\x8f\xeds\xe6'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
PORTFOLIO_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = PORTFOLIO_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/portfolio.sqlite3
DATABASE_FILENAME = PORTFOLIO_ROOT/'var'/'portfolio.sqlite3'

