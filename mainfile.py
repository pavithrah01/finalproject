import sys

from admin import *
from user import *

print("Welcome to the Restaurant App")

while True:
    role = int(input("Please select your role \n1.Admin \n 2.User\n 3.Exit"))
    if role ==1:
        res = Admin()
        while True:
            admin_input = int(input('enter your preference'))
            print("press 1 for add item")
            print("press 2 for edit item")
            print("press 3 for remove item")
            print("press 4 for view item")
            if admin_input==1:
                res.add_food_item()
            elif admin_input==2:
                res.edit_food_item()
            elif admin_input==3:
                res.remove_food_item()
            elif admin_input==4:
                res.view_all_food_items()
            elif admin_input==0:
                sys.exit()
            else:
                print("enter valid input")
    if role==2:
        res = User()
        while True:
            admin_input = int(input('enter your preference'))
            print("press 1 for place order")
            print("press 2 for view order history")
            print("press 3 for update profile")
            print("press 4 for register")
            print("press 5 for login")
            if admin_input==1:
                res.place_new_order()
            elif admin_input==2:
                res.view_order_history()
            elif admin_input==3:
                res.update_profile()
            elif admin_input==4:
                res.register()
            elif admin_input==5:
                res.login()
            elif admin_input==0:
                sys.exit()
            else:
                print("enter valid input")

    if role==3:
        print("thank u for visiting")
        sys.exit()
