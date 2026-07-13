
# chaeck folder exist

import os

location = "C:\\CodeMines\\files\\CodeMines1"

if os.path.exists(location):
    print("Folder already exist")
else:
    os.makedirs(location)
    print("folder created")