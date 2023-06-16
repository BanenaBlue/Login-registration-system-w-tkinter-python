
#setup
from tkinter import *
import tkinter.messagebox

root = Tk()
root.resizable(True, False)
root.title("Login system")
root.geometry("700x300")
#defining functions
def login():
    #deleting the previous widgets
    label_w_nothing.destroy()
    login_button.destroy()
    register_button.destroy()
    #declaring the next widgets
    empty_label = Label(root, padx = 90, pady = 36) 
    namelabel = Label(root, text="username")
    namefield = Entry(root, width=50)
    passwordlabel = Label(root, text="password")
    passwordfield = Entry(root, width=50)
    #putting the next widgets on the screen
    empty_label.grid(row = 0, column = 0)
    namelabel.grid(row = 1, column = 1)
    namefield.grid(row = 2, column = 1)
    passwordlabel.grid(row = 3, column = 1)
    passwordfield.grid(row = 4, column = 1)

    def login_button_pressed():
        namefield_text = namefield.get()
        passwordfield_text = passwordfield.get()
        with open("usernames_and_passwords_store", "r") as t:
            data = list(t.read().split(" : "))
            for i in range(0, len(data), 2):
                if namefield_text == data[i]:
                    if passwordfield_text == data[int(data.index(data[i]) + 1)]:
                        namelabel.destroy()
                        namefield.destroy()
                        passwordlabel.destroy()
                        passwordfield.destroy()
                        confirm_login_button.destroy()
                        you_logged_in_succesfully = Label(root, text = "You logged in succesfully", padx = 40, pady = 15)
                        you_logged_in_succesfully.grid(row = 1, column = 1)
                    elif passwordfield_text != data.index(i) + 1 and passwordfield_text not in data:                        
                        continue
                    if passwordfield_text not in data:
                        tkinter.messagebox.showinfo(title = "Error", message = "The password isn't correct, please retry")
                elif namefield_text != data[i]:
                    continue
                if namefield_text not in data:
                    tkinter.messagebox.showinfo(title = "Error", message = "This username does not exist. Please register first or retry.")
            t.close()
        return

    confirm_login_button = Button(root, text = "login", padx = 30, pady = 10, command = login_button_pressed)
    confirm_login_button.grid(row = 5, column = 1)
    return

def register():
    #deleting the previous widgets
    label_w_nothing.destroy()
    login_button.destroy()
    register_button.destroy()
    #declaring the next widgets
    empty_label2 = Label(root, padx = 95, pady = 26) 
    namelabel_register = Label(root, text="username")
    namefield_register = Entry(root, width=50)
    passwordlabel_register = Label(root, text="password")
    passwordfield_register = Entry(root, width=50)
    confirmthepassword = Label(root, text="Please confirm your password")
    passwordconfirm_register = Entry(root, width=50)
    #putting the next widgets on the screen
    empty_label2.grid(row = 0, column = 0)
    namelabel_register.grid(row = 1, column = 1)
    namefield_register.grid(row = 2, column = 1)
    passwordlabel_register.grid(row = 3, column = 1)
    passwordfield_register.grid(row = 4, column = 1)
    confirmthepassword.grid(row = 5, column = 1)
    passwordconfirm_register.grid(row = 6, column = 1)

    def go_ahead():
        finished = False
        while finished == False: 
            passwordconfirm_register_text = passwordconfirm_register.get()
            passwordfield_register_text = passwordfield_register.get()
            namefield_register_text = namefield_register.get()             
            if passwordconfirm_register_text == passwordfield_register_text:    
                with open("usernames_and_passwords_store", "r") as f:
                    elements = list(f.read().split(" : "))
                    for i in range(0, len(elements), 2):
                        if elements[i] == namefield_register.get():
                            tkinter.messagebox.showinfo(title = "Error", message = "This username is already taken. Please try with another one.")
                            continue
                        else:
                            continue  
                        f.close()              
                with open("usernames_and_passwords_store", "a") as o:
                    o.write(namefield_register_text + " : " + passwordfield_register_text + " : ")
                    o.close()
                namelabel_register.destroy()
                namefield_register.destroy()
                passwordlabel_register.destroy()
                passwordfield_register.destroy()
                confirmthepassword.destroy()
                passwordconfirm_register.destroy()
                continue_button.destroy()
                registered_succesfully = Label(root, text = "You registered succesfully!", padx = 40, pady = 80)
                registered_succesfully.grid(row = 1, column = 1)
                finished == True
            else:
                tkinter.messagebox.showinfo(title = "Error", message = "The passwords do not match. Please try again.")
                continue
    continue_button = Button(root, text = "continue", command = go_ahead)
    continue_button.grid(row = 7, column = 1)
    return

label_w_nothing = Label(root, padx = 110, pady = 42)
login_button = Button(root, text = "login", padx = 40, pady = 20, command = login)
register_button = Button(root, text = "register", padx = 35, pady = 20, command = register)

label_w_nothing.grid(row = 0, column = 0)
login_button.grid(row = 1, column = 1)
register_button.grid(row = 1, column = 2)

root.mainloop()  
