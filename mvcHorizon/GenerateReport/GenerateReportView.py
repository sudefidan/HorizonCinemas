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
        self.listingsBooking = Frame(self.notebook, width=740, height=280)
        self.listingsBooking.pack(fill='both', expand=True)
        self.notebook.add(self.listingsBooking, text='Number of bookings\nfor each listing')

        columns = ('date', 'time', 'screenid','filmid','bookings')
        self.reportTickettree = ttk.Treeview(self.listingsBooking, columns=columns, show='headings')
        self.reportTickettree.pack()
        self.reportTickettree.heading('date', text='Date')
        self.reportTickettree.heading('time', text='Time')
        self.reportTickettree.heading('screenid', text='Screen')
        self.reportTickettree.heading('filmid', text='Film')
        self.reportTickettree.heading('bookings', text='Number of Bookings')
        self.button = Button(self.listingsBooking, text='data',command=lambda: self.displayTicketShowReport(), width=12).pack()
    
    """Fiorella Scarpino 21010043"""
    def displayTicketShowReport(self):
        showsreport = []
        showsArrayfromGet = []
        self.reportdataTicketCount = self.controller.get_ticket_show_report()
        showsArrayfromGet.append(self.reportdataTicketCount[0])
        for i in range(0,len(self.reportdataTicketCount)+1):
            showsreport.append(showsArrayfromGet[0][i])  
        for row in showsreport:
            self.reportTickettree.insert('', END, values=row)


    """Fiorella Scarpino 21010043"""
    def monthly_revenue_view(self):
        #otal monthly revenue for each cinema frame
        self.monthlyRevenue = Frame(self.notebook, width=740, height=280)
        self.monthlyRevenue.pack(fill='both', expand=True)
        self.notebook.add(self.monthlyRevenue, text='Monthly revenue\nfor each cinema')

        columns = ('month','city','location','totalrev')
        self.monthlyCinemaTree = ttk.Treeview(self.monthlyRevenue, columns=columns, show='headings')
        self.monthlyCinemaTree.pack()
        self.monthlyCinemaTree.heading('month', text='Month')
        self.monthlyCinemaTree.heading('city', text='City')
        self.monthlyCinemaTree.heading('location', text='Location')
        self.monthlyCinemaTree.heading('totalrev', text='Total Revenue (£)')
        self.monthlyCinemaButton = Button(self.monthlyRevenue, text='Generate Data',command=lambda: self.displayMonthlyCinema(), width=12).pack()
    
    """Fiorella Scarpino 21010043"""
    def displayMonthlyCinema(self):
        self.monthlyListCinema = self.controller.get_monthly_cinema_report()
        self.monthlyListCinema1 = self.monthlyListCinema.to_numpy().tolist()
        for row in self.monthlyListCinema1:
            self.monthlyCinemaTree.insert('', END, values=row)

    """Cameron Povey 21011010"""
    def top_film_view(self):
        #top revenue generating film frame
        self.topFilm = Frame(self.notebook, width=740, height=280)
        self.topFilm.pack(fill='both', expand=True)
        self.notebook.add(self.topFilm, text='Top revenue\ngenerating film')
        
        columns = ('Film Id', 'Film Name', 'Revenue')
        self.topFilmTree = ttk.Treeview(self.topFilm, columns=columns, show='headings')
        self.topFilmTree.pack()
        for col in (columns):
            self.topFilmTree.heading(str(col), text=str(col), command=lambda: \
                 self.treeview_sort_column(self.topFilmTree, col, False))
            
        Button(self.topFilm, text='Generate Data',command=lambda: self.getTopFilms(), pady=5).pack(fill=X)
    
    """Cameron Povey 21011010"""
    def getTopFilms(self):
        #self.topFilmTree.delete('', END, None)
        topFilmList = (self.controller.getTopFilms())
        print(topFilmList)
        for row in topFilmList:
            self.topFilmTree.insert('', END, values=row)

    """Cameron Povey 21011010"""
    def staffs_booking_view(self):
        #monthly list of staff making number of bookings in sorted order frame
        self.staffsBooking = Frame(self.notebook, width=740, height=280)
        self.staffsBooking.pack(fill='both', expand=True)
        self.notebook.add(self.staffsBooking, text='Monthly list of staff\nmaking number of bookings')
        
        columns = ('Staff Id', 'Role', 'Cinema', 'First Name', 'Last Name', 'Bookings')
        self.topStaffTree = ttk.Treeview(self.staffsBooking, columns=columns, show='headings')
        self.topStaffTree.pack()
        for col in (columns):
            self.topStaffTree.heading(str(col), text=str(col), command=lambda: \
                 self.treeview_sort_column(self.topStaffTree, col, False))
            
        Button(self.staffsBooking, text='Generate Data',command=lambda: self.getTopStaff(), pady=5).pack(fill=X)
    
    """Cameron Povey 21011010"""
    def getTopStaff(self):
        topStaff = (self.controller.getTopStaff())
        print(topStaff)
        for row in topStaff:
            self.topStaffTree.insert('', END, values=row)
            
    def treeview_sort_column(self, tree, column, reverse):
        l = [(tree.set(i, column), i) for i in tree.get_children('')]
        l.sort(reverse=reverse)
        
        for index, (val, i) in enumerate(l):
            tree.move(i, '', index)

        tree.heading(column, command=lambda: \
                self.treeview_sort_column(tree, column, not reverse))
            

    """Sude Fidan 21068639"""
    def set_controller(self, controller):
        self.controller = controller
    