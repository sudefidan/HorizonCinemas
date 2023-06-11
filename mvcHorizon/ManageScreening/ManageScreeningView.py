"""Sude Fidan 21068639"""
"""Cameron Povey 21011010"""
"""Fiorella Scarpino 21010043"""
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter.ttk import Treeview
import time

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
        self.add_new_shows()
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
        Label(self.removeFilm, text="Please enter film details",bg="#0E6655", fg="white",font=("Arial",13,"bold"), width=100).pack(side=TOP)


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
    
    """Fiorella Scarpino 21010043"""
    def add_new_shows(self):
        #add new shows
        self.newShows = Frame(self.notebook, width=740, height=280)
        self.newShows.pack(fill='both', expand=True)
        self.notebook.add(self.newShows, text='Add New Shows')

        #for padding
        self.padding = {'ipadx': 10, 'ipady': 10}
        title = Label(self.newShows,text="Add New Shows",bg="#0E6655", fg="white",font=14).pack(**self.padding)

        #date
        dateCreateShowLabel = Label(self.newShows, text='Choose Date', bg="#0E6655", fg="white",font=12).pack(**self.padding, fill=X)
        self.dateCreateShow = DateEntry(self.newShows)
        self.dateCreateShow.pack(**self.padding, fill=X)

        #time
        timeCreateShowLabel = Label(self.newShows, text='Choose Time', bg="#0E6655", fg="white",font=12).pack(**self.padding, fill=X)
        hourString=StringVar()
        minutesString=StringVar()
        self.timeCreateShowHours = Spinbox(self.newShows,from_=0,to=23,wrap=True,textvariable=hourString,state="readonly")
        self.timeCreateShowMin = Spinbox(self.newShows,from_ =0, to=59, wrap=True, textvariable=minutesString)
        self.timeCreateShowHours.pack(side=TOP,**self.padding)
        self.timeCreateShowMin.pack(side=TOP,**self.padding)

        #film
        self.filmCreateShow = StringVar()
        filmrecords = self.controller.createNewFilm()
        filmCreateShowVariable = StringVar(self.newShows)
        filmCreateShowVariable.set(filmrecords[0]) 
        filmCreateShowLabel = Label(self.newShows, text='Choose Film',bg="#0E6655", fg="white", font=12).pack(**self.padding, fill=X)
        self.filmCreateShowOption = OptionMenu(self.newShows, filmCreateShowVariable, *filmrecords)
        self.filmCreateShowOption.pack()

        #cinema
        cinemarecords = self.controller.createNewCinema()
        self.cinemaCreateShowVariable = StringVar(self.newShows)
        self.cinemaCreateShowVariable.set('Choose a Cinema')
        cinemaCreateShowLabel = Label(self.newShows, text='Choose Cinema', bg="#0E6655", fg="white",font=12).pack(**self.padding, fill=X)
        cinemaCreateShow = OptionMenu(self.newShows, self.cinemaCreateShowVariable, *cinemarecords,command=self.dataForOptionScreen)
        cinemaCreateShow.pack()
        cinemaCreateShow.bind('<<OptionMenuSelect>>',self.dataForOptionScreen)

        #screen
        self.screenCreateShowVariable = StringVar(self.newShows)
        screenCreateShowLabel = Label(self.newShows, text='Choose Screen', bg="#0E6655", fg="white",font=12).pack(**self.padding, fill=X)
        columns = ('screenid')
        self.AddNewShowsTree = ttk.Treeview(self.newShows, columns=columns, show='headings')
        self.AddNewShowsTree.pack(side=RIGHT,fill='both', expand=True, anchor="n")
        self.AddNewShowsTree.heading('screenid', text='Screen')

        #final button
        self.finalCreateNewButton = Button(self.newShows, text="Confirm Option",command=lambda: self.screenNewShowsGet(),)
        self.finalCreateNewButton.pack(**self.padding)

    """Fiorella Scarpino 21010043"""
    def dataForOptionScreen(self,selection):
        #delete data from treeview
        for item in self.AddNewShowsTree.get_children():
            self.AddNewShowsTree.delete(item)
        self.userSelectionNewShows = ''
        self.userSelectionNewShows = (selection)

        #gets data of screens
        self.screenToOutput = []
        screenrecords = self.controller.createNewScreen(self.userSelectionNewShows)
        for i in screenrecords:
            self.screenToOutput.append(i[1])
        for row in self.screenToOutput:
                self.AddNewShowsTree.insert('', END, values=row)

    """Fiorella Scarpino 21010043"""
    def screenNewShowsGet(self):
        selectedScreen = self.AddNewShowsTree.focus()
        newScreenSelected = self.AddNewShowsTree.item(selectedScreen)
        self.screenUserShow = newScreenSelected.get("values")
        userSelectionNewShowsName = self.userSelectionNewShows[0]#cinema
        dateNewShow = self.dateCreateShow.get()#date
        #formats the date
        self.newDateForShow = time.mktime(datetime.strptime(dateNewShow, "%m/%d/%y").timetuple())
        self.newDateForShow = self.newDateForShow * 1000 #turns into milliseconds

        #time
        hoursTime = self.timeCreateShowHours.get()
        minutesTime = self.timeCreateShowMin.get()
        #formats the time
        if int(hoursTime) <=9:
            hoursTime = '0'+ hoursTime
        if int(minutesTime) <= 9:
            minutesTime = '0'+ minutesTime
        self.newTimeShow = hoursTime + ":" + minutesTime
        self.dataToAddForShow = self.controller.addDataForNewShow(self.newDateForShow,self.newTimeShow,self.screenUserShow,userSelectionNewShowsName)

    """Cameron Povey 21011010"""
    def update_show_time_view(self):
        #update show times frame
        self.updateShowTime = Frame(self.notebook, width=740, height=280)
        self.updateShowTime.pack(fill='both', expand=True)
        self.notebook.add(self.updateShowTime, text='Update Show Times')

        #line 1
        line1 = Frame(self.updateShowTime, bg="#0E6655", pady=5)
        line1.pack(fill=X)
        
        Label(line1, text="Enter show ID", font=("Arial", 25), fg='Black', bg='#0E6655').pack(fill=BOTH)
        self.update_shows = Spinbox(line1, from_=1, to=999999)
        self.update_shows.pack(fill=X)
        Button(line1, text="Find Show Times", bg="#0E6655", padx=2,pady=2, command=lambda: self.get_show_times()).pack(fill=Y)
        
        #line 2
        line2 = Frame(self.updateShowTime, bg="white", pady=5)
        line2.pack(fill=X)
        
        self.oldShowDate = Label(line2, text="Date: ", bg="white", fg="black", padx=5, pady=5)
        self.oldShowTime = Label(line2, text="Time: ", bg="white", fg="black", padx=5, pady=5)
        self.oldShowCinema = Label(line2, text="Cinema: ", bg="white", fg="black", padx=5, pady=5)
        self.oldShowFilm = Label(line2, text="Film: ", bg="white", fg="black", padx=5, pady=5)
        
        self.oldShowDate.pack(fill=X, side=LEFT)
        self.oldShowTime.pack(fill=X, side=LEFT)
        self.oldShowCinema.pack(fill=X, side=LEFT)
        self.oldShowFilm.pack(fill=X, side=LEFT)
        
        #edit date
        editInfo = Frame(self.updateShowTime, bg="white", pady=5)
        editInfo.pack(fill=BOTH)
        
        self.newDate = DateEntry(editInfo, bg=None, state=DISABLED)
        self.newDate.pack()
        self.newDateConfirm = Button(editInfo, background="blue", command=lambda: self.changeInfo.configure(state=NORMAL), text="Confirm", state=DISABLED)
        self.newDateConfirm.pack()
        
        self.hourShow = IntVar()
        self.minShow = IntVar()
        
        #edit time
        editTime = Frame(self.updateShowTime, bg="white", pady=5)
        editTime.pack(fill=BOTH)
        
        self.hoursEdited = Spinbox(editTime, from_=00, to=24, width=2, state=DISABLED, textvariable=self.hourShow, command=lambda: self.changeInfo.configure(state=NORMAL))#disabled
        self.hoursEdited.pack(side=LEFT)
        middleEdit = Label(editTime, text=":", state=DISABLED)#disabled
        middleEdit.pack(side=LEFT)
        self.minEdited = Spinbox(editTime, from_=00, to=59, width=2, state=DISABLED, textvariable=self.minShow, command=lambda: self.changeInfo.configure(state=NORMAL))#disabled
        self.minEdited.pack(side=LEFT)
        
        updateframe = Frame(self.updateShowTime, height=200, width=200, bg=None, pady=10, padx=50)
        updateframe.pack(fill=X)
        self.changeInfo = Button(updateframe, text="UPDATE", state=DISABLED, font=("Arial", 25), command=lambda: self.confirm_change())
        self.changeInfo.pack(fill=X, side=TOP)
        
        self.setState = [self.newDate, self.hoursEdited, middleEdit, self.minEdited, self.newDateConfirm]
    
    """Cameron Povey 21011010"""
    def get_show_times(self):
        showId = self.update_shows.get()
        self.updatedShowInfo = self.controller.get_show_times(showId)
        
        if self.updatedShowInfo == 0: 
            for part in self.setState:
                part.configure(state=DISABLED)
                print("NOT FOUND")
            return 0
        
        self.oldShowDate.configure(text="Date: " + str(self.updatedShowInfo[1]))
        self.oldShowTime.configure(text="Time: " + str(self.updatedShowInfo[2]))
        self.oldShowCinema.configure(text="Cinema: " + str(self.updatedShowInfo[3]))
        self.oldShowFilm.configure(text="Film: " + str(self.updatedShowInfo[4]))
        self.changeInfo.configure(state=DISABLED)
        
        for part in self.setState:
            part.configure(state=NORMAL)
            
        self.newDate.set_date(self.updatedShowInfo[1])
        h, m = self.updatedShowInfo[2].split(':')
        self.hourShow.set(h)
        self.minShow.set(m)
    
    """Cameron Povey 21011010"""
    def confirm_change(self):
        date = self.newDate.get()
        hour = self.hoursEdited.get()
        minute = self.minEdited.get()
        self.controller.confirm_change(date, hour, minute)

    """Cameron Povey 21011010"""
    def attach_show_view(self):
        #attach shows to screen/hall frame
        attachShow = Frame(self.notebook, width=740, height=280)
        attachShow.pack(fill='both', expand=True)
        self.notebook.add(attachShow, text='Attach Shows to Screen/hall')

        self.successMessage = False
        self.errorMessage = False
        
        line1 = Frame(attachShow, bg="#0E6655", pady=5)
        line1.pack(fill=X)
        
        self.showTitle = Label(line1, text="Enter show ID", bg="#0E6655", font=("Arial", 25), fg='Black')
        self.showTitle.pack(fill=BOTH, expand=True)
        self.showSpin = Spinbox(line1, from_=1, to=999999)
        self.showSpin.pack(fill=Y)
        Button(line1, text="Find Show Times", bg="#0E6655", padx=2,pady=2, command=lambda: self.fetch_screen_numbers()).pack(fill=Y) #function

        line2 = Frame(attachShow, bg="#0E6655", pady=5)
        line2.pack(fill=X)
        
        self.reShowDate = Label(line2, text="Date: ", bg="white", fg="black", padx=10, pady=10)
        self.reShowDate.pack(fill=X, side=LEFT, expand=True)
        self.reShowTime = Label(line2, text="Time: ", bg="white", fg="black", padx=10, pady=10)
        self.reShowTime.pack(fill=X, side=LEFT, expand=True)
        self.reShowFilm = Label(line2, text="Film: ", bg="white", fg="black", padx=10, pady=10)
        self.reShowFilm.pack(fill=X, side=LEFT, expand=True)
        
        Label(attachShow, font=("Arial", 25), text="Select Screen ID", pady=10).pack()
        
        editInfo = Frame(attachShow, bg=None, pady=0)
        editInfo.pack(fill=X, expand=True, side=LEFT)
        self.editScreen = Spinbox(editInfo, bg=None, state=DISABLED,from_=1, to=99999)
        self.editScreen.pack()
        
        self.updateFrame = Frame(attachShow, height=200, width=200, bg=None, pady=10, padx=50)
        self.updateFrame.pack(fill=X)
        self.attachInfo = Button(self.updateFrame, text="UPDATE", font=("Arial", 25), state=DISABLED, command=lambda: self.commitChange()) #function
        self.attachInfo.pack(fill=X, expand=True, side=TOP)

    """Cameron Povey 21011010"""   
    def check_messages(self):
        if self.successMessage == True:
            self.success.pack_forget()
            self.successMessage = False
        if self.errorMessage == True:
            self.error.pack_forget()
            self.errorMessage = False

    """Cameron Povey 21011010"""
    def fetch_screen_numbers(self):
        showId = self.showSpin.get()
        upShowInfo = self.controller.fetch_screen_numbers(showId)
        self.check_messages()
        
        if upShowInfo == 0:
            self.editScreen.configure(state=DISABLED)
            self.attachInfo.configure(state=DISABLED)
            self.showTitle.configure("Show not found")
        
        self.reShowDate.configure(text="Date: " + str(upShowInfo[1]))
        self.reShowTime.configure(text="Time: " + str(upShowInfo[2]))
        self.reShowFilm.configure(text="Film: " + str(upShowInfo[3]))
        self.editScreen.configure(state=NORMAL)
        self.attachInfo.configure(state=NORMAL)

    """Cameron Povey 21011010"""      
    def commit_change(self):
        screenId = self.editScreen.get()
        self.check_messages()
        
        updateCheck = self.controller.commit_change(screenId)
        if updateCheck == False:
            self.error = Label(self.updateFrame, text="ERROR: SCREEN DOES NOT EXIST", font=("Arial", 25), fg="RED")
            self.error.pack()
            self.errorMessage = True
        else:
            self.success = Label(self.updateFrame, text="SUCCESS!", font=("Arial", 25), fg="Green")
            self.success.pack()
            self.successMessage = True
    
    """Sude Fidan 21068639"""
    def set_controller(self, controller):
        self.controller = controller

    
