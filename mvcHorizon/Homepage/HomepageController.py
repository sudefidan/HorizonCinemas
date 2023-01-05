from Homepage.HomepageModel import HomepageModel
from Entities.User import User
from datetime import datetime

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
    
    """Sude Fidan 21068639"""
    def logout(self):
        self.application.logout()

    """Sude Fidan 21068639"""
    def get_user(self):
        return str(self.application.user.location+"\n"+self.application.user.name + " " + self.application.user.surname +" [" + self.application.userRole.roleName+"] ")
    
    """Sude Fidan 21068639"""
    def booking_location(self):
        return self.application.user.location

    """Fiorella Scarpino 21010043"""
    def get_films(self):
        return self.model.get_films()
    
    """Fiorella Scarpino 21010043"""
    def get_film_dict(self, records,film):
        return str(f"Film Name: {records[film][1]}\nCast: {records[film][2]}\nDescription: {records[film][6]}\n\nRating: {records[film][3]}\nGenre: {records[film][4]}\nRelease Year: {records[film][5]}\nDuration: {records[film][7]}\nAge Rating: {records[film][8]}")
    
    """Fiorella Scarpino 21010043"""
    def show_selection(self,value):
        return self.model.show_selection(value)
    
    """Fiorella Scarpino 21010043"""
    def get_new_cinema(self,city,location,seatEntry):
        self.view.clear_text()
        self.model.get_new_cinema(city,location,seatEntry)
    
    
    

    

    


