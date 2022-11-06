import mute_list
import spotilib
import time

# Please make sure that your computer is not muted when starting this script
# it is assumed that the computer is not muted

input("Press [ENTER] to start the program. After that, you have 2 seconds to make sure the Spotify Window is in "
      "foreground")
print("[", end="")
for _ in range(20):
    time.sleep(0.1)
    print("~", end="")
print("]")

spotInterface = spotilib.create_spotify_interface_obj(0)

print("The window id was successfully fetched. The window id is: {}".format(hex(spotInterface.window_id)))

is_muted = False

last_spot_window_title = ""

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

    # Provide the user with information about the current track and the block status
    if current_spot_window_title != last_spot_window_title:
        print("Currently playing: {}".format(current_spot_window_title))
        print("Song status = {}".format("BLOCKED" if is_muted else "ALLOWED"))
        last_spot_window_title = current_spot_window_title

    time.sleep(0.1)
