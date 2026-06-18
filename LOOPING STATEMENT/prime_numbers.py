

num = 13

if num%2==0:
    print("Not a prime")
else:
    mid = num//2
    end = mid + 1

    isPrime = 0

    for i in range(3,end):
        if num%i==0:
            isPrime = 1
            break
    
    if isPrime==0:
        print("num is prime")
    else:
        print("num is not a prime")
        