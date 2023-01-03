from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
import numpy as np

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

    """Fiorella Scarpino"""
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
    
    def manage_view(self):
        #manage frame
        self.manage = Frame(self.notebook, width=800, height=280)
        self.manage.pack(fill='both', expand=True)
        self.notebook.add(self.manage, text='Manage Screening')
        

        #create nested notebook
        self.screeningNotebook = ttk.Notebook(self.manage)
        self.screeningNotebook.pack(pady=10, expand=True)

        self.add_film_view()
        self.remove_film_view()
        self.update_show_time_view()
        self.attach_show_view()

        
    def add_film_view(self):
        #add film frame
        self.addFilm = Frame(self.screeningNotebook, width=740, height=280)
        self.addFilm.pack(fill='both', expand=True)
        self.screeningNotebook.add(self.addFilm, text='Add Film')

    def remove_film_view(self):
        #remove film frame
        self.removeFilm = Frame(self.screeningNotebook, width=740, height=280)
        self.removeFilm.pack(fill='both', expand=True)
        self.screeningNotebook.add(self.removeFilm, text='Remove Film')

    def update_show_time_view(self):
        #update show times frame
        self.updateShowTime = Frame(self.screeningNotebook, width=740, height=280)
        self.updateShowTime.pack(fill='both', expand=True)
        self.screeningNotebook.add(self.updateShowTime, text='Update Show Times')

    def attach_show_view(self):
        #attach shows to screen/hall frame
        self.attachShow = Frame(self.screeningNotebook, width=740, height=280)
        self.attachShow.pack(fill='both', expand=True)
        self.screeningNotebook.add(self.attachShow, text='Attach Shows to Screen/hall')

    def report_view(self):
        #report frame
        self.report = Frame(self.notebook, width=800, height=280)
        self.report.pack(fill='both', expand=True)
        self.notebook.add(self.report, text='Generate Report')
    
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
            
            self.addCinemaButton = Button(self.new_cinema, text='Add New Cinema',command=lambda: self.get_newCinema(), width=12).pack()
        except TclError:  #validation for integer
            self.getScreenNumber['state'] = NORMAL
            messagebox.showerror(title = 'Error',message='Please enter an integer')

    """Fiorella Scarpino 21010043"""
    def get_newCinema(self):
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
            self.dataToAdd = self.controller.get_newCinema(self.cityGet, self.locationGet,self.seatEntry) ###HERE
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
