
list_var = [40,20,60,1,90]

min = list_var[0]

for i in range(1,len(list_var)):
    if min > list_var[i]:
        min = list_var[i]

print("min value:",min)