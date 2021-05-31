# Example Usage: python trending-tracks.py LoadTopTracks --local-scheduler
import luigi
from Utils.SpotifyUtils import SpotifyUtils

class ExtractTopTracks(luigi.Task) :
    def run(self):
        # Auth on Spotify
        spotify = SpotifyUtils('76f2693443984cd89a17b0c742c83253', '34208e0dbfec4baa8e166797d40f13fe')
        # Create playlist object
        playlist = spotify.getPlaylist('https://open.spotify.com/playlist/37i9dQZEVXbLp5XoPON0wI?si=007bb52706f04181')
        # Extract tracks from playlist
        tracks = spotify.getPlaylistTracks(playlist)
        with open('top_track_names.txt','a') as track_file:
            for track in tracks:
                track_file.write(track['track']['name'] + '\n')
                print(track['track']['name'])
            track_file.close()

    def output(self) :
        return luigi.LocalTarget('top_track_names.txt')

class LoadTopTracks(luigi.Task):

    def requires(self):
        return ExtractTopTracks()

    def run(self):
        # Insert rows into postgres table
        pass
        # with open('world.txt','w') as world_file :
        #     world_file.write('World')
        #     world_file.close()

    def output(self) :
        return luigi.LocalTarget('world.txt')

if __name__ == '__main__':
    luigi.run()