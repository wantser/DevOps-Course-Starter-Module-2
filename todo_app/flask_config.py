import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.urandom(24)
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
