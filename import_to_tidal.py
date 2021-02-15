from MYSETTINGS import *
import requests
import sys, os
import tidalapi
import re
import codecs

def log_print(data, access_type):
	__location__ = os.path.realpath(
	    os.path.join(os.getcwd(), os.path.dirname(__file__)))

	f = codecs.open(os.path.join(__location__ + '/log.txt'), access_type, "utf-8")
	f.write(data)
	f.close()
	print(data)

def try_import(import_tracks, service, my_playlist):
	log_print('', "w")	
	session = tidalapi.Session()
	session.login(tidal_login, tidal_password)
	uid = session.user.id
	favorites = tidalapi.Favorites(session, uid)

	# УДАЛИТЬ МОЙ ПЛЕЙЛИСТ:

	playlists = session.get_user_playlists(uid)
	for playlist in playlists:
			if	playlist.name == 'FreeMyMusic '+my_playlist:
					favorites.delete_playlist(playlist.id)

	# СОЗДАТЬ МОЙ ПЛЕЙЛИСТ СНОВА:
	favorites.add_playlist('FreeMyMusic '+my_playlist,'FreeMyMusic from ' + service +' playlist')
	playlists = session.get_user_playlists(uid)
	for playlist in playlists:
			if	playlist.name == 'FreeMyMusic '+my_playlist:
				playlist_id = playlist.id

	for import_track in import_tracks:
		tracks_results = 0
		track_name = import_track['name']
		track_artist = import_track['artist']
		track_artist = track_artist.replace('The ', '')
		do_search = session.search('track', track_name + ' ' + track_artist, 10)
		if len(do_search.tracks) > 0:
			tracks_results = 1
		else:
			track_artist = track_artist.replace('Trio', '')
			track_artist = track_artist.replace('Quintet', '')
			track_name = re.sub(' - Remastered \d{4}.*', '', track_name)
			track_name = re.sub(' - \d{4} Remastered .*', '', track_name)
			track_name = re.sub('\\(feat.*', '', track_name)
			track_name = re.sub(' - Live.*', '', track_name)
			removal_list_track = [' - Instrumental',' - Acoustic Version', ' - Edit']
			for word in removal_list_track:
				track_name = track_name.replace(word, " ")
			do_search = session.search('track', track_name + ' ' + track_artist, 10)
			if len(do_search.tracks) > 0:
				tracks_results = 2
			else:
				track_name = re.sub(' -.*', '', track_name)
				do_search = session.search('track', track_name + ' ' + track_artist, 10)
				if len(do_search.tracks) > 0:
					tracks_results = 3
		
		if tracks_results > 0:
			start_track_results = tracks_results
			for result in do_search.tracks:
				s = set(result.artists[0].name.lower().split()) & set(track_artist.lower().split())
				if s:
					results_to_log = (str(tracks_results) + ' >> ' + result.name + ' ||| ' + result.artists[0].name + ' ||| ' + result.album.name)
					favorites.add_playlist_track(result.id, playlist_id, 999)
					tracks_results = start_track_results
					break
				else:
					tracks_results = 5

			if tracks_results == 5:
				track_name = re.sub('( - .*)|(\(?feat .*)', '', track_name)
				do_search_last = session.search('track', track_name + ' ' + track_artist, 10)
				if len(do_search_last.tracks) > 0:
					for result_last in do_search_last.tracks:
						s = set(result_last.artists[0].name.lower().split()) & set(track_artist.lower().split())
						if s:
							results_to_log = (str(tracks_results) + ' >> ' + result_last.name + ' ||| ' + result_last.artists[0].name + ' ||| ' + result_last.album.name)
							favorites.add_playlist_track(result_last.id, playlist_id, 999)
							break
						else:
							tracks_results = 6
							results_to_log = ('!!!! >> ' + track_name + ' by ' + track_artist)
				else:
					results_to_log = ('!!! >> ' + track_name + ' by ' + track_artist)
		
		else:
			results_to_log = (str(tracks_results) + ' >> ' + track_name + ' by ' + track_artist)
		log_print(str(results_to_log)+"\n", "a")
