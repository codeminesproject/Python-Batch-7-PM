
"""
decorators: decorators are additonal rules which we are applying on class methods

classmethod : It is a decorator used to call class method without object. 
we can directly call class method using class name
In classmethod decorator, methods first parameter by default cls

We can access global property of class
"""

class Institute:

    name = "CodeMines Computer Institute"

    def details(self):
        print("value of name:",self.name)
        print("This is for institute details")

    @classmethod
    def contact(cls):
        print("value of global variable name:",cls.name)
        print("This is for institute contact details")

    @classmethod
    def message(cls):
        print("This is message function")


# call class methods without object of class
Institute.contact()
Institute.message()

