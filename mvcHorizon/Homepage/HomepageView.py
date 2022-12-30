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
        

        '''
        #Creating layout of homepage
        Label(self,width="300", text="Homepage", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
        #Make Booking button
        Button(self, text="Make Booking", width=30, height=5, bg="#0E6655", font=("Arial",12,"bold")).place(x=20,y=40)
        #Make Cancellation button
        Button(self, text="Make Cancellation", width=50, height=5, bg="#0E6655",font=("Arial",12,"bold")).place(x=120,y=40)
        #Make Booking In Other Cinema button for admin only
        if self.controller.showOtherBookingButton:
            Button(self, text="Make Booking In Other Cinema", width=50, height=5, bg="#0E6655",font=("Arial",12,"bold")).place(x=20,y=80)
        #Manage Screening button
        if self.controller.showManageScreeningButton:
            Button(self, text="Manage Screening", width=50, height=5, bg="#0E6655",font=("Arial",12,"bold")).place(x=120,y=80)
        #Generate Report button
        if self.controller.showGenerateReportButton:
            Button(self, text="Generate Report", width=50, height=5, bg="#0E6655",font=("Arial",12,"bold")).place(x=20,y=120)
        #Add New Cinema button for manager only
        if self.controller.showAddCinemaButton:
            Button(self, text="Add New Cinema", width=50, height=5, bg="#0E6655",font=("Arial",12,"bold")).place(x=120,y=120)
        '''

        
    def set_controller(self, controller):
        self.controller = controller