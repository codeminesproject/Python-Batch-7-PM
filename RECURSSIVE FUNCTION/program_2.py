
# factorial

def Fibonacci(num):
    if num <= 1:
        return num
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)

result=Fibonacci(25)
print(result)