"""Sude Fidan 21068639"""
"""Cameron Povey 21011010"""
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox 

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
        self.newFilmName = StringVar()
        self.newFilmCast = StringVar()
        self.newFilmRating = StringVar()
        self.newFilmGenre = StringVar()
        self.newFilmYear = StringVar()
        self.newFilmDescription = StringVar()
        self.newFilmDuration = StringVar()
        self.newFilmAge = StringVar()

        #add film frame
        self.addFilm = Frame(self.notebook, width=740, height=280)
        self.addFilm.pack(fill='both', expand=True)
        self.notebook.add(self.addFilm, text='Add Film')
        Label(self.addFilm, text="Please enter film details",bg="#0E6655", fg="white",font=("Arial",13,"bold"), width=100).pack(side=TOP)

        #film name entry
        Label(self.addFilm, text="Film Name:",fg="white",font=("Arial",14,"bold")).pack()
        self.newFilmNameEntry = Entry(self.addFilm, textvariable=self.newFilmName,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.newFilmNameEntry.pack()
        #cast entry
        Label(self.addFilm, text="Cast:",fg="white",font=("Arial",14,"bold")).pack()
        self.newFilmCastEntry = Entry(self.addFilm, textvariable=self.newFilmCast,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.newFilmCastEntry.pack()
        #rating entry
        Label(self.addFilm, text="Rating: ",fg="white",font=("Arial",14,"bold")).pack()
        self.newFilmRatingEntry =Entry(self.addFilm, textvariable=self.newFilmRating,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.newFilmRatingEntry.pack()
        #genre entry
        Label(self.addFilm, text="Genre: ",fg="white",font=("Arial",14,"bold")).pack()
        self.newFilmGenreEntry = Entry(self.addFilm, textvariable=self.newFilmGenre,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.newFilmGenreEntry.pack()
        #year entry
        Label(self.addFilm, text="Release Year: ",fg="white",font=("Arial",14,"bold")).pack()
        self.newFilmYearEntry = Entry(self.addFilm, textvariable=self.newFilmYear,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.newFilmYearEntry.pack()
        #description entry
        Label(self.addFilm, text="Description: ",fg="white",font=("Arial",14,"bold")).pack()
        self.newFilmDescriptionEntry = Entry(self.addFilm, textvariable=self.newFilmDescription,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.newFilmDescriptionEntry.pack()
        #duration entry
        Label(self.addFilm, text="Duration: ",fg="white",font=("Arial",14,"bold")).pack()
        self.newFilmDurationEntry = Entry(self.addFilm, textvariable=self.newFilmDuration,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.newFilmDurationEntry.pack()
        #age entry
        Label(self.addFilm, text="Age Rating:",fg="white",font=("Arial",14,"bold")).pack()
        self.newFilmAgeEntry = Entry(self.addFilm, textvariable=self.newFilmAge,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.newFilmAgeEntry.pack()

        #Label for displaying error
        self.addFilmErrorLabel = Label(self.addFilm, text='',font=("Arial",12,"bold"))
        self.addFilmErrorLabel.pack()

        Button(self.addFilm, text='Add New Film',command=lambda: self.add_film(), width=12).pack()
    
    """Sude Fidan 21068639"""
    def add_film(self):
        addingState = self.controller.commit_add_film(self.newFilmName.get(),self.newFilmCast.get(),self.newFilmRating.get(),self.newFilmGenre.get(),self.newFilmYear.get(),self.newFilmDescription.get(),self.newFilmDuration.get(),self.newFilmAge.get())
        if addingState == 0:
            self.addFilmErrorLabel.config(text="ERROR, Contact Admin!!", font=('Arial', 20) ,pady=10,width=50, bg=None, fg="Red")
        elif addingState == 1: 
            self.addFilmErrorLabel.config(text ="Film Added!", font=('Arial', 20) ,pady=10,width=50, bg=None, fg="Green")
            self.newFilmNameEntry.delete(0,END)
            self.newFilmCastEntry.delete(0,END)
            self.newFilmRatingEntry.delete(0,END)
            self.newFilmGenreEntry.delete(0,END)
            self.newFilmYearEntry.delete(0,END)
            self.newFilmDescriptionEntry.delete(0,END)
            self.newFilmDurationEntry.delete(0,END)
            self.newFilmAgeEntry.delete(0,END)
        elif addingState == 2: 
            self.addFilmErrorLabel.config(text="Please enter integer for rating, release year, duration and age rating", font=('Arial', 20) ,pady=10,width=50, bg=None, fg="Red")
        else:
            self.addFilmErrorLabel.config(text="Please enter all fields", font=('Arial', 20) ,pady=10,width=50, bg=None, fg="Red")
        self.addFilmErrorLabel.pack(expand=True)

    """Sude Fidan 21068639"""
    def remove_film_view(self):
        #remove film frame
        self.removeFilm = Frame(self.notebook, width=740, height=280)
        self.removeFilm.pack(fill='both', expand=True)
        self.notebook.add(self.removeFilm, text='Remove Film')

        self.deleteFilm = StringVar()

        #age entry
        Label(self.removeFilm, text="Film Name:",fg="white",font=("Arial",14,"bold")).pack()
        self.filmEntry = Entry(self.removeFilm, textvariable=self.deleteFilm,bg="#1C2833",fg="white",font=("Arial",12,"bold"))
        self.filmEntry.pack()

        #Label for displaying error
        self.removeFilmErrorLabel = Label(self.removeFilm, text='',font=("Arial",12,"bold"))
        self.removeFilmErrorLabel.pack()

        Button(self.removeFilm, text='Remove Film',command=lambda: self.remove_film(), width=12).pack()

    """Sude Fidan 21068639"""
    def remove_film(self):
        removedState = self.controller.commit_remove_film(self.deleteFilm.get())
        if removedState == 0:
            self.removeFilmErrorLabel.config(text="ERROR, Contact Admin!!", font=('Arial', 20) ,pady=10,width=50, bg=None, fg="Red")
        elif removedState ==1:
            self.removeFilmErrorLabel.config(text ="Film Removed!", font=('Arial', 20) ,pady=10,width=50, bg=None, fg="Green")
            self.filmEntry.delete(0,END)
        elif removedState ==2:
            self.removeFilmErrorLabel.config(text="Film could not found, Contact Admin!!!", font=('Arial', 20) ,pady=10,width=50, bg=None, fg="Red")
        else:
            self.removeFilmErrorLabel.config(text ="Please enter all fields!", font=('Arial', 20) ,pady=10,width=50, bg=None, fg="Red")
        self.removeFilmErrorLabel.pack()

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

    
