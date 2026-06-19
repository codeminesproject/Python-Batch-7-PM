
isContinue = "yes"

while isContinue=="yes":
    num = int(input("Please enter number: "))
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
    isContinue = input("do you want to continue? press yes else press anything..: ")