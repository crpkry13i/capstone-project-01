from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import tekore as tk
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///music_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "secret"
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
spotify = tk.Spotify(app_token)

connect_db(app)

@app.route('/')
def index_page():
    results = spotify.artist_albums("1wAkNf5IFauLqZgJFY2mAg")
    return render_template('index.html', results=results)
