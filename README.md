# run-python-vlc
Python code to run multiple random media sources at the same time in separate windows, running a VLC player (python-vlc) embedded in a GUI (PySimpleGUI)

# todo:
- position windows on mult monitors
- save & load program settings 
- play a playlist


## done:
- multiple concurrent VLC instances
- LibVLC spawns its own uncontrollable GUI. Testing produced multiple uncloseable windows
- Needed better GUI to embed VLC in, even if I only add basic user features: enter PySimpleGUI
 