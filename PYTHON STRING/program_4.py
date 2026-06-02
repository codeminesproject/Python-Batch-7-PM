
description = "welcome to CodeMines Computer"

#o/p: Hello, Welcome to CodeMines Computer

print("description in title case:",description.title())

# current o/p: Welcome To Codemines Computer

result = description.title().replace("Welcome","Hello, Welcome").replace("To","to").replace("Codemines","CodeMines")

print(result)