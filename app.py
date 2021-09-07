from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import tekore as tk
import asyncio
from models import db, connect_db
from secret import client_id, client_secret
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///music_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secretbackup')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


BASE_API = "https://api.spotify.com"
AUTH = "https://accounts.spotify.com/authorize"
MY_URI = "spotify:artist:1wAkNf5IFauLqZgJFY2mAg"

client_id = client_id
client_secret = client_secret
redirect_uri = "http://127.0.0.1:5000"

# Retrieving a client token
app_token = tk.request_client_token(client_id, client_secret)

# Calling the API
spotify = tk.Spotify(app_token, sender=tk.AsyncSender())

# Artist ID
ryleinathaniel = "1wAkNf5IFauLqZgJFY2mAg"

async def get_artist_albums():
	return await spotify.artist_albums(ryleinathaniel, limit=50)

albums = asyncio.run(get_artist_albums())


connect_db(app)

# for item in albums.items:
# 	print(item)

@app.route('/')
def index_page():
	album_image = albums.items[0].images[1].url
	album_image1 = albums.items[1].images[1].url
	album_image2 = albums.items[2].images[1].url
	album_image3 = albums.items[3].images[1].url
	album_name = albums.items[0].name
	album_name1 = albums.items[1].name
	album_name2 = albums.items[2].name
	album_name3 = albums.items[3].name
	release_date = albums.items[0].release_date
	release_date1 = albums.items[1].release_date
	release_date2 = albums.items[2].release_date
	release_date3 = albums.items[3].release_date
	album_link = albums.items[0].external_urls['spotify']
	album_link1 = albums.items[1].external_urls['spotify']
	album_link2 = albums.items[2].external_urls['spotify']
	album_link3 = albums.items[3].external_urls['spotify']
	return render_template('01.html', 
		album_image=album_image,
    album_image1=album_image1,
    album_image2=album_image2,
    album_image3=album_image3,
		album_name=album_name,
    album_name1=album_name1,
    album_name2=album_name2,
    album_name3=album_name3,
		release_date=release_date,
    release_date1=release_date1,
    release_date2=release_date2,
    release_date3=release_date3,
		album_link=album_link,
    album_link1=album_link1,
    album_link2=album_link2,
    album_link3=album_link3)


@app.route('/2')
def second_page():
	album_image = albums.items[4].images[1].url
	album_image1 = albums.items[5].images[1].url
	album_image2 = albums.items[6].images[1].url
	album_image3 = albums.items[7].images[1].url
	album_name = albums.items[4].name
	album_name1 = albums.items[5].name
	album_name2 = albums.items[6].name
	album_name3 = albums.items[7].name
	release_date = albums.items[4].release_date
	release_date1 = albums.items[5].release_date
	release_date2 = albums.items[6].release_date
	release_date3 = albums.items[7].release_date
	album_link = albums.items[4].external_urls['spotify']
	album_link1 = albums.items[5].external_urls['spotify']
	album_link2 = albums.items[6].external_urls['spotify']
	album_link3 = albums.items[7].external_urls['spotify']
	return render_template('02.html',
    album_image=album_image,
    album_image1=album_image1,
    album_image2=album_image2,
    album_image3=album_image3,
    album_name=album_name,
    album_name1=album_name1,
    album_name2=album_name2,
    album_name3=album_name3,
    release_date=release_date,
    release_date1=release_date1,
    release_date2=release_date2,
    release_date3=release_date3,
    album_link=album_link,
    album_link1=album_link1,
    album_link2=album_link2,
    album_link3=album_link3)


@app.route('/3')
def third_page():
	album_image = albums.items[8].images[1].url
	album_image1 = albums.items[9].images[1].url
	album_image2 = albums.items[10].images[1].url
	album_image3 = albums.items[11].images[1].url
	album_name = albums.items[8].name
	album_name1 = albums.items[9].name
	album_name2 = albums.items[10].name
	album_name3 = albums.items[11].name
	release_date = albums.items[8].release_date
	release_date1 = albums.items[9].release_date
	release_date2 = albums.items[10].release_date
	release_date3 = albums.items[11].release_date
	album_link = albums.items[8].external_urls['spotify']
	album_link1 = albums.items[9].external_urls['spotify']
	album_link2 = albums.items[10].external_urls['spotify']
	album_link3 = albums.items[11].external_urls['spotify']
	return render_template('03.html',
    album_image=album_image,
    album_image1=album_image1,
    album_image2=album_image2,
    album_image3=album_image3,
    album_name=album_name,
    album_name1=album_name1,
    album_name2=album_name2,
    album_name3=album_name3,
    release_date=release_date,
    release_date1=release_date1,
    release_date2=release_date2,
    release_date3=release_date3,
    album_link=album_link,
    album_link1=album_link1,
    album_link2=album_link2,
    album_link3=album_link3)


@app.route('/4')
def fourth_page():
	album_image = albums.items[12].images[1].url
	album_image1 = albums.items[13].images[1].url
	album_image2 = albums.items[14].images[1].url
	album_image3 = albums.items[15].images[1].url
	album_name = albums.items[12].name
	album_name1 = albums.items[13].name
	album_name2 = albums.items[14].name
	album_name3 = albums.items[15].name
	release_date = albums.items[12].release_date
	release_date1 = albums.items[13].release_date
	release_date2 = albums.items[14].release_date
	release_date3 = albums.items[15].release_date
	album_link = albums.items[12].external_urls['spotify']
	album_link1 = albums.items[13].external_urls['spotify']
	album_link2 = albums.items[14].external_urls['spotify']
	album_link3 = albums.items[15].external_urls['spotify']
	return render_template('04.html',
    album_image=album_image,
    album_image1=album_image1,
    album_image2=album_image2,
    album_image3=album_image3,
    album_name=album_name,
    album_name1=album_name1,
    album_name2=album_name2,
    album_name3=album_name3,
    release_date=release_date,
    release_date1=release_date1,
    release_date2=release_date2,
    release_date3=release_date3,
    album_link=album_link,
    album_link1=album_link1,
    album_link2=album_link2,
    album_link3=album_link3)


@app.route('/5')
def fifth_page():
	album_image = albums.items[16].images[1].url
	album_image1 = albums.items[17].images[1].url
	album_image2 = albums.items[18].images[1].url
	album_image3 = albums.items[19].images[1].url
	album_name = albums.items[16].name
	album_name1 = albums.items[17].name
	album_name2 = albums.items[18].name
	album_name3 = albums.items[19].name
	release_date = albums.items[16].release_date
	release_date1 = albums.items[17].release_date
	release_date2 = albums.items[18].release_date
	release_date3 = albums.items[19].release_date
	album_link = albums.items[16].external_urls['spotify']
	album_link1 = albums.items[17].external_urls['spotify']
	album_link2 = albums.items[18].external_urls['spotify']
	album_link3 = albums.items[19].external_urls['spotify']
	return render_template('05.html',
    album_image=album_image,
    album_image1=album_image1,
    album_image2=album_image2,
    album_image3=album_image3,
    album_name=album_name,
    album_name1=album_name1,
    album_name2=album_name2,
    album_name3=album_name3,
    release_date=release_date,
    release_date1=release_date1,
    release_date2=release_date2,
    release_date3=release_date3,
    album_link=album_link,
    album_link1=album_link1,
    album_link2=album_link2,
    album_link3=album_link3)


@app.route('/6')
def sixth_page():
	album_image = albums.items[20].images[1].url
	album_image1 = albums.items[21].images[1].url
	album_image2 = albums.items[22].images[1].url
	album_image3 = albums.items[23].images[1].url
	album_name = albums.items[20].name
	album_name1 = albums.items[21].name
	album_name2 = albums.items[22].name
	album_name3 = albums.items[23].name
	release_date = albums.items[20].release_date
	release_date1 = albums.items[21].release_date
	release_date2 = albums.items[22].release_date
	release_date3 = albums.items[23].release_date
	album_link = albums.items[20].external_urls['spotify']
	album_link1 = albums.items[21].external_urls['spotify']
	album_link2 = albums.items[22].external_urls['spotify']
	album_link3 = albums.items[23].external_urls['spotify']
	return render_template('06.html',
    album_image=album_image,
    album_image1=album_image1,
    album_image2=album_image2,
    album_image3=album_image3,
    album_name=album_name,
    album_name1=album_name1,
    album_name2=album_name2,
    album_name3=album_name3,
    release_date=release_date,
    release_date1=release_date1,
    release_date2=release_date2,
    release_date3=release_date3,
    album_link=album_link,
    album_link1=album_link1,
    album_link2=album_link2,
    album_link3=album_link3)


@app.route('/7')
def seventh_page():
	album_image = albums.items[24].images[1].url
	album_image1 = albums.items[25].images[1].url
	album_image2 = albums.items[26].images[1].url
	album_image3 = albums.items[27].images[1].url
	album_name = albums.items[24].name
	album_name1 = albums.items[25].name
	album_name2 = albums.items[26].name
	album_name3 = albums.items[27].name
	release_date = albums.items[24].release_date
	release_date1 = albums.items[25].release_date
	release_date2 = albums.items[26].release_date
	release_date3 = albums.items[27].release_date
	album_link = albums.items[24].external_urls['spotify']
	album_link1 = albums.items[25].external_urls['spotify']
	album_link2 = albums.items[26].external_urls['spotify']
	album_link3 = albums.items[27].external_urls['spotify']
	return render_template('07.html',
    album_image=album_image,
    album_image1=album_image1,
    album_image2=album_image2,
    album_image3=album_image3,
    album_name=album_name,
    album_name1=album_name1,
    album_name2=album_name2,
    album_name3=album_name3,
    release_date=release_date,
    release_date1=release_date1,
    release_date2=release_date2,
    release_date3=release_date3,
    album_link=album_link,
    album_link1=album_link1,
    album_link2=album_link2,
    album_link3=album_link3)


@app.route('/8')
def eighth_page():
	album_image = albums.items[28].images[1].url
	album_image1 = albums.items[29].images[1].url
	album_image2 = albums.items[30].images[1].url
	# album_image3 = albums.items[31].images[1].url
	album_name = albums.items[28].name
	album_name1 = albums.items[29].name
	album_name2 = albums.items[30].name
	# album_name3 = albums.items[31].name
	release_date = albums.items[28].release_date
	release_date1 = albums.items[29].release_date
	release_date2 = albums.items[30].release_date
	# release_date3 = albums.items[31].release_date
	album_link = albums.items[28].external_urls['spotify']
	album_link1 = albums.items[29].external_urls['spotify']
	album_link2 = albums.items[30].external_urls['spotify']
	# album_link3 = albums.items[31].external_urls['spotify']
	return render_template('08.html',
    album_image=album_image,
    album_image1=album_image1,
    album_image2=album_image2,
    # album_image3=album_image3,
    album_name=album_name,
    album_name1=album_name1,
    album_name2=album_name2,
    # album_name3=album_name3,
    release_date=release_date,
    release_date1=release_date1,
    release_date2=release_date2,
    # release_date3=release_date3,
    album_link=album_link,
    album_link1=album_link1,
    album_link2=album_link2,
    # album_link3=album_link3
	)
