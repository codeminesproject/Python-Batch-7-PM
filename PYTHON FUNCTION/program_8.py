
def addition(a,b,c=0,d=0,e=0):
    add = a + b + c + d + e
    print("Addition:",add)

def greet(name="Guest"):
    print("Welcome",name)

#addition() missing 1 required positional argument: 'c'
addition(10,20)
addition(10,20,30)
addition(10,20,30,40)
addition(10,20,30,40,50)

greet()
greet("Veena")