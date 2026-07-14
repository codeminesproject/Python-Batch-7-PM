
# prepare excel file

import pandas

student_data = [{"id":1,"name":"Vedant","mobile":"1234567890"},
                {"id":2,"name":"Veena","mobile":"9876787654"},
                {"id":3,"name":"Nilima","mobile":"1233457890"},
                {"id":4,"name":"Arman","mobile":"123987890"},
                {"id":5,"name":"Aditya","mobile":"129876890"}]

print(student_data)

# convert dictionary into dataframe

df = pandas.DataFrame(student_data)

print(df)

# rename column names
df = df.rename(columns={"id":"Student ID","name":"Student Name","mobile":"Student Mobile Number"})

df.to_csv("C:\\CodeMines\\files\\CodeMines\\codemines_students.csv",index=False)

print("CSV File Created")

