import sys, os
import requests

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
spotify_client_data = open(os.path.join(__location__ + '/private_spotify_settings.txt'), 'r').read().splitlines()
SPOTIFY_CLIENT_ID = spotify_client_data[0].split(":")[1]
SPOTIFY_CLIENT_SECRET = spotify_client_data[1].split(":")[1]

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': SPOTIFY_CLIENT_ID,
    'client_secret': SPOTIFY_CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__ + '/private_spotify_token.txt'), "w")
f.write(access_token)
f.close()