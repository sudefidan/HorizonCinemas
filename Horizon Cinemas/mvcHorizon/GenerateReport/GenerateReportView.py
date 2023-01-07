"""Sude Fidan 21068639"""
"""Fiorella Scarpino 21010043"""
"""Cameron Povey 21011010"""
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry

class GenerateReportView(Frame):
    """Sude Fidan 21068639"""
    def __init__(self, parent):

        super().__init__(parent)

        #create nested notebook
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(pady=10, expand=True)   
    
    """Sude Fidan 21068639"""
    def generate_report(self):
        self.listings_booking_view()
        self.monthly_revenue_view()
        self.top_film_view()
        self.staffs_booking_view()

    """Fiorella Scarpino 21010043"""
    def listings_booking_view(self):
        #number of bookings for each listing frame
        listingsBooking = Frame(self.notebook, width=740, height=280)
        listingsBooking.pack(fill='both', expand=True)
        self.notebook.add(listingsBooking, text='Number of bookings\nfor each listing')

        columns = ('date', 'time', 'screenid','filmid','bookings')
        self.reportTicketTree = ttk.Treeview(listingsBooking, columns=columns, show='headings')
        self.reportTicketTree.pack()
        self.reportTicketTree.heading('date', text='Date')
        self.reportTicketTree.heading('time', text='Time')
        self.reportTicketTree.heading('screenid', text='Screen')
        self.reportTicketTree.heading('filmid', text='Film')
        self.reportTicketTree.heading('bookings', text='Number of Bookings')
        Button(listingsBooking, text='data',command=lambda: self.display_ticket_show_report(), width=12).pack()
    
    """Fiorella Scarpino 21010043"""
    def display_ticket_show_report(self):
        showsrReport = []
        showsArrayfromGet = []
        reportdataTicketCount = self.controller.get_ticket_show_report()
        showsArrayfromGet.append(reportdataTicketCount[0])
        for i in range(0,len(reportdataTicketCount)+1):
            showsrReport.append(showsArrayfromGet[0][i])  
        for row in showsrReport:
            self.reportTicketTree.insert('', END, values=row)

    """Fiorella Scarpino 21010043"""
    def monthly_revenue_view(self):
        #otal monthly revenue for each cinema frame
        monthlyRevenue = Frame(self.notebook, width=740, height=280)
        monthlyRevenue.pack(fill='both', expand=True)
        self.notebook.add(monthlyRevenue, text='Monthly revenue\nfor each cinema')

        columns = ('month','city','location','totalrev')
        self.monthlyCinemaTree = ttk.Treeview(monthlyRevenue, columns=columns, show='headings')
        self.monthlyCinemaTree.pack()
        self.monthlyCinemaTree.heading('month', text='Month')
        self.monthlyCinemaTree.heading('city', text='City')
        self.monthlyCinemaTree.heading('location', text='Location')
        self.monthlyCinemaTree.heading('totalrev', text='Total Revenue (£)')
        Button(monthlyRevenue, text='Generate Data',command=lambda: self.display_monthly_cinema(), width=12).pack()
    
    """Fiorella Scarpino 21010043"""
    def display_monthly_cinema(self):
        self.monthlyListCinema = self.controller.get_monthly_cinema_report()
        self.monthlyListCinema1 = self.monthlyListCinema.to_numpy().tolist()
        for row in self.monthlyListCinema1:
            self.monthlyCinemaTree.insert('', END, values=row)

    """Fiorella Scarpino 21010043"""
    def top_film_view(self):
        #top revenue generating film frame
        topFilm = Frame(self.notebook, width=740, height=280)
        topFilm.pack(fill='both', expand=True)
        self.notebook.add(topFilm, text='Top revenue\ngenerating film')
        columns = ('filmid','name','totalrevfilm')
        self.topRevTree = ttk.Treeview(topFilm, columns=columns, show='headings')
        self.topRevTree.pack()
        self.topRevTree.heading('filmid', text='Film ID')
        self.topRevTree.heading('name', text='Name')
        self.topRevTree.heading('totalrevfilm', text='Total Revenue (£)')
        Button(topFilm, text='Generate Data',command=lambda: self.display_top_rev(), width=12).pack()
    
    """Fiorella Scarpino 21010043"""
    def display_top_rev(self):
        self.topRev = self.controller.get_top_rev_report()
        topRevCinema = self.topRev.to_numpy().tolist()
        for row in topRevCinema:
            self.topRevTree.insert('', END, values=row)

    """Cameron Povey 21011010"""
    def staffs_booking_view(self):
        #monthly list of staff making number of bookings in sorted order frame
        self.staffsBooking = Frame(self.notebook, width=740, height=280)
        self.staffsBooking.pack(fill='both', expand=True)
        self.notebook.add(self.staffsBooking, text='Monthly list of staff\nmaking number of bookings')

    """Sude Fidan 21068639"""
    def set_controller(self, controller):
        self.controller = controller
    