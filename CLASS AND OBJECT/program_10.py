
class Arithmatic:

    num_1:int
    num_2:int
    num_3:float
    name:str

    def __init__(self,a=0,b=0,c=0,d="Guest"):
        self.num_1=a
        self.num_2=b
        self.num_3=c
        self.name=d

    def display(self):
        print("value of num 1:",self.num_1)
        print("value of num 2:",self.num_2)
        print("value of num 3:",self.num_3)
        print("value of name:",self.name)

obj = Arithmatic("test","tes1","asas",4)
obj_1 = Arithmatic()
