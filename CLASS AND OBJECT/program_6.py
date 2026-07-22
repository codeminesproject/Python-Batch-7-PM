
"""
decorators: decorators are additonal rules which we are applying on class methods

staticmethod : It is a decorator used to call class method without object. 
we can directly call class method using class name

We can not access global property of class

"""

class Institute:

    name = "CodeMines Computer"

    def details(self):
        print("This is for institute details")

    @staticmethod
    def contact():
        print("This is for institute contact details")


# call class methods without object of class
Institute.contact()

