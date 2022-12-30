from Login.LoginModel import LoginModel
from Entities.User import User

class LoginController:
    def __init__(self, application, model, view):
        self.application = application
        self.model = model
        self.view = view

    def login(self, username, password):
        try:
            self.application.user  = self.model.login(username, password)
            self.application.on_login_success()
        except ValueError as error:
            #show an error message
            self.view.show_error(error)   