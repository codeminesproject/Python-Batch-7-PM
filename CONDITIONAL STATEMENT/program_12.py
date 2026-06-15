

"""
ATM:
1. Enter pin and validate
2. If pin validated, then enter amount. If not validated then show message Invalid Pin
3. Check If amount is multple of 100, If yes check with daily limit If not then show Amount should be multiple of 100
4. Check if amount is less than daily limit, if yes then check balance If not then show You exceeded daily limit
5. Check if amaunt is less than balance, if yes then show Success If not then show Insufficient Balance

"""

balance = 35000
pin = 1234
daily_limit = 10000

user_pin = int(input("Please enter pin: "))

# 1. Enter pin and validate

if user_pin==pin:
    user_amount = int(input("Please enter amount: "))

    # 3. Check If amount is multple of 100, If yes check with daily limit If not then show Amount should be multiple of 100

    if user_amount%100 == 0:
        # 4. Check if amount is less than daily limit, if yes then check balance If not then show You exceeded daily limit
        if user_amount < daily_limit:
            # 5. Check if amaunt is less than balance, if yes then show Success If not then show Insufficient Balance
            if user_amount < balance:
                print("Success")
            else:
                print("Insufficient Balance")
        else:
            print("You exceeded daily limit")

    else:
        print("Amount should be multiple of 100")


else:
    print("Invalid Pin")