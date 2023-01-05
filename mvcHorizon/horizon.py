from tkinter import *
import sqlite3

from Entities.Role import Role
from Login.LoginModel import LoginModel
from Login.LoginView import LoginView
from Login.LoginController import LoginController
from Homepage.HomepageModel import HomepageModel
from Homepage.HomepageView import HomepageView
from Homepage.HomepageController import HomepageController

class App(Tk):
    def __init__(self):
        super().__init__()
        self.role()
        self.user = None

        self.title("Horizon Cinemas")
        self["bg"]="#1C2833"

        self.navigate_to_login()

    def navigate_to_login(self):
        #create a model
        self.model = LoginModel()

        #create a view and place it on the root window
        self.view = LoginView(self)
        self.view.pack(expand=True, fill='both')

        #create a controller
        self.controller = LoginController(self, self.model, self.view)

        #set the controller to view
        self.view.set_controller(self.controller)

    def navigate_to_homepage(self):
        #destroy login window
        self.view.destroy()

        #create a model
        self.model = HomepageModel()

        #create a view and place it on the root window
        self.view = HomepageView(self)
        self.view.pack(expand=True, fill='both')

        #create a controller
        self.controller = HomepageController(self, self.model, self.view)

        #set the controller to view
        self.view.set_controller(self.controller)

        self.view.homepage()

    def logout(self):
        self.user = None
        self.userRole = None

        #destroy homepage window
        self.view.destroy()

        self.navigate_to_login()

    def on_login_success(self):
        #check role with map
        self.userRole = self.roleMap[self.user.roleId]

        self.navigate_to_homepage()

    def role(self):
        #open database
        conn = sqlite3.connect('database/horizoncinemas.db')
        #select query
        cursor = conn.execute('SELECT * from role ')
        #fetch data 
        roles = cursor.fetchall()
        #map data
        self.roleMap = dict()
        for role in roles:
            self.roleMap[role[0]] = Role(role[0], role[1])

    def isAdmin(self):
        return self.userRole!=None and self.userRole.roleName == 'Admin'

    def isManager(self):
        return self.userRole!=None and self.userRole.roleName == 'Manager'
        
    def isBookingStaff(self):
        return self.userRole!=None and self.userRole.roleName == 'BookingStaff'

if __name__ == '__main__':
    app = App()
    app.geometry("1280x720")
    app.mainloop()
