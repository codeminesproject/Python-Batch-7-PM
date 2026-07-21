
class Institute:

    name = "CodeMines Computer Institute"

    def display_1(self):
        print("value of name:",self.name)
        print("This is display_1")
        self.details()
    
    def addition(self,num_1,num_2):
        add = num_1 + num_2
        print("Addition:",add)
    
    def details(self):
        user_name = "test"
        print("This is details function")

obj = Institute()

obj.display_1()
obj.addition(20,30)

print(obj.name)

print(obj.user_name) 