
# check file exist and remove

import os

file_name = "C:\\CodeMines\\files\\destination\\introduction.txt"

isExist = os.path.exists(file_name)
# True -> file exist
# False -> file does not exist

print(isExist)

if os.path.exists(file_name):
    os.remove(file_name)
    print("file deleted")
else:
    print("file does not exist")