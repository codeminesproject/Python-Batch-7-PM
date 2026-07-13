
import os

location = "C:\\CodeMines\\files\\destination"

file_1 = "Lecture 1 - introduction.pdf"
file_2 = "Lecture 2 - Data Model Normalisation.pdf"

file_1_loc = os.path.join(location,file_1)
file_2_loc = os.path.join(location,file_2)

print(file_1_loc)
print(file_2_loc)