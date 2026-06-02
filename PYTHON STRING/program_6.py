
description = "     CodeMines     Computer  Institute               "

print("value of description:",description)
print("no of character in description:",len(description))

print("----------- remove all additional space from description ---------")

description_without_space = description.strip()

print("value of description_without_space:",description_without_space)
print("no of character in description_without_space:",len(description_without_space))

print("----------- remove left additional space from description ---------")

description_without_left_space = description.lstrip()

print("value of description_without_left_space:",description_without_left_space)
print("no of character in description_without_left_space:",len(description_without_left_space))

print("----------- remove right additional space from description ---------")

description_without_right_space = description.rstrip()

print("value of description_without_right_space:",description_without_right_space)
print("no of character in description_without_right_space:",len(description_without_right_space))

