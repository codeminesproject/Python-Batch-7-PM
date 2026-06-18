

for num in range(1,101):
    if num==1:
        continue
    elif num==2:
        print(num)
    elif num%2==0:
        continue
    else:
        mid = num//2
        end = mid + 1

        isPrime = 0

        for i in range(3,end):
            if num%i==0:
                isPrime = 1
                break
        
        if isPrime==0:
            print(num)


    
        