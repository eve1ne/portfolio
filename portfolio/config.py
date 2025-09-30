"""portfolio development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
PORTFOLIO_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = PORTFOLIO_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024


