
"""
Constructor: It is a special function which automatically called when object of class created

syntax for constructor:


def __init__(self):
    // logic

Type of constructor:
1. Zero Parameterised
2. Parameterised

"""

class Institute:

    name = ""

    def __init__(self):
        self.name = "CodeMines Computer"
        print("Welcome to CodeMines Computer")

    def details(self):
        print("value of variable name is:",self.name)


obj = Institute()
obj.details()