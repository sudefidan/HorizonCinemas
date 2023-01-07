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
        
        #line 1
        line1 = Frame(self.updateShowTime, bg="cyan", pady=5)
        line1.pack(fill=X)
        
        Label(line1, text="Enter show ID", font=("Arial", 25), fg='Black', bg='Cyan').pack(fill=BOTH)
        self.update_shows = Spinbox(line1, from_=1, to=999999)
        self.update_shows.pack(fill=X)
        Button(line1, text="Find Show Times", bg="cyan", padx=2,pady=2, command=lambda: self.getShowTimes()).pack(fill=Y)
        
        #line 2
        line2 = Frame(self.updateShowTime, bg="white", pady=5)
        line2.pack(fill=X)
        
        self.cpUST_date = Label(line2, text="Date: ", bg="white", fg="black", padx=5, pady=5)
        self.cpUST_time = Label(line2, text="Time: ", bg="white", fg="black", padx=5, pady=5)
        self.cpUST_cinema = Label(line2, text="Cinema: ", bg="white", fg="black", padx=5, pady=5)
        self.cpUST_film = Label(line2, text="Film: ", bg="white", fg="black", padx=5, pady=5)
        
        self.cpUST_date.pack(fill=X, side=LEFT)
        self.cpUST_time.pack(fill=X, side=LEFT)
        self.cpUST_cinema.pack(fill=X, side=LEFT)
        self.cpUST_film.pack(fill=X, side=LEFT)
        
        #editDate
        editInfo = Frame(self.updateShowTime, bg="white", pady=5)
        editInfo.pack(fill=BOTH)
        
        self.cpUST_editdate = DateEntry(editInfo, bg=None, state=DISABLED)
        self.cpUST_editdate.pack()
        self.cpUST_dateconfirm = Button(editInfo, background="blue", command=lambda: self.cpUST_changeinfo.configure(state=NORMAL), text="confirm", state=DISABLED)
        self.cpUST_dateconfirm.pack()
        
        self.cpUST_hourshow = IntVar()
        self.cpUST_minshow = IntVar()
        
        #editTime
        editTime = Frame(self.updateShowTime, bg="white", pady=5)
        editTime.pack(fill=BOTH)
        
        self.cpUST_timechangeH = Spinbox(editTime, from_=00, to=24, width=2, state=DISABLED, textvariable=self.cpUST_hourshow, command=lambda: self.cpUST_changeinfo.configure(state=NORMAL))#disabled
        self.cpUST_timechangeH.pack(side=LEFT)
        self.cpUST_middlebit = Label(editTime, text=":", state=DISABLED)#disabled
        self.cpUST_middlebit.pack(side=LEFT)
        self.cpUST_timechangeM = Spinbox(editTime, from_=00, to=59, width=2, state=DISABLED, textvariable=self.cpUST_minshow, command=lambda: self.cpUST_changeinfo.configure(state=NORMAL))#disabled
        self.cpUST_timechangeM.pack(side=LEFT)
        
        updateframe = Frame(self.updateShowTime, height=200, width=200, bg=None, pady=10, padx=50)
        updateframe.pack(fill=X)
        self.cpUST_changeinfo = Button(updateframe, text="UPDATE", state=DISABLED, font=("Arial", 25), command=lambda: self.confirmChange())
        self.cpUST_changeinfo.pack(fill=X, side=TOP)
        
        self.setstate = [self.cpUST_editdate, self.cpUST_timechangeH, self.cpUST_middlebit, self.cpUST_timechangeM, self.cpUST_dateconfirm]
    
    """Cameron Povey 21011010"""
    def getShowTimes(self):
        showid = self.update_shows.get()
        self.upshowinfo = self.controller.getShowTimes(showid)
        
        if self.upshowinfo == 0: 
            for part in self.setstate:
                part.configure(state=DISABLED)
                print("NOT FOUND")
            return 0
        
        self.cpUST_date.configure(text="Date: " + str(self.upshowinfo[1]))
        self.cpUST_time.configure(text="Time: " + str(self.upshowinfo[2]))
        self.cpUST_cinema.configure(text="Cinema: " + str(self.upshowinfo[3]))
        self.cpUST_film.configure(text="Film: " + str(self.upshowinfo[4]))
        self.cpUST_changeinfo.configure(state=DISABLED)
        
        for part in self.setstate:
            part.configure(state=NORMAL)
            
        self.cpUST_editdate.set_date(self.upshowinfo[1])
        h, m = self.upshowinfo[2].split(':')
        self.cpUST_hourshow.set(h)
        self.cpUST_minshow.set(m)
    
    """Cameron Povey 21011010"""
    def confirmChange(self):
        date = self.cpUST_editdate.get()
        timeh = self.cpUST_timechangeH.get()
        timem = self.cpUST_timechangeM.get()
        self.controller.confirmChange(date, timeh, timem)
    
    """Cameron Povey 21011010"""
    def attach_show_view(self):
        #attach shows to screen/hall frame
        self.attachShow = Frame(self.notebook, width=740, height=280)
        self.attachShow.pack(fill='both', expand=True)
        self.notebook.add(self.attachShow, text='Attach Shows to Screen/hall')


    """Sude Fidan 21068639"""
    def set_controller(self, controller):
        self.controller = controller

    
