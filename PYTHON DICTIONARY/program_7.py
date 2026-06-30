
# string datatype as a key
# 1:"Test" we are using 1 number as a key

dict_var = {"id":1,"name":"Veena",1:"Test",101:99,(45,23,65,78):"CodeMines",99:{"1":1,"2":2}}

print("value of id:",dict_var["id"])
print("value of name:",dict_var["name"])
print("value of 1:",dict_var[1])
print("value of key 101:",dict_var[101])
print("value of key tuple:",dict_var[(45,23,65,78)])
print("value of key 99:",dict_var[99])