import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'postgresql://my_database_0ijx_user:m19zfx2eFnMVnb4c21LXEd7SW9P3sOfX@dpg-ctdrngilqhvc73d8qemg-a.singapore-postgres.render.com/my_database_0ijx'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
