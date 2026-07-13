
import os

file_list = []
folder_list = []

location = "C:\\CodeMines\\files\\CodeMines"

folder_data = os.listdir(location)

for data in folder_data:
    data_path = os.path.join(location,data)
    if os.path.isfile(data_path):
        file_list.append(data)
    else:
        folder_list.append(data)
    
print("file list: ",file_list)
print("folder list:",folder_list)