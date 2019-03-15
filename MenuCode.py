## MADE BY LIAM OSMANI ###
#this is the newer version that is similar all that needs to be added is the menu for desserts etc
#i will be able to do this using the same function possbily having a nested function to decide which menu will be accessed
#this will mean that i will minimise the amount of functions that will be required for the user


#these variables will be used throughout the code so i will therfore declare them as global
global order
global total

#this is the function for the mainmenu that i have made so far, i have used the def function to define the function
def mainMenu():
    global order
    global total
    #this opens the text file so that it can it can be read in to access the menu on it 
    f=open("menuList.txt", "r")
    
    #this reads the data and sets it to the variable menu
    menu = f.read()

    #this takes each item in the menu and divides by each line to give each item in the menu a new element
    menuItems = menu.split("\n")

    #this creates a loop that iterates over the different items in the menu, this means that items can be added to the menu without changing the code
    for i in range(len(menuItems)):

        #this divides the item in the menu into price and item name by splitting by the "-"
        item = menuItems[i].split("-")
        
        #this accesses the zeroth element in the item and sets it to name
        name = item[0]
        
        #this takes the first element in the item and rounds it to 2 decimals places just incase
        price = round(float(item[1]),2)
        
        #this prints out the menu accessed from text file and splits it up to display it more elegantly and so we can use the variables later on
        print("({}) {} - £{}".format(i + 1, name, price))

    #this is displayed from the user 
    print("\nPlease select the number of the item you want ")

    #this takes an input from the user as an integer, to improve this i could add error catcher so they type in a number only
    menuChoice = int(input(""))

    #this takes the item selected by the user by using elements and splits
    item = menuItems[menuChoice - 1].split("-")

    #this displays what item of food has been added to the order
    print("\n{} has been added to the order".format(item[0]))

    #the item is addeed to the list 
    order.append(item[0])

    #the price is added to the users total
    total += float(item[1])

#finished is set to flase at the beggining of the program     
finished = False

#the list is created for the users order 
order = []

#the initial total is also set to 0 , it was important to use global so that data can be changed in the functions also 
total = 0

#this creates a loop that will keep iterating until the user has said that they are finished with their order 
while not finished:
    print("""Please select the corresponding number.
1.Main course
2.Desserts
3.Drinks
4.login
5.Order list
""")

    mainChoice = int(input(""))

    #if the input from the user is equal to 1 the indented code will run
    if mainChoice == 1:

        #this calls the function previously defined in the code 
        mainMenu()

    elif mainChoice == 2:
        print("")

    elif mainChoice == 3:
        print("")

    elif mainChoice == 4:
        print("")

    #if the choice is 5 the final order screen will be shown
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

            #this will end the loop above as finished will now be set to true, therefore the program will end
            finished = True
            
        if orderchoice == 2:
            
            print("OK please complete your order.")
            
            item = [order]
            
        for items in item:
            
            print(items)
            
            print("The final total is £",total)
            
    else:
        print("invalid command")





    
    

