"""Sude Fidan 21068639"""
"""Cameron Povey 21011010"""
"""Fiorella Scarpino 21010043"""
from ManageScreening.ManageScreeningModel import ManageScreeningModel
from Entities.User import User

class ManageScreeningController:
    """Sude Fidan 21068639"""  
    def __init__(self, application, model, view):
        self.application = application
        self.model = model
        self.view = view

    """Sude Fidan 21068639""" 
    def commit_add_film(self, name, cast,rating,genre,year, description, duration, age):
        return self.model.commit_add_film(name, cast,rating,genre,year, description, duration, age)

    """Sude Fidan 21068639""" 
    def commit_remove_film(self, name):
        return self.model.commit_remove_film(name)

    """Cameron Povey 21011010"""
    def get_show_times(self, showId):
        return self.model.get_show_times(showId)
    
    """Cameron Povey 21011010"""
    def confirm_change(self, date, hour, min):
        return self.model.confirm_change(date, hour, min)
    
    """Cameron Povey 21011010"""
    def fetch_screen_numbers(self, showId):
        return self.model.fetch_screen_numbers(showId)

    """Cameron Povey 21011010"""
    def commit_change(self, screenId):
        return self.model.commit_change(screenId)

    """Fiorella Scarpino 21010043"""
    def createNewFilm(self):
        return self.model.createNewFilm()

    """Fiorella Scarpino 21010043"""
    def createNewCinema(self):
        return self.model.createNewCinema()

    """Fiorella Scarpino 21010043"""
    def createNewScreen(self,userSelectionNewShows):
        return self.model.createNewScreen(userSelectionNewShows)

    """Fiorella Scarpino 21010043"""
    def addDataForNewShow(self,newDateForShow,newTimeShow,screenUserShow,userSelectionNewShowsName):
        return self.model.addDataForNewShow(newDateForShow,newTimeShow,screenUserShow,userSelectionNewShowsName)


