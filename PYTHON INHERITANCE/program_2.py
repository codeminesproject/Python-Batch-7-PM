

class Parent:
    def parentFunction(self):
        print("Parent - Parent Function")

    def message(self):
        print("Parent - Welcome to CodeMines Computer")

class Child(Parent):
    def childFunction(self):
        print("Child - Child Function")

    def message(self):
        print("Child - Welcome Child")

objChild = Child()
objChild.message()

objParent = Parent()
objParent.message()