from tkinter import *
from tkinter import ttk

class HomepageView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)
        
    
    def homepage(self):
        #create frames and add frames to notebook
        self.frame1 = ttk.Frame(self.notebook, width=800, relief='sunken', height=280)
        self.frame1.pack(fill='both', expand=True)
        self.notebook.add(self.frame1, text='Listings')
        
        self.frame2 = ttk.Frame(self.notebook, width=800, relief='sunken', height=280)
        self.frame2.pack(fill='both', expand=True)
        self.notebook.add(self.frame2, text='Make Booking')

        #proceed booking button
        Button(self.frame1, text="Proceed Booking", width=10, height=1, command=self.show_make_booking, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM)


        frame3 = ttk.Frame(self.notebook, width=800, relief='raised', height=280)
        frame3.pack(fill='both', expand=True)
        self.notebook.add(frame3, text='Make Cancellation')
        if self.controller.showOtherBooking:
            frame4 = ttk.Frame(self.notebook, width=800, relief='groove', height=280)
            frame4.pack(fill='both', expand=True)
            self.notebook.add(frame4, text='Make Booking In Other Cinema')
        if self.controller.showManageScreening:
            frame5 = ttk.Frame(self.notebook, width=800, relief='solid', height=280)
            frame5.pack(fill='both', expand=True)
            self.notebook.add(frame5, text='Manage Screening')
        if self.controller.showGenerateReport:
            frame6 = ttk.Frame(self.notebook, width=800, relief='sunken', height=280)
            frame6.pack(fill='both', expand=True)
            self.notebook.add(frame6, text='Generate Report')
        if self.controller.showAddCinema:
            frame7 = ttk.Frame(self.notebook, width=800, relief='raised', height=280)
            frame7.pack(fill='both', expand=True)
            self.notebook.add(frame7, text='Add New Cinema')

        #staff details 
        staff= Label(self, text=self.controller.get_user(), width=30, height=5, fg= '#ffffff',font=("Arial",12,"bold"))
        staff.place(relx = 1.0, rely = 0.0,anchor='ne')

        #logout button
        Button(self, text="Logout", width=10, height=1, command=self.logout_clicked, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM, anchor="e")

    def show_make_booking(self):
        self.notebook.select(tab_id=1)

    def logout_clicked(self):
        if self.controller:
            self.controller.logout()

    def set_controller(self, controller):
        self.controller = controller