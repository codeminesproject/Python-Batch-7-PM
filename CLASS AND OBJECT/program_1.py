"""
class - It is a collection of properties i.e methods and attributes

function declared inside class is called methods
variable declared inside class is called attributes

Syntax for class:

class class_name:
    // body of class

object is used to exposed property of class

Syntax for object:

object_name = class_name()

self is a parameteris used when we want to call methods of class using object

We can create numbers of object of classes as per user

""" 

class institute:
    def display(self):
        print("Welcome To CodeMines Computer")

# create object for institute
obj = institute()
obj.display()

obj1=institute()
obj1.display()

obj2=institute()
obj2.display()



