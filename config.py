import os

class Config:
    # Get the database URL from the environment variable, with a fallback default
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'postgresql://user:password@localhost/bank'  # Fallback if env variable not set
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
