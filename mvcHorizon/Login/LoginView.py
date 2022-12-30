from tkinter import *
from tkinter import ttk

class LoginView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #declaring variable
        self.message = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        
        #Creating layout of login form
        Label(self,width="300", text="Login From", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
        #Username Label
        Label(self, text="Username * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
        #Username textbox
        self.usernameField = Entry(self, textvariable=self.username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=40)
        #Password Label
        Label(self, text="Password * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
        #Password textbox
        self.passwordField = Entry(self, textvariable=self.password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=80)
        #Label for displaying login status[success/failed]
        self.messageLabel = ttk.Label(self, text='',font=("Arial",12,"bold"))
        self.messageLabel.place(x=95,y=120)
        #Login button
        Button(self, text="Login", width=10, height=1, command=self.login_clicked, bg="#0E6655",font=("Arial",12,"bold")).place(x=125,y=170)

        #set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def login_clicked(self):
        if self.controller:
            self.controller.login(self.username.get(), self.password.get())

    def show_error(self, message):
        self.messageLabel['text'] = message
        