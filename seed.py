"""Seed file to make sample data for db."""
from models import Album, db, connect_db
from app import app

# Create all tables
db.drop_all()
db.create_all()


a1 = Album(id='5l9OqH5UrekBwmqnfbRgeT', name="サイバーパンクな夏の夜", release_date="2021-07-09", image="", link="")
a2 = Album(id='6kp3pXVZs2sNmwZJTPyJaZ', name="タイムラインジャンピング", release_date="2021-06-11", image="", link="")
a3 = Album(id='2C7mPkz4XlBfGBHR2O72S0', name="Chamber of Visions", release_date="2021-04-09", image="", link="")
a4 = Album(id='2wChxKxFyDKgHtC2vqRA7r', name="The Girl with Many Playlists", release_date="2021-03-05", image="", link="")


db.session.add_all([a1, a2, a3, a4])

db.session.commit()
