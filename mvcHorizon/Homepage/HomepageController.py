"""Sude Fidan 21068639"""
from Homepage.HomepageModel import HomepageModel
from Entities.User import User

class HomepageController:
    def __init__(self, application, model, view):
        self.application = application
        self.model = model
        self.view = view

        #Priviliges
        self.showOtherBooking = application.isAdmin()
        self.showManageScreening = application.isAdmin() or application.isManager()
        self.showGenerateReport = application.isAdmin() or application.isManager()
        self.showAddCinema = application.isManager()
        self.userDetail = self.application.user

    def logout(self):
        self.application.logout()

    def get_user(self):
        return str(self.application.user.location+"\n"+self.application.user.name + " " + self.application.user.surname +" [" + self.application.userRole.roleName+"] ")
    
    def get_films(self):
        return self.model.get_films()
    
    def get_film_dict(self, records,film):
        return self.model.get_film_dict(records,film)
    
    def show_selection(self,value):
        return self.model.show_selection(value)
    





