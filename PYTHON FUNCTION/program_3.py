
"""
Variable type: Global Variable & Local Variable

Local Variable: Local variable are those declared inside function and can be accessible inside function only
Global Variable: Global variable are those declared at program level and can be accessible inside whole program
"""
institute_name = "CodeMines Computer Institute"

def displayMessage():
    message = "Welcome to CodeMines Computer"
    print(message)
    print("displayMessage() - value of variable institute_name:",institute_name)

def greet():
    name = "Santtosh Upadhyay"
    print("Welcome",name)
    print("greet() - Age:",age)

displayMessage()
print("value of variable institute_name:",institute_name)

age = 20

greet()


print("value of variable name age:",age)