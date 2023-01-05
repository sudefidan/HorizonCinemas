from ManageScreening.ManageScreeningModel import ManageScreeningModel
from Entities.User import User

class ManageScreeningController:
    def __init__(self, application, model, view):
        self.application = application
        self.model = model
        self.view = view
        """
    def add_film(self):
        return self.model.add_film()
    def remove_film(self, filmName):
        return self.model.remove_film(filmName)"""

