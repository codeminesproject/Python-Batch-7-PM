"""
Encapsulation: It is used to define rules of property access

Type of Access:
Public - We can access public property of class using object of class
private - When we want to restric property of class to be called using object

private property declared using double underscore __
"""


class Institute:

    __account_number = 1234567890

    def general_details(self):
        print("Name: CodeMines Computer Institute")
        print("Mobile: 9167519953")
    
    def __account_details(self):
        print("Account Number: 123XXXXXXXXXX89")
        print("Username: xxxxxxxxxxxxx")
        print("Password: xxxxxxxxxxxxx")
    
obj = Institute()
obj.general_details()
#obj.__account_details()

print(obj.__account_number)
