
import threading
import time

def displayTable():
    num = 10
    for i in range(1,11):
        result = num * i
        print(f"{num} x {i} = {result}")

def displayEvenNumbers():
    num = 50
    for i in range(1,num+1):
        if i%2==0:
            print("Even Number:",i)
        if i==10:
            print("sleep start...")
            time.sleep(10)
            print("sleep completed...")

task_1 = threading.Thread(target=displayTable)
task_2 = threading.Thread(target=displayEvenNumbers)

task_1.start()
task_2.start()

print("all logic executed waiting for final program end")
time.sleep(5)
print("Main program ends")