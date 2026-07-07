# can we declare global variable inside a function and can we access in whole program?

def greet():
    name = "Santtosh Upadhyay"
    print("Welcome",name)
    global age
    age = 30
    print("greet() - Age:",age)



greet()
print("value of variable name age after greet():",age)

