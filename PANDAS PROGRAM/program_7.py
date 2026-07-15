
import pandas as pd

df = pd.read_excel("C:\\CodeMines\\files\\CodeMines\\employee_data.xlsx")

print("---- total salary ----")

print(df["Salary"].sum())

print("---- min salary ----")

print(df["Salary"].min())

print("---- max salary ----")

print(df["Salary"].max())

print("---- average salary ----")

print(df["Salary"].mean())

print("--- show city wise total salary ---")

city_wise_total_sal = df.groupby(["City"])["Salary"].sum()

print(city_wise_total_sal)

print("--- show city wise gender wise total salary ---")

city_wise_gender_wise_total_sal = df.groupby(["City","Gender"])["Salary"].sum()

print(city_wise_gender_wise_total_sal)