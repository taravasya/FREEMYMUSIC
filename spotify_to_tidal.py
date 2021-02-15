from MYSETTINGS import *
from freemymusic.import_to_tidal import try_import
import requests
import sys, os
import re
import codecs

if tidal_import_playlist == '':
	tidal_import_playlist = 'Spotify'
	
BASE_URL = 'https://api.spotify.com/v1/'

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
access_token = open(os.path.join(__location__ + '/spotify_token.txt')).read()

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token),
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Accept-Language': 'RU'
}

r = requests.get(BASE_URL + 'me', headers=headers)
r = r.json()


if 'error' in r and r['error']['status'] > 0:
	os.system(os.path.join('python.exe ') + os.path.join(__location__ + '/spotify_token.py'))
	access_token = open(os.path.join(__location__ + '/spotify_token.txt')).read()
	headers = {
	    'Authorization': 'Bearer {token}'.format(token=access_token),
	    'Accept': 'application/json',
	    'Content-Type': 'application/json',
	    'Accept-Language': 'RU'
	}

r = requests.get(BASE_URL + 'playlists/' + spotify_playlist_id + '/tracks?market=RU&fields=items(track(name,artists(name))),total,next', headers=headers)
r = r.json()
spotify_tracks = r['items']

while r['next']:
	r = requests.get(r['next'], headers=headers)
	r = r.json()
	spotify_tracks += r['items']

spotify_tracks_export = []

for spotify_track in spotify_tracks:
	spotify_tracks_export.append({'name':spotify_track['track']['name'], 'artist':spotify_track['track']['artists'][0]['name']})

try_import(spotify_tracks_export, 'spotify', tidal_import_playlist)
