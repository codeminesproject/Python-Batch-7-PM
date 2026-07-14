
# read excel file

import pandas

location = "C:\\CodeMines\\files\\student_data.xlsx"

student_data = pandas.read_excel(location)

print(student_data)
print("datatype:",type(student_data))