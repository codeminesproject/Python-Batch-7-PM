
# copy file from one location to another

import shutil

source_loc = "C:\\CodeMines\\files\\source\\myfile.txt"
destination_loc = "C:\\CodeMines\\files\\destination\\sample.txt"

shutil.copy(source_loc,destination_loc)

print("file copied")

