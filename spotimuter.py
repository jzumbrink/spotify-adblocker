import mute_list
import spotilib
import time

input("Press [ENTER] to start the program. After that, you have 2 seconds to make sure the Spotify Window is in foreground")
print("[", end="")
for _ in range(20):
    time.sleep(0.1)
    print("~", end="")
print("]")

spotInterface = spotilib.create_spotify_interface_obj(0)

print("The window id was successfully fetched. The window id is: {}".format(hex(spotInterface.window_id)))

is_muted = False

while True:
    current_spot_window_title = spotInterface.song_info()
    if current_spot_window_title in mute_list.mute_list:
        if not is_muted:
            spotilib.mute()
            is_muted = True
    else:
        # Allowed Song is playing
        if is_muted:
            spotilib.mute()
            is_muted = False

    time.sleep(0.1)
