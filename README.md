# run-python-vlc
Python code to run multiple random media sources at the same time, running a VLC player (python-vlc) embedded in a GUI (PySimpleGUI)

# todo
- multiple concurrent VLC instances
- random playlist

## problems and solutions done:
- LibVLC spawns its own GUI, so testing means multiple unused windows which can't be closed until the kernel restarts 
- Needed a better GUI to embed VLC in, even if I only add basic user features: enter PySimpleGUI
 