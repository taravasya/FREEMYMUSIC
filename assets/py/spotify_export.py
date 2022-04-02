import requests
import sys, os
import re
import codecs

def log_print(data, access_type, filename):
	__location__ = os.path.realpath(
	    os.path.join(os.getcwd(), os.path.dirname(__file__)))

	f = codecs.open(os.path.join(__location__ + '/'+filename), access_type, "utf-8")
	f.write(data)
	f.close()
	data = re.sub('\n', '', data)
	print(data.encode("unicode_escape").decode() + '</br>')

BASE_URL = 'https://api.spotify.com/v1/'

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
access_token = sys.argv[1]
spotify_settings = open(os.path.join(__location__ + '/private_spotify_settings.txt'), 'r').read().splitlines()
spotify_playlist_id = spotify_settings[2].split(":")[1]

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
	access_token = open(os.path.join(__location__ + '/private_spotify_token.txt')).read()
	headers = {
	    'Authorization': 'Bearer {token}'.format(token=access_token),
	    'Accept': 'application/json',
	    'Content-Type': 'application/json',
	    'Accept-Language': 'RU'
	}

r = requests.get(BASE_URL + 'playlists/' + spotify_playlist_id + '/tracks?market=RU&fields=items(track(name,artists(name),album(name))),total,next', headers=headers)
r = r.json()
spotify_tracks = r['items']

while r['next']:
	r = requests.get(r['next'], headers=headers)
	r = r.json()
	spotify_tracks += r['items']



for import_track in spotify_tracks:
	track_album = import_track['track']['album']['name']
	track_name = import_track['track']['name']
	track_artist = import_track['track']['artists'][0]['name']
	track_artist = track_artist.replace('The ', '')
	track_artist = track_artist.replace('Trio', '')
	track_artist = track_artist.replace('Quintet', '')
	track_artist = re.sub('( & .*)|(, .*)', '', track_artist)
	track_name = re.sub('( -.*)|( - .*)|(\(?feat .*)|( - Remastered \d{4}.*)|( - \d{4} Remastered .*)|(\\(feat.*)|( - Live.*)', '', track_name)
	removal_list_track = [' - Instrumental',' - Acoustic Version', ' - Edit']
	for word in removal_list_track:
		track_name = track_name.replace(word, " ")
	log_print(str(track_artist)+"::"+(track_name)+"::"+(track_album)+"\n", "a", spotify_playlist_id+'_tracks.txt')


