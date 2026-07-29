
import threading

class Thread1(threading.Thread):
    def run(self):
        num = 10
        for i in range(1,11):
            result = num * i
            print(f"{num} x {i} = {result}")

class Thread2(threading.Thread):
    def run(self):
        num = 50
        for i in range(1,num+1):
            if i%2==0:
                print("Even Number:",i)

task_1 = Thread1()
task_1.start()

task_2 = Thread2()
task_2.start()