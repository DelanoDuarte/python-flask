from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_database(app):
    database = db.init_app(app)
    return db