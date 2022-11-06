import spotilib

spotInterface = spotilib.create_spotify_interface_obj()

print(spotInterface.song_info())