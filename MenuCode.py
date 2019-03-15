global order
global total


def mainMenu():
    global order
    global total

    f=open("menuList.txt", "r")

    menu = f.read()

    menuItems = menu.split("\n")

    for i in range(len(menuItems)):

        item = menuItems[i].split("-")
        
        name = item[0]
        
        price = round(float(item[1]),2)
        
        print("({}) {} - £{}".format(i + 1, name, price))

    print("\nPlease select the number of the item you want ")

    menuChoice = int(input(""))

    item = menuItems[menuChoice - 1].split("-")

    print("\n{} has been added to the order".format(item[0]))

    order.append(item[0])

    total += float(item[1])

    
finished = False

order = []

total = 0

while not finished:
    print("""Please select the corresponding number.

1.Main course
2.Desserts
3.Drinks
4.login
5.Order list
""")

    mainChoice = int(input(""))

    if mainChoice == 1:

        mainMenu()

    elif mainChoice == 2:
        print("")

    elif mainChoice == 3:
        print("")

    elif mainChoice == 4:
        print("")

    elif mainChoice == 5:
        item = [order]
        for items in item:
            print(items)
            print("The total is £",total)
            print("""Are you finished with your order?
    1.Yes
    2.No""")
            orderchoice=int(input("?"))
            
        if orderchoice == 1:

            finished = True
            
        if orderchoice == 2:
            
            print("OK please complete your order.")
            
            item = [order]
            
        for items in item:
            
            print(items)
            
            print("The final total is £",total)
            
    else:
        print("invalid command")





    
    

