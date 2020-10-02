# $ yum install python3-tk (If you are using Linux system, then you can use the given command to avoid no module error)
from tkinter import *
def LoginPage():
    login_screen=Tk()
    login_screen.title("Ultra_Animation")
    login_screen.geometry("400x300")

    
    
    Label(login_screen, text="Enter Login Details").pack()
    Label(login_screen, text="____________________").pack()
    Label(login_screen, text="").pack()   
    Label(login_screen, text="Username").pack()  
    
    username_enter = Entry(login_screen,textvariable="username")
    username_enter.pack()
    
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack() 
    
    password_enter = Entry(login_screen,textvariable="password", show= '*')
    password_enter.pack()
    
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=15, height=1).pack()
    login_screen.mainloop()
LoginPage()
