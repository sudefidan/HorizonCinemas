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
    
    """Cameron Povey 21011010"""
    def get_films_cinema(self):
        return (self.model.get_films_cinema(self.application.user.location))

    """Cameron Povey 21011010"""
    def existed_showing(self,film,date):
        return (self.model.existed_showing(film,date))

    """Cameron Povey 21011010"""
    def update_type(self,time):
        return (self.model.update_type(time))

    """Cameron Povey 21011010"""
    def calculate_cost(self, typesel, amount):
        return (self.model.calculate_cost(typesel, amount))
        
    """Cameron Povey 21011010"""
    def book_film(self, fname, lname, phone, email, card, exp, cvv):
        return self.model.book_film(fname, lname, phone, email, card, exp, cvv, self.application.user.id)
    
    """Cameron Povey 21011010"""
    def get_film_info(self, id):
        return (self.model.get_film_info(id))
    
    """Cameron Povey 21011010"""
    def cancel_cost(self):
        return (self.model.cancel_cost())
    
    def commit_cancel(self):
        return (self.model.commit_cancel())
    
    
    

    

    


