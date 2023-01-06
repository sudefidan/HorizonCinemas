from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox 
import numpy as np
from ManageScreening.ManageScreeningController import ManageScreeningController
from ManageScreening.ManageScreeningModel import ManageScreeningModel
from ManageScreening.ManageScreeningView import ManageScreeningView
from GenerateReport.GenerateReportController import GenerateReportController
from GenerateReport.GenerateReportModel import GenerateReportModel
from GenerateReport.GenerateReportView import GenerateReportView

class HomepageView(Frame):
    """Sude Fidan 21068639"""
    def __init__(self, parent):

        super().__init__(parent)

        #create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)
        
    """Sude Fidan 21068639"""
    def homepage(self):
        #create frames and add frames to notebook
        self.listings_view()
        self.booking_view()
        self.cancellation_view()
        #admin and manager access
        if self.controller.showManageScreening:
            self.manage_view()
        #admin and manager access
        if self.controller.showGenerateReport:
            self.report_view()
        #only manager access
        if self.controller.showAddCinema:
            self.new_cinema_view()
            
        #staff details 
        Label(self, text=self.controller.get_user(), width=30, height=5, fg= '#ffffff',font=("Arial",12,"bold")).place(relx = 1.0, rely = 0.0,anchor="ne")

        #logout button
        Button(self, text="Logout", width=10, height=1, command=self.logout_clicked, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM, anchor="e")

    """Fiorella Scarpino 21010043"""
    def listings_view(self):
        #listing frame
        self.listing = Frame(self.notebook, width=800, height=280)
        self.listing.pack(fill='both', expand=True)
        self.notebook.add(self.listing, text='Listings')
        #self.controller.listings()

        #proceed booking button
        Button(self.listing, text="Proceed Booking", width=10, height=1, command=self.show_make_booking, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM)
        
        #movie scrollbar
        scrollbar = Scrollbar(self.listing, orient="vertical")
        self.movieFrame=Listbox(self.listing,bg = "grey64",selectbackground="grey",activestyle = 'dotbox',yscrollcommand=scrollbar.set)
        self.movieFrame.pack(side=LEFT, fill='both', expand=True, anchor="n")
        scrollbar.config(command=self.movieFrame.yview)

        #insert movie names
        self.records = self.controller.get_films()
        for row in self.records:
            movieName=row[1]
            self.movieFrame.insert('end',movieName)

        #movie info scrollbar
        self.textOutput = Text(self.listing,bg = "grey64",wrap=WORD)   
        self.textOutput.pack(side=TOP, fill='both', expand=True, anchor="e")

        #correlate film selection to data from database        
        self.movieFrame.bind('<<ListboxSelect>>',self.get_selection)

        #show scrollbar
        columns = ('date', 'time', 'screenid')
        self.tree = ttk.Treeview(self.listing, columns=columns, show='headings')
        self.tree.pack(side=RIGHT, fill='both', expand=True, anchor="n")
        self.tree.heading('date', text='Date')
        self.tree.heading('time', text='Time')
        self.tree.heading('screenid', text='Screen')

    """Fiorella Scarpino 21010043"""
    def get_selection(self,event):
        widget = event.widget
        selection=widget.curselection()
        self.value = widget.get(selection[0])
        curselection = self.movieFrame.curselection()[0]
        filmDict = self.controller.get_film_dict(self.records,curselection)
        self.textOutput.delete(1.0,'end')
        for f in filmDict:
            self.textOutput.insert('end',f)
            self.tree.delete(*self.tree.get_children()) #clear tree
            selection = self.controller.show_selection(curselection+1)    
            for row in selection:
                self.tree.insert('', END, values=row)

    """Sude Fidan 21068639"""
    def show_make_booking(self):
        self.notebook.select(tab_id=1)

    """Cameron Povey 21011010"""
    def booking_view(self):
        #booking frame
        self.booking = Frame(self.notebook, width=800, height=280)
        self.booking.pack(fill='both', expand=True)
        self.notebook.add(self.booking, text='Make Booking')
        
    """Cameron Povey 21011010"""
    def cancellation_view(self):
        #cancellation frame    
        self.cancellation = Frame(self.notebook, width=800, height=280)
        self.cancellation.pack(fill='both', expand=True)
        self.notebook.add(self.cancellation, text='Make Cancellation')

        Label(self.cancellation, text="Enter Booking No:", bg="cyan", font=("Arial", 25), fg='Black').pack(fill=X)
        self.cpcanBookNos = Spinbox(self.cancellation, from_=1, to=999999)
        self.cpcanBookNos.pack(expand=True)
        Button(self.cancellation, text="Find Booking info", bg="cyan", padx=2,pady=2, command=lambda: self.get_film_info()).pack()
        
        
        #LIST OF INFO
        self.line1 = Frame(self.cancellation)
        self.line1.pack(fill=X, expand=True)
        self.cpcanBookingId = Label(self.line1, text="ID: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanBookingPrice = Label(self.line1, text="Price: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanBookingHall = Label(self.line1, text="Hall Type: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanBookingStaff = Label(self.line1, text="Staff: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanBookingId.pack(fill=X, side=LEFT, expand=True)
        self.cpcanBookingPrice.pack(fill=X, side=LEFT, expand=True)
        self.cpcanBookingHall.pack(fill=X, side=LEFT, expand=True)
        self.cpcanBookingStaff.pack(fill=X, side=LEFT, expand=True)
        
        self.line2 = Frame(self.cancellation)
        self.line2.pack(fill=X, expand=True)
        self.cpcanCustomerName = Label(self.line2, text="First Name: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanCustomerPhone = Label(self.line2, text="Last Name: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanCustomerPhone = Label(self.line2, text="Phone: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanCustomerEmail = Label(self.line2, text="E-Mail: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanCustomerName.pack(fill=X, side=LEFT, expand=True)
        self.cpcanCustomerPhone.pack(fill=X, side=LEFT, expand=True)
        self.cpcanCustomerPhone.pack(fill=X, side=LEFT, expand=True)
        self.cpcanCustomerEmail.pack(fill=X, side=LEFT, expand=True)
        
        self.line3 = Frame(self.cancellation)
        self.line3.pack(fill=X, expand=True)
        self.cpcanFilmName = Label(self.line3, text="Film: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanFilmGenre = Label(self.line3, text="Genre: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanFilmYear = Label(self.line3, text="Year: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanFilmDuration = Label(self.line3, text="Duration: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcanFilmName.pack(fill=X, side=LEFT, expand=True)
        self.cpcanFilmGenre.pack(fill=X, side=LEFT, expand=True)
        self.cpcanFilmYear.pack(fill=X, side=LEFT, expand=True)
        self.cpcanFilmDuration.pack(fill=X, side=LEFT, expand=True)
        #END OF LIST
        
        self.cancelCostTitle = Label(self.cancellation, text="Cancel Cost: ", font=('Arial', 25) ,pady=10, bg="cyan", fg="black")
        self.cancelCostTitle.pack(fill=X, expand=True)
        
        self.cancelButton =Button(self.cancellation, height=2, padx=25, pady=25, text="Cancel", state=DISABLED)
        self.cancelButton.pack(fill=X, expand=True)

    """Cameron Povey 21011010"""
    def get_film_info(self):
        try: self.cancelMessage.pack_forget()
        except: pass
        self.cpcanFilmInfo = self.controller.get_film_info(self.cpcanBookNos.get())
        if self.cpcanFilmInfo == 0:
            self.cpcan_resetbook()
            return 0
        else:
            self.cpcanBookingId.configure(text="ID: " + str(self.cpcanFilmInfo[0][0]))
            self.cpcanBookingPrice.configure(text="Price: £" + str(self.cpcanFilmInfo[0][1]))
            self.cpcanBookingHall.configure(text="Hall Type: " + str(self.cpcanFilmInfo[0][2]))
            self.cpcanBookingStaff.configure(text="Staff: " + str(self.cpcanFilmInfo[2][0]))
            
            self.cpcanCustomerName.configure(text="First Name: " + str(self.cpcanFilmInfo[1][1]))
            self.cpcanCustomerPhone.configure(text="Last Name: " + str(self.cpcanFilmInfo[1][2]))
            self.cpcanCustomerPhone.configure(text="Phone: " + str(self.cpcanFilmInfo[1][3]))
            self.cpcanCustomerEmail.configure(text="E-Mail: " + str(self.cpcanFilmInfo[1][4]))
            
            self.cpcanFilmName.configure(text="Film: " + str(self.cpcanFilmInfo[3][1]))
            self.cpcanFilmGenre.configure(text="Genre: " + str(self.cpcanFilmInfo[3][4]))
            self.cpcanFilmYear.configure(text="Year: " + str(self.cpcanFilmInfo[3][5]))
            self.cpcanFilmDuration.configure(text="Duration: " + str(self.cpcanFilmInfo[3][7]))
            
            cpcan_cancelcost = self.controller.cancel_cost()
            #cpcan_cancelcost = "DAY_PRIOR" #Placeholder
            if cpcan_cancelcost == "SAME_DAY":
                self.cancelCostTitle.configure(text="CANNOT CANCEL ON DAY OF SHOW")
                self.cancelButton.configure(state=DISABLED, command=None)
                return 0
            elif cpcan_cancelcost == "DAY_PRIOR":
                self.cancelCostTitle.configure(text="Cancel Cost: " + str(self.cpcanFilmInfo[0][1]/2))
                self.cancelButton.configure(state=NORMAL, command=lambda: self.cpcan_cancel())
            else:
                self.cancelCostTitle.configure(text="Cancel Cost: FREE")
                self.cancelButton.configure(state=NORMAL, command=lambda: self.cpcan_cancel())
    
    """Cameron Povey 21011010"""
    def cpcan_cancel(self):
        cancelState = self.controller.commit_cancel()
        if cancelState == 1: self.cancelMessage = Label(self.cancellation, text="Ticket Removed!", font=('Arial', 25) ,pady=10,width=20, bg=None, fg="Green")
        else: self.cancelMessage = Label(self.cancellation, text="ERROR, Contact Admin", font=('Arial', 25) ,pady=10,width=20, bg=None, fg="Red")
        self.cancelMessage.pack()
    
    """Cameron Povey 21011010"""
    def cpcan_resetbook(self):
        self.cpcanBookingId.configure(text="ID: ")
        self.cpcanBookingPrice.configure(text="Price: ")
        self.cpcanBookingHall.configure(text="Hall Type: ")
        self.cpcanBookingStaff.configure(text="Staff: ")
        self.cpcanCustomerName.configure(text="First Name: ")
        self.cpcanCustomerPhone.configure(text="Last Name: ")
        self.cpcanCustomerPhone.configure(text="Phone: ")
        self.cpcanCustomerEmail.configure(text="E-Mail: ")
        self.cpcanFilmName.configure(text="Film: ")
        self.cpcanFilmGenre.configure(text="Genre: ")
        self.cpcanFilmYear.configure(text="Year: ")
        self.cpcanFilmDuration.configure(text="Duration: ") 
        self.cancelCostTitle.configure(text="INVALID BOOKING NUMBER")
        self.cancelButton.configure(state=DISABLED, command=None)
        try: self.cancelMessage.pack_forget()
        except: pass
        
    """Sude Fidan 21068639"""
    def manage_view(self):
        #manage frame
        self.manage = Frame(self.notebook, width=800, height=280)
        self.manage.pack(fill='both', expand=True)
        self.notebook.add(self.manage, text='Manage Screening')

        #create a model
        self.manageModel = ManageScreeningModel()

        #create a view and place it on the root window
        self.manageView = ManageScreeningView(self.manage)
        self.manageView.pack(expand=True, fill='both')

        #create a controller
        self.manageController = ManageScreeningController(self, self.manageModel, self.manageView)

        #set the controller to view
        self.manageView.set_controller(self.manageController)

        self.manageView.manage_screening()

    """Sude Fidan 21068639"""
    def report_view(self):
        #report frame
        self.report = Frame(self.notebook, width=800, height=280)
        self.report.pack(fill='both', expand=True)
        self.notebook.add(self.report, text='Generate Report')

        #create a model
        self.reportModel = GenerateReportModel()

        #create a view and place it on the root window
        self.reportView = GenerateReportView(self.report)
        self.reportView.pack(expand=True, fill='both')

        #create a controller
        self.reportController = GenerateReportController(self, self.reportModel, self.reportView)

        #set the controller to view
        self.reportView.set_controller(self.reportController)

        self.reportView.generate_report()

    """Fiorella Scarpino 21010043"""
    def new_cinema_view(self):
        #new_cinema frame
        self.new_cinema = Frame(self.notebook, width=800, height=280)
        self.new_cinema.pack(fill='both', expand=True)
        self.notebook.add(self.new_cinema, text='Add New Cinema')

        padding = {'ipadx': 10, 'ipady': 10}
        title = Label(self.new_cinema,text="Add New Cinema",font=14).pack(**padding)

        self.cityText = StringVar()
        city_Label = Label(self.new_cinema, text='City', font=12).pack(**padding, fill=X)
        self.city_Entry = Entry(self.new_cinema, textvariable=self.cityText)
        self.city_Entry.pack(**padding, fill=X)

        self.locationText = StringVar()
        location_Label = Label(self.new_cinema, text='Location', font=12).pack(**padding, fill=X)
        self.location_Entry = Entry(self.new_cinema, textvariable=self.locationText)
        self.location_Entry.pack(**padding, fill=X)

        self.screenNumber = IntVar()
        screen_Label = Label(self.new_cinema, text='Number of Screens', font=12).pack(**padding, fill=X)
        self.screen_Entry = Entry(self.new_cinema, textvariable=self.screenNumber)
        self.screen_Entry.pack(**padding, fill=X)

        #to edit the capacity for each screen
        self.getScreenNumber = Button(self.new_cinema, text='Edit Screens',command=lambda: self.getscreensChange(), width=12)
        self.getScreenNumber.pack(**padding)
    
    """Fiorella Scarpino 21010043"""
    def getscreensChange(self):
        #capacity for each screen 
        try:
            self.getScreenNumber['state'] = DISABLED
            self.seatEntryArray = []
            self.screenGet = self.screenNumber.get()

            #number of screens
            self.Screenlist = np.arange(1,self.screenGet+1)
            self.seatingCap_Label = Label(self.new_cinema, text='Seating Capacity', font=12).pack()

            #makes the same amount of labels as screens
            for screens in range(len(self.Screenlist)):
                #label for each screen
                self.screenNumber = Label(self.new_cinema, text=f'Screen {screens+1}', font=12).pack()
                self.screenEntry = Entry(self.new_cinema)
                self.screenEntry.pack()
                self.seatEntryArray.append(self.screenEntry)
            
            self.addCinemaButton = Button(self.new_cinema, text='Add New Cinema',command=lambda: self.add_new_cinema(), width=12).pack()
        except TclError:  #validation for integer
            self.getScreenNumber['state'] = NORMAL
            messagebox.showerror(title = 'Error',message='Please enter an integer')

    """Fiorella Scarpino 21010043"""
    def add_new_cinema(self):
         #get user data for new cinema
        self.cityGet = self.cityText.get()
        self.locationGet = self.locationText.get()
        allValid = True # to validate
        #seat capacities
        self.seatingArray = ''
        for s in self.seatEntryArray:
            self.seatingArray = self.seatingArray + str(s.get()) + '\n'
        self.seatEntry = self.seatEntryArray

        if self.cityGet.isalpha() and self.locationGet.isalpha():
            allValid = True
            for valid in range(len(self.seatEntry)):
                if self.seatEntry[valid].get().isdigit():
                    allValid = True
                else:
                    allValid = False
        else:
            allValid = False
            
        #final validation
        if allValid == True:
            self.dataToAdd = self.controller.get_new_cinema(self.cityGet, self.locationGet,self.seatEntry) ###HERE
        else:
            messagebox.showerror(title = 'Error',message='Please enter integer for seating capacity and string for city/location')

    """Fiorella Scarpino 21010043"""
    def clear_text(self):
        #clears entry text
        self.city_Entry.delete(0,END)
        self.location_Entry.delete(0, END)
        self.screen_Entry.delete(0, END) # number of screens
        self.getScreenNumber['state'] = NORMAL


    """Sude Fidan 21068639"""
    def logout_clicked(self):
        if self.controller:
            self.controller.logout()

    """Sude Fidan 21068639"""
    def set_controller(self, controller):
        self.controller = controller