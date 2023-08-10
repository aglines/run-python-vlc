# run-python-vlc
Python code to run multiple random media sources at the same time in separate windows, running a VLC player (python-vlc) embedded in a GUI (PySimpleGUI)

# Monitor measurements are specific to each setup. To find these:
- Run the screenfinder code found at https://www.pysimplegui.org/en/latest/cookbook/#recipe-positioning-windows-on-a-multi-monitor-setup-tkinter-version-of-pysimplegui-only
- Once found, update the list of tuples, locations[], in the first section


## done:
- plays a playlist
- position mult windows on mult monitors 
- plays multiple concurrent media files in different windows
- LibVLC spawns its own GUI, got better GUI to embed VLC in: PySimpleGUI

# todo:
- error handling, exit button not always functional
- testing scenarios
- randomize playlists
- save & load program settings 
