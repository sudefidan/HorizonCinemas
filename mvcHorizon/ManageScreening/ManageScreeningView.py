from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry

class ManageScreeningView(Frame):
    """Sude Fidan 21068639"""
    def __init__(self, parent):

        super().__init__(parent)

        #create nested notebook
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(pady=10, expand=True)   
    
    """Sude Fidan 21068639"""
    def manage_screening(self):
        self.add_film_view()
        self.remove_film_view()
        self.update_show_time_view()
        self.attach_show_view()

    """Sude Fidan 21068639"""
    def add_film_view(self):
        #declaring variable
        name = StringVar()
        cast = StringVar()
        rating = StringVar()
        genre = StringVar()
        year = IntVar()
        description = StringVar()
        duration = StringVar()
        age = IntVar()

        #add film frame
        self.addFilm = Frame(self.notebook, width=740, height=280)
        self.addFilm.pack(fill='both', expand=True)
        self.notebook.add(self.addFilm, text='Add Film')

        #Login Form
        Label(self.addFilm, text="Please enter film details",bg="#0E6655", fg="white",font=("Arial",13,"bold"), width=100).pack(side=TOP)
        #film name entry
        Label(self.addFilm, text="Film Name:",fg="white",font=("Arial",14,"bold")).pack()
        nameField = Entry(self.addFilm, textvariable=name,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        #cast entry
        Label(self.addFilm, text="Cast:",fg="white",font=("Arial",14,"bold")).pack()
        castField = Entry(self.addFilm, textvariable=cast,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        #rating entry
        Label(self.addFilm, text="Rating: ",fg="white",font=("Arial",14,"bold")).pack()
        ratingField = Entry(self.addFilm, textvariable=rating,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        #genre entry
        Label(self.addFilm, text="Genre: ",fg="white",font=("Arial",14,"bold")).pack()
        genreField = Entry(self.addFilm, textvariable=genre,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        #year entry
        Label(self.addFilm, text="Release Year: ",fg="white",font=("Arial",14,"bold")).pack()
        yearField = Entry(self.addFilm, textvariable=year,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        #description entry
        Label(self.addFilm, text="Description: ",fg="white",font=("Arial",14,"bold")).pack()
        descriptionField = Entry(self.addFilm, textvariable=description,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        #duration entry
        Label(self.addFilm, text="Duration: ",fg="white",font=("Arial",14,"bold")).pack()
        durationField = Entry(self.addFilm, textvariable=duration,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()
        #age entry
        Label(self.addFilm, text="Age Rating:",fg="white",font=("Arial",14,"bold")).pack()
        ageField = Entry(self.addFilm, textvariable=age,bg="#1C2833",fg="white",font=("Arial",12,"bold")).pack()

    """Sude Fidan 21068639"""
    def remove_film_view(self):
        #remove film frame
        self.removeFilm = Frame(self.notebook, width=740, height=280)
        self.removeFilm.pack(fill='both', expand=True)
        self.notebook.add(self.removeFilm, text='Remove Film')

    """Cameron Povey 21011010"""
    def update_show_time_view(self):
        #update show times frame
        self.updateShowTime = Frame(self.notebook, width=740, height=280)
        self.updateShowTime.pack(fill='both', expand=True)
        self.notebook.add(self.updateShowTime, text='Update Show Times')

    """Cameron Povey 21011010"""
    def attach_show_view(self):
        #attach shows to screen/hall frame
        self.attachShow = Frame(self.notebook, width=740, height=280)
        self.attachShow.pack(fill='both', expand=True)
        self.notebook.add(self.attachShow, text='Attach Shows to Screen/hall')

    """Sude Fidan 21068639"""
    def set_controller(self, controller):
        self.controller = controller

    
