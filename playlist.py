import PySimpleGUI as sg
import vlc
from time import sleep
import os
import sys
#from sys import platform
from pathlib import Path
import test_data

#----------- MONITOR SETUP -----------#
#window_locations = []

number_of_windows = test_data.monitor_count
match number_of_windows:
    case 4:
        window_locations = [(0,0), (0,720), (1280,0), (1280,720)]
    case 8:
        window_locations = [(0,0), (0,720), (1280,0), (1280,720), (-2560,380), (-1280,380), (-2560,1000), (-1280,1000)]
    case _:
        sys.exit("error, ensure the value number_of_windows is either 4 or 8 in test_data.py")

# if number_of_windows == 4:
#     window_locations = [(0,0), (0,720), (1280,0), (1280,720)]
# elif number_of_windows == 8:
#     window_locations = [(0,0), (0,720), (1280,0), (1280,720), (-2560,380), (-1280,380), (-2560,1000), (-1280,1000)]
# else:
#     print("error, ensure the value number_of_windows is either 4 or 8 in test_data.py")
#     exit()

#----------- TEST DATA / PLAYLIST SETUP -----------#

playlist = test_data.media_path
allowed_filetypes = test_data.allowed_filetypes
filenames = list(Path(playlist).iterdir())

def create_playlist(vlc_instance, filenames):
    ordered_playlist = vlc_instance.media_list_new()
    for file in filenames:
        if file.suffix in (allowed_filetypes):
            ordered_playlist.add_media(file)
    return ordered_playlist


#----------- GUI SETUP -----------#

# Unused param because it errors using the same key for multiple windows. this gets around it 
def layout(number):
    return [
        [sg.Graph(canvas_size=(1280,720), graph_bottom_left=(0,0), graph_top_right=(0,0), key='-G-')],
        [sg.Button('Exit', size=(10,1), pad=(0,0))]]

windows = []
instances = []
players = []

for i in range(number_of_windows):

    # first arg is a required unique window name, hence stringified i
    window = sg.Window(str(i), layout(i), finalize=True, location=window_locations[i])

    instance = vlc.Instance()
    player = instance.media_list_player_new()

    # Plan is to randomize this later, otherwise it would be the same order on every screen
    # ..better to extract this outside the loop probably
    ordered_playlist = create_playlist(instance, filenames)

    curr_media_player = player.get_media_player()
    curr_media_player.set_hwnd(window['-G-'].Widget.winfo_id())
    player.set_media_list(ordered_playlist)

    windows.append(window)
    instances.append(instance)
    players.append(player)


#----------- MAIN LOOP -----------#

i, paused = 0, [False, False]

while True:
    window, event, values = sg.read_all_windows(timeout=1000)
    for i in range(number_of_windows):
        players[i].play()
        if (windows[i] == sg.WIN_CLOSED) or (event == 'Exit'):
            windows[i].close()
            # players[i].stop()
            # players[i].release()
            # instances[i].release()
            sys.exit("Closed by user")

#----------- CLEANUP -----------#
# Looks like a known issue closing windows cleanly if read_all_windows is used 
