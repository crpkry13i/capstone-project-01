from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW!

# class Album(db.Model):
#     """Albums Model"""

#     __tablename__ = "albums"

#     id = db.Column(db.text, primary_key=True)
#     name = db.Column(db.Text)
#     release_date = db.Column(db.Text)
#     image = db.Column(db.Text)
