"""Sude Fidan 21068639"""
from tkinter import *
from tkinter import ttk

class LoginView(Frame):
    """Sude Fidan 21068639"""  
    def __init__(self, parent):
        super().__init__(parent)
        #create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        #declaring variable
        self.message = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        #create frame and add it to notebook
        self.frame1 = Frame(self.notebook, width=800, height=50)
        self.frame1.pack(fill='both', expand=True)
        self.notebook.add(self.frame1, text='Login Form')

        #Creating layout
        #Login Form
        Label(self.frame1, text="Please enter login details",bg="#0E6655", fg="white",font=("Arial",13,"bold"), width=100).pack(side=TOP)
        Label(self.frame1, text="", height=1).pack()
        #Username Label
        Label(self.frame1, text="Username * ",fg="white",font=("Arial",14,"bold")).pack()
        #Username textbox
        self.usernameField = Entry(self.frame1, textvariable=self.username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        Label(self.frame1, text="", height=1).pack()
        #Password Label
        Label(self.frame1, text="Password * ",fg="white",font=("Arial",14,"bold")).pack()
        #Password textbox
        self.passwordField = Entry(self.frame1, textvariable=self.password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        Label(self.frame1, text="", height=2).pack()
        #Label for displaying login status[success/failed]
        self.messageLabel = ttk.Label(self.frame1, text='',font=("Arial",12,"bold"))
        self.messageLabel.place(x=290,y=160)
        #Login button
        Button(self.frame1, text="Login", width=10, height=1, command=self.login_clicked, bg="#0E6655",font=("Arial",12,"bold")).pack()

        #set the controller
        self.controller = None

    """Sude Fidan 21068639"""  
    def set_controller(self, controller):
        self.controller = controller

    """Sude Fidan 21068639"""  
    def login_clicked(self):
        if self.controller:
            self.controller.login(self.username.get(), self.password.get())

    """Sude Fidan 21068639"""  
    def show_error(self, message):
        self.messageLabel['text'] = message
        