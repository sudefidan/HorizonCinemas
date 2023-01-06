from Entities.User import User
from GenerateReport.GenerateReportModel import GenerateReportModel

class GenerateReportController:
    def __init__(self, application, model, view):
        self.application = application
        self.model = model
        self.view = view
        
    """Fiorella Scarpino 21010043"""
    def get_ticket_show_report(self):
        return self.model.get_ticket_show_report()

    """Fiorella Scarpino 21010043"""
    def get_monthly_cinema_report(self):
        return self.model.get_monthly_cinema_report()
    
