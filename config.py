import os

class Config:
    # Flask app configurations
    DEBUG = True
    SECRET_KEY = '0Hp1pzhZN2ID0DfNpA4lc3-bVWXPjI0yaqGTdru3OcA'  # Replace with your Flask secret key

    # SQLAlchemy configurations
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Example: SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Bcrypt configurations
    BCRYPT_LOG_ROUNDS = 12

    # JWT configurations
    JWT_SECRET_KEY = '9St-i4JTKBXWJXuG7yHWSzDxH_yjolPVjUqnYv6kXUI'  # Replace with your JWT secret key
    JWT_TOKEN_LOCATION = ['headers', 'cookies']  # Specify where to look for JWT tokens
    JWT_COOKIE_SECURE = False  # Set to True if using HTTPS
    JWT_COOKIE_CSRF_PROTECT = False  # Enable CSRF protection for cookies

    # Example: Set the maximum token expiration time to 7 days
    JWT_ACCESS_TOKEN_EXPIRES = 7 * 24 * 3600

    # Flask-Login configurations
    LOGIN_DISABLED = False  # Set to True to disable Flask-Login

    # Other configurations...
