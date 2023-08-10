import PySimpleGUI as sg
import vlc
from time import sleep
import os
from sys import platform
from pathlib import Path
import test_data

#----------- TEST DATA -----------#

# Four windows per monitor, two monitors
number_of_media = 8
locations = [(0,0), (0,720), (1280,0), (1280,720), (-2560,380), (-1280,380), (-2560,1000), (-1280,1000)]

# Four windows per monitor, one monitor
# number_of_media = 4
# locations = [(0,0), (0,720), (1280,0), (1280,720)]

#----------- PLAYLIST SETUP -----------#

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

def layout(number):
    # can't use the same layout each time, but it works using just an unused param
    return [
        [sg.Graph(canvas_size=(1280,720), graph_bottom_left=(0,0), graph_top_right=(0,0), key='-G-')],
        [sg.Button('Exit', size=(10,1), pad=(0,0))]]

window_names = {}
instance_names = {}
player_names = {}
media_names = {}

for i in range(1, number_of_media + 1):
    window_names['window' + str(i)] = sg.Window(str(i), layout(i), finalize=True, location=locations[i-1])
    instance_names['instance' + str(i)] = vlc.Instance()
    current_instance = instance_names['instance' + str(i)]

    # player_names['player' + str(i)] = instance_names['instance' + str(i)].media_player_new()
    player_names['player' + str(i)] = instance_names['instance' + str(i)].media_list_player_new()
    ordered_playlist = create_playlist(current_instance, filenames)

    # to get win handle, must get each media player from its media list player
    curr_media_player = player_names['player' + str(i)].get_media_player()
    curr_media_player.set_hwnd(window_names['window' + str(i)]['-G-'].Widget.winfo_id())

    player_names['player' + str(i)].set_media_list(ordered_playlist)


#----------- MAIN LOOP -----------#

i, paused = 0, [False, False]

while True:
    window, event, values = sg.read_all_windows(timeout=1000)
    for i in range(1,number_of_media + 1):
        player_names['player' + str(i)].play()
    # Not sure this closes OK but might not be relevant for deployment
    if (window_names['window' + str(i)] == sg.WIN_CLOSED) or (event == 'Exit'):
        break

#----------- CLEANUP -----------#

for i in range(1,number_of_media + 1):
    player_names['player' + str(i)].stop()
    player_names['player' + str(i)].release()
    instance_names['instance' + str(i)].release()
    window_names['window' + str(i)].close()
    