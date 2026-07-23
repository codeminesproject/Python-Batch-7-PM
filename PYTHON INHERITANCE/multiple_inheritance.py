
class Parent1:
    def parent1Function(self):
        print("Parent1 - Parent1 Function")

class Parent2:
    def parent2Function(self):
        print("Parent2 - Parent2 Function")

class Child(Parent1,Parent2):
    def childFunction(self):
        print("Child - Child Function")

objChild = Child()

objChild.childFunction()
objChild.parent1Function()
objChild.parent2Function()