
import os


location = "C:\\CodeMines\\files\\CodeMines"

folder_data = os.listdir(location)

for data in folder_data:
    data_path = os.path.join(location,data)
    if os.path.isfile(data_path):
        print(f"{data_path} - file")
    else:
        print(f"{data_path} - folder")