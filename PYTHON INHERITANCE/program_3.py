
# super() is a class refer to parent of current class

class Parent:
    def parentFunction(self):
        print("Parent - Parent Function")

    def message(self):
        print("Parent - Welcome to CodeMines Computer")

class Child(Parent):
    def childFunction(self):
        super().message()
        print("Child - Child Function")

    def message(self):
        print("Child - Welcome Child")

objChild = Child()
objChild.childFunction()
objChild.parentFunction()
objChild.message()