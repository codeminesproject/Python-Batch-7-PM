class GrandParent:
    def grandParentFunction(self):
        print("GrandParent - Grand Parent Function")

class Parent(GrandParent):
    def parentFunction(self):
        print("Parent - Parent Function")

class Child(Parent):
    def childFunction(self):
        print("Child - Child Function")

objChild = Child()
objChild.childFunction()
objChild.grandParentFunction()
objChild.parentFunction()
