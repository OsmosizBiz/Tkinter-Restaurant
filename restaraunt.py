import time
import sys
total=0
n=0
order=[]
print("Welcome to Good Food, this is the menu.\n")
while n != 1:
    print("""Please select the corresponding number.
1.Main course
2.Desserts
3.Drinks
4.login
5.Order list
""")
    menuchoice=int(input(""))
    if menuchoice == 1:
        f=open("main_menu.txt")
        print(f.read())
        main=int(input(""))
        if main == 1:
            order.append("chips and sausage")
        elif main == 2:
            order.append("Large Chips")
        elif main == 3:
            order.append("Chips & Cheese")
        elif main == 4:
            order.append("Large Chips & Gravy")
        elif main == 5:
            order.append("4 oz Cheese Burger with cheese and bacon")
        elif main == 6:
            order.append("6 oz Cheese Burger")
        else:
            print("not valid")
        total=total+5
    elif menuchoice == 2:        
        f=open("desserts.txt")
        print(f.read())
        main=int(input(""))
        if main == 1:
            order.append("Ice cream and Strawberries")
        elif main == 2:
            order.append("Profiteroles")
        elif main == 3:
            order.append("Waffles and Chocolate")
        elif main == 4:
            order.append("Fudge Cake")
        elif main == 5:
            order.append("Cheese Cake")
        elif main == 6:
            order.append("Strawbeery Sundae")
        else:
            print("not valid")
        total=total+3.5
    elif menuchoice == 3:        
        f=open("drinks.txt")
        print(f.read())
        main=int(input("?"))
        if main == 1:
            order.append("Coca Cola")
        elif main == 2:
            order.append("Tango")
        elif main == 3:
            order.append("Pepsi")
        elif main == 4:
            order.append("Tea")
        elif main == 5:
            order.append("Milkshake")
        elif main == 6:
            order.append("Coffee")
        else:
            print("not valid")
        total=total+1.5
    elif menuchoice == 4:        
        f=open("login.txt")
        print(f.read())
        main=int(input(""))    
    elif menuchoice == 5:
        item = [order]
        for items in item:
            print(items)
            print("The total is £",total)
            print("""Are you finished with your order?
    1.Yes
    2.No""")
        orderchoice=int(input("?"))
        if orderchoice == 1:
            n=n+1
        if orderchoice == 2:
            print("OK please complete your order.")
    else:
        print("invlaid number")
        
item = [order]
for items in item:
    print(items)
    print("The final total is £",total)
