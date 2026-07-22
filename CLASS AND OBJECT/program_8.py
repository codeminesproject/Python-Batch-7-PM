
class Institute:

    name = ""

    def __init__(self,user_name):
        self.name = user_name

    def details(self):
        print("value of variable name is ",self.name)

obj = Institute("CodeMines")
obj.details()

print("--------------------------------------------")

obj = Institute("Santtosh")
obj.details()

print("--------------------------------------------")

obj = Institute("Python Full Stack")
obj.details()