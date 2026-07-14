
# read excel file

import pandas

location = "C:\\CodeMines\\files\\student_data.csv"

student_data = pandas.read_csv(location)

print(student_data)
print("datatype:",type(student_data))