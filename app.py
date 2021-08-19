from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import tekore as tk
import asyncio
from models import db, connect_db
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///music_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secretbackup')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


BASE_API = "https://api.spotify.com"
AUTH = "https://accounts.spotify.com/authorize"
MY_URI = "spotify:artist:1wAkNf5IFauLqZgJFY2mAg"

client_id = "8fbed18498c2466db7bb5253d588f6ac"
client_secret = "83e6aa9fa09741289506e394cc726af7"
redirect_uri = "http://127.0.0.1:5000"

# Retrieving a client token
app_token = tk.request_client_token(client_id, client_secret)

# Calling the API
spotify = tk.Spotify(app_token, sender=tk.AsyncSender())

# Artist ID
ryleinathaniel = "1wAkNf5IFauLqZgJFY2mAg"

async def get_artist_albums():
    return await spotify.artist_albums(ryleinathaniel, limit=5)

albums = asyncio.run(get_artist_albums())

connect_db(app)

for item in albums.items:
    print(item)

@app.route('/')
def index_page():
    album_image = albums.items[0].images[1].url
    album_name = albums.items[0].name
    release_date = albums.items[0].release_date
    album_link = albums.items[0].external_urls['spotify']
    return render_template('index.html', 
        album_image=album_image, 
        album_name=album_name, 
        release_date=release_date,
        album_link=album_link)
