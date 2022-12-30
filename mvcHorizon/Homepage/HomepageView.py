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
        frame1 = ttk.Frame(self.notebook, width=800, relief='sunken', height=280)
        frame1.pack(fill='both', expand=True)
        self.notebook.add(frame1, text='Make Booking')
        frame2 = ttk.Frame(self.notebook, width=800, relief='raised', height=280)
        frame2.pack(fill='both', expand=True)
        self.notebook.add(frame2, text='Make Cancellation')
        if self.controller.showOtherBooking:
            frame3 = ttk.Frame(self.notebook, width=800, relief='groove', height=280)
            frame3.pack(fill='both', expand=True)
            self.notebook.add(frame3, text='Make Booking In Other Cinema')
        if self.controller.showManageScreening:
            frame4 = ttk.Frame(self.notebook, width=800, relief='solid', height=280)
            frame4.pack(fill='both', expand=True)
            self.notebook.add(frame4, text='Manage Screening')
        if self.controller.showGenerateReport:
            frame5 = ttk.Frame(self.notebook, width=800, relief='sunken', height=280)
            frame5.pack(fill='both', expand=True)
            self.notebook.add(frame5, text='Generate Report')
        if self.controller.showAddCinema:
            frame6 = ttk.Frame(self.notebook, width=800, relief='raised', height=280)
            frame6.pack(fill='both', expand=True)
            self.notebook.add(frame6, text='Add New Cinema')

        #logout button
        Button(self, text="Logout", width=10, height=1, command=self.logout_clicked, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM, anchor="e")
        
    def logout_clicked(self):
        if self.controller:
            self.controller.logout()

        
    def set_controller(self, controller):
        self.controller = controller