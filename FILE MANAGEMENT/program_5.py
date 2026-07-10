
# read content from textfile

with open("C:\\CodeMines\\files\\myfile.txt","r") as file:
    print(file.read())

print("-------------------------------------------------------------")

# show only first line:

with open("C:\\CodeMines\\files\\myfile.txt","r") as file:
    print(file.readline())

print("-------------------------------------------------------------")

# show all lines in list:

with open("C:\\CodeMines\\files\\myfile.txt","r") as file:
    print(file.readlines())
