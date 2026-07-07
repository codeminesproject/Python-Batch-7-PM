# can we modify global variable value inside function: No

def greet():
    name = "Santtosh Upadhyay"
    print("Welcome",name)
    age = 30
    print("greet() - Age:",age)

age = 20
print("value of variable name age before greet():",age)

greet()

print("value of variable name age after greet():",age)