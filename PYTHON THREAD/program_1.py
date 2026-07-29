
"""
Thread is a unit of independent program

Life Cycle of Thread:
1. Thread Create
2. run thread
"""

import threading


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

task_1 = threading.Thread(target=displayTable)
task_2 = threading.Thread(target=displayEvenNumbers)

task_1.start()
task_2.start()