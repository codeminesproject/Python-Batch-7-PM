
import pandas as pd

student_df = pd.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\student.xlsx")
course_df = pd.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\courses.xlsx")

merge_df = pd.merge(student_df,course_df,left_on="Name",right_on="Student Name",how="outer")

merge_df.to_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\outer_join.xlsx",index=False)

print("file created")