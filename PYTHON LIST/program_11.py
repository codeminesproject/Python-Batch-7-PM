
list_var = [100,200,300,400,500,200,900,1200,200,178,987,456,200]

print("value of list_var:",list_var)
print("total no of values:",len(list_var))


print("position of value 300 in list:",list_var.index(300))
print("position of value 900 in list:",list_var.index(900))
# print("position of value 700 in list:",list_var.index(700))

print("position of value 200 in list:",list_var.index(200))
print("second position of value 200 in list:",list_var.index(200,2))
print("third position of value 200 in list:",list_var.index(200,6))
print("fourth position of value 200 in list:",list_var.index(200,9))