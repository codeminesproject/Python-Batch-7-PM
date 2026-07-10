
# create a text file using python

localtion = "C:\\CodeMines\\files\\sample.txt"

# method 1:
# w -> write

# file=open(localtion,"w")
# file_1 = open("C:\\CodeMines\\files\\sample_1.txt","w")

# method 2:

with open(localtion,"w") as file:
    file.write("")

