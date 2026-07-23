class GrandParent:
    def grandParentFunction(self):
        print("GrandParent - Grand Parent Function")

class Parent1(GrandParent):
    def parent1Function(self):
        print("Parent1 - Parent1 Function")

class Parent2(GrandParent):
    def parent2Function(self):
        print("Parent2 - Parent2 Function")

class Child(Parent1,Parent2):
    def childFunction(self):
        print("Child - Child Function")

objChild = Child()

objChild.grandParentFunction()
objChild.parent1Function()
objChild.parent2Function()
objChild.childFunction()