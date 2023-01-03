from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry

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
        self.frame1_view()
        self.frame2_view()
        self.frame3_view()
        #admin and manager access
        if self.controller.showManageScreening:
            self.frame4_view()
        #admin and manager access
        if self.controller.showGenerateReport:
            self.frame5_view()
        #only manager access
        if self.controller.showAddCinema:
            self.frame6_view()
            
        #staff details 
        Label(self, text=self.controller.get_user(), width=30, height=5, fg= '#ffffff',font=("Arial",12,"bold")).place(relx = 1.0, rely = 0.0,anchor="ne")

        #logout button
        Button(self, text="Logout", width=10, height=1, command=self.logout_clicked, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM, anchor="e")

    """Fiorella Scarpino"""
    def frame1_view(self):
        #frame1
        self.frame1 = Frame(self.notebook, width=800, height=280)
        self.frame1.pack(fill='both', expand=True)
        self.notebook.add(self.frame1, text='Listings')
        #self.controller.listings()

        #proceed booking button
        Button(self.frame1, text="Proceed Booking", width=10, height=1, command=self.show_make_booking, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM)
        
        #movie scrollbar
        scrollbar = Scrollbar(self.frame1, orient="vertical")
        self.movieFrame=Listbox(self.frame1,bg = "grey64",selectbackground="grey",activestyle = 'dotbox',yscrollcommand=scrollbar.set)
        self.movieFrame.pack(side=LEFT, fill='both', expand=True, anchor="n")
        scrollbar.config(command=self.movieFrame.yview)

        #insert movie names
        self.records = self.controller.get_films()
        for row in self.records:
            movieName=row[1]
            self.movieFrame.insert('end',movieName)

        #movie info scrollbar
        self.textOutput = Text(self.frame1,bg = "grey64",wrap=WORD)   
        self.textOutput.pack(side=TOP, fill='both', expand=True, anchor="e")

        #correlate film selection to data from database        
        self.movieFrame.bind('<<ListboxSelect>>',self.get_selection)

        #show scrollbar
        columns = ('date', 'time', 'screenid')
        self.tree = ttk.Treeview(self.frame1, columns=columns, show='headings')
        self.tree.pack(side=RIGHT, fill='both', expand=True, anchor="n")
        self.tree.heading('date', text='Date')
        self.tree.heading('time', text='Time')
        self.tree.heading('screenid', text='Screen')

    """Fiorella Scarpino"""
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
    def frame2_view(self):
        #frame2
        self.frame2 = Frame(self.notebook, width=800, height=280)
        self.frame2.pack(fill='both', expand=True)
        self.notebook.add(self.frame2, text='Make Booking')
        
    """Cameron Povey 21011010"""
    def frame3_view(self):
        #frame3      
        self.frame3 = ttk.Frame(self.notebook, width=800, height=280)
        self.frame3.pack(fill='both', expand=True)
        self.notebook.add(self.frame3, text='Make Cancellation')
    
    def frame4_view(self):
        #frame4
        self.frame4 = ttk.Frame(self.notebook, width=800, height=280)
        self.frame4.pack(fill='both', expand=True)
        self.notebook.add(self.frame4, text='Manage Screening')

    def frame5_view(self):
        #frame5
        self.frame5 = ttk.Frame(self.notebook, width=800, height=280)
        self.frame5.pack(fill='both', expand=True)
        self.notebook.add(self.frame5, text='Generate Report')
    
    """Fiorella Scarpino"""
    def frame6_view(self):
        #frame6
        self.frame6 = ttk.Frame(self.notebook, width=800, height=280)
        self.frame6.pack(fill='both', expand=True)
        self.notebook.add(self.frame6, text='Add New Cinema')

    """Sude Fidan 21068639"""
    def logout_clicked(self):
        if self.controller:
            self.controller.logout()

    """Sude Fidan 21068639"""
    def set_controller(self, controller):
        self.controller = controller