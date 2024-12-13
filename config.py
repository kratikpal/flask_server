import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    # Get the database URL from the environment variable, with a fallback default
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
