import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyUtils:
    def __init__(self, client_id, client_secret):
        self.api = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(
                client_secret=client_secret,
                client_id=client_id
            )
        )

    def getArtist(self, id):
        return self.api.artist(id)

    def getArtistAlbums(self, id, album_type='album'):
        results = self.api.artist_albums(id, album_type=album_type)
        albums = results['items']
        while results['next']:
            results = self.api.next(results)
            albums.extend(results['items'])
        return albums

    def getPlaylist(self, id):
        return self.api.playlist(id)

    def getPlaylistTracks(self, playlist):
        tracks = playlist['tracks']['items']
        while playlist['tracks']['next']:
            playlist = self.api.next(playlist)
            tracks.extend(playlist['items'])
        return tracks

    
    

# def main():
#     spotify = SpotifyUtils('76f2693443984cd89a17b0c742c83253', '34208e0dbfec4baa8e166797d40f13fe')
#     # print(spotify.getArtistAlbums('spotify:artist:2WX2uTcsvV5OnS0inACecP'))
#     spotify.api.featured_playlists(locale=None, country=None)

# main()