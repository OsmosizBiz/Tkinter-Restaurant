def mainMenu():
    global order
    global total

    f=open("menuList.txt", "r")

    menu = f.read()

    menuItems = menu.split("\n")

    for i in range(len(menuItems)):

        item = menuItems[i].split("-")
        
        name = item[0]
        
        price = (float(item[1]) - 0.01)
        
        menu = ("({}) {} - £{}".format(i + 1, name, price))

        lbl = Label(window , text = menu , bg = "gray80", fg ="white")
        lbl.pack(side = LEFT)

        btn = Button(window, text = "add", bg = "white")
        btn.pack(side = RIGHT)

    
    label = Label(window, text = "\nPlease select the number of the item you want", bg = "gray80", )
    label.pack()

    ent = Entry(window)
    ent.pack()
    

    btn = Button(window, text = "Enter")
    btn.pack()

    item = menuItems[ent - 1].split("-")

    choice = ("\n{} has been added to the order".format(item[0]))

    label = Label(window , text = choice, bg = "gray80")
    label.pack()
    

    order.append(item[0])

    total += float(item[1])



#this imports the tkinter functions
from tkinter import *
import sys
#####from MenuCode import mainMenu as Main

# a window is created using Tk from tkinter
window = Tk()

#here we are giving the window a title
window.title("Menu Login")


#this sets the original size for the window
window.geometry("400x420")

#this adds an icon to the window
window.wm_iconbitmap("favicon.ico")

window.configure(background = "gray80")
#create a label called 'lbl'
photo = PhotoImage(file = "picture1.png")
lbl = Label(window , text = "Osmani's Ristorante" , bg = "gray80" , fg = "magenta")
lbl.pack()

#menu functions 
def ViewOrder():
    print(order)
def NewOrder():
    sys.exit(window)
def About():
    print("This is a simple example of a menu")

#creating a dropdown menu in the corner
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label="Order", menu=filemenu)

filemenu.add_command(label="View Order", command=ViewOrder)
filemenu.add_command(label="New Order", command=NewOrder)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

mainMenu()



window.mainloop()

