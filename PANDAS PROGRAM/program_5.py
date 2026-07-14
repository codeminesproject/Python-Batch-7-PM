import pandas as pd

# add custom column Total in excel

# step 1: read data from excel and save into dataframe

df = pd.read_excel("C:\\CodeMines\\files\\CodeMines\\student_subject_marks.xlsx")

print(df)

df["Marks Obtained"] = df["Maths"] + df["English"] + df["Science"]

print(df)

df.to_excel("C:\\CodeMines\\files\\CodeMines\\updated_student_subject_marks.xlsx")

