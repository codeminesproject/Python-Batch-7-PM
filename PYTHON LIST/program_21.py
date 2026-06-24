
list_var = [40,20,60,1,90]

max = list_var[0]

for i in range(1,len(list_var)):
    if max < list_var[i]:
        max = list_var[i]

print("max value:",max)