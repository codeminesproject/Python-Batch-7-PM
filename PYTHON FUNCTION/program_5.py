# Modify global variable value inside function
# global is a keyword which is used to declared global variable

def greet():
    name = "Santtosh Upadhyay"
    print("Welcome",name)
    global age
    age = 30
    print("greet() - Age:",age)

age = 20
print("value of variable name age before greet():",age)

greet()

print("value of variable name age after greet():",age)