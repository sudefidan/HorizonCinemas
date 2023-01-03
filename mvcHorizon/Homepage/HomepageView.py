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
        #only admin access
        #TODO: if self.controller.showOtherBooking: --ADD OTHER CINEMAS FOR ADMIN TO BE AVAILABLE FOR BOOKING

        #Options set
        self.filmlist = self.controller.get_films()
        filmoption = StringVar()
        filmoption.set(self.filmlist[0])

        
        self.showoption = StringVar()
        showlist = ["--SELECT SHOW TIME--"]
        self.showoption.set(showlist[0])

        #TITLE BLOCK
        titlecon = Frame(self.frame2, pady=2, padx=2)
        #current time
        Label(titlecon, text=datetime.now().strftime("%H:%M"), padx=25, pady=25).pack(fill=BOTH, side=LEFT, expand=True)
        #title
        Label(titlecon, text="H.C. Booking", font=('Arial', 50) ,pady=25,width=100).pack(fill=BOTH, side=RIGHT, expand=True)
        logcon = Frame(titlecon, padx=25,pady=25,width=25)

        #TODO: Check if these packs can be done JUST AFTER their assignment
        logcon.pack(fill=Y, side=RIGHT, expand=True)
        titlecon.pack(fill=BOTH, side=TOP, expand=False)

        #container for first part booking system (selecting seats, film, amount, date, type)
        containerig1 = Frame(self.frame2, height=200, bg="white", padx=0,pady=0)

        #LINE 1: FILM & DATE
        line1 = Frame(master= containerig1, height=200, width=200, bg="white")
        #film
        filmFrame = Frame(master=line1, bg="cyan", width=200, padx=5, pady=5)
        Label(master=filmFrame, text="Select Film",  bg="cyan", font=("Arial", 25)).pack(fill=Y)
        OptionMenu(filmFrame, filmoption, *self.filmlist, command=self.upshow).pack(fill=Y)
        #date
        dateFrame = Frame(master=line1,bg="cyan", width=200, padx=5,pady=5)
        Label(master=dateFrame, text="Select Date -null", bg="cyan", font=("Arial", 25)).pack(fill=Y)
        self.dates = DateEntry(master=dateFrame, background="blue")
        self.dates.pack(fill=Y)
        Button(master=dateFrame, background="blue", command=lambda: self.upshow(filmoption.get()), text="confirm").pack(fill=BOTH, side=LEFT, expand=True)


        #TODO: Check if these packs can be done JUST AFTER their assignment
        filmFrame.pack(fill=BOTH, side=LEFT, expand=True)
        dateFrame.pack(fill=BOTH, side=LEFT, expand=True)
        
        #LINE2 SHOWING & TICKET TYPES
        line2 = Frame(master=containerig1, height=200, width=200, bg="black")
        #showing
        showFrame = Frame(line2, bg="cyan", width=200, padx=5, pady=5)
        Label(showFrame, text="Select Film Showing", bg="cyan", font=("Arial", 25), fg='#ffffff').pack(fill=Y)
        self.showOptions = OptionMenu(showFrame, self.showoption, *showlist, command=self.uptype)
        self.showOptions.pack(fill=Y)
        #ticket types
        typeFrame = Frame(line2, bg="cyan", width=200, padx=5, pady=5)
        self.typeLabel = Label(typeFrame, text="Select Ticket Type", bg="cyan", font=("Arial", 25), fg='#ffffff')
        self.typeLabel.pack(fill=Y)
        allTypesFrame = Frame(typeFrame, width=200, bg='cyan')
        ticktype = StringVar(allTypesFrame, "low")
        self.lowerhall= Radiobutton(allTypesFrame, variable=ticktype, text="Lower", value="low", command=lambda: self.upamout(0))
        self.lowerhall.pack(fill=X, side=LEFT, expand=True)
        self.upperhall = Radiobutton(allTypesFrame, variable=ticktype, text="Upper", value="up", command=lambda: self.upamout(1))
        self.upperhall.pack(fill=X, side=LEFT, expand=True)
        self.vip = Radiobutton(allTypesFrame, variable=ticktype, text="VIP", value="vip", command=lambda: self.upamout(2))
        self.vip.pack(fill=X, side=LEFT, expand=True)
        
        #TODO: Check if these packs can be done JUST AFTER their assignment
        typeFrame.pack(fill=BOTH, side=LEFT, expand=True)
        allTypesFrame.pack(fill=BOTH, expand=True)
        showFrame.pack(fill=BOTH, side=LEFT, expand=True)
    
        #LINE3 TICKET NUMBERS & CHECK AVALIBILITY
        line3 = Frame(master=containerig1,width=200, height=200, bg="green")
        #ticket numbers
        numberFrame = Frame(line3, bg="cyan", width=200, padx=5, pady=5)
        self.ticketAmountLabel = Label(numberFrame, text="Select Ticket Amount",  bg="cyan", font=("Arial", 25))
        self.ticketAmountLabel.pack(fill=Y)
        self.numberSpinbox = Spinbox(numberFrame, from_=1, to=9,command=lambda: self.rescheck())
        self.numberSpinbox.pack(fill=Y)
        #check availability
        checkAvailabilityFrame = Frame(line3, bg="cyan", width=200, padx=5, pady=5)
        self.checkAvailability = Button(checkAvailabilityFrame ,text="Check Avalibility",padx=5, pady=5, bg="cyan", command= lambda: self.calculate_cost())
        self.checkAvailability .pack(fill=BOTH, expand=True)

        #TODO: Check if these packs can be done JUST AFTER their assignment
        numberFrame.pack(fill=BOTH, side=LEFT, expand=True)
        checkAvailabilityFrame.pack(fill=BOTH, side=LEFT, expand=True)
        #PACK LINES
        line1.pack(fill=BOTH, side=TOP, expand=True)
        line2.pack(fill=BOTH, side=TOP, expand=True)
        line3.pack(fill=BOTH, side=TOP, expand=True)
        containerig1.pack(fill=X, side=TOP, expand=False)


        #total cost
        #info = Frame(self.frame2, width=200)
        self.costTitle = Label(self.frame2, text="£~COST~", font=('Arial', 25), padx=25, pady=25)
        self.costTitle.pack(fill=BOTH, expand=False)
        self.error = Label(self.frame2,text="Enter customer info:", font=('Arial', 25), padx=5, pady=5)
        self.error.pack(fill=BOTH, expand=False)
        Label(self.frame2,text="Enter customer info:", font=('Arial', 25), padx=5, pady=5).pack(fill=BOTH, expand=False)


        #CREATE SECTION2 #-----------------
        containerig2 = Frame(self.frame2, height=200,bg="cyan")

        #LINE 1: NAME & PHONE
        containerig2Line1 = Frame(master=containerig2, height=200, width=200, bg="cyan")
        #first and last name
        nameFrame = Frame(master=containerig2Line1, bg="cyan", width=200, padx=5, pady=5)
        Label(master=nameFrame, text="First and Last Name", bg="cyan", fg='#ffffff', font=("Arial", 25)).pack(fill=X)
        self.firstName = Entry(master=nameFrame)
        self.firstName.pack(fill=X, side=LEFT, expand=True)
        self.lastName = Entry(master=nameFrame)
        self.lastName.pack(fill=X, side=LEFT, expand=True)
        #phone nuber
        phoneFrame = Frame(master=containerig2Line1, bg="cyan", width=200, padx=10, pady=10)
        Label(master=phoneFrame, text="Phone", bg="cyan", fg='#ffffff',font=("Arial", 25))
        self.phone = Entry(master=phoneFrame)
        self.phone.pack(fill=Y)

        #TODO: Check if these packs can be done JUST AFTER their assignment
        nameFrame.pack(fill=BOTH, side=LEFT, expand=True)
        phoneFrame.pack(fill=BOTH, side=LEFT, expand=True)

        #LINE 2: EMAIL & CARDNO
        containerig2Line2 = Frame(master=containerig2, height=200, width=100, bg="white")
        #email
        emailFrame= Frame(master=containerig2Line2, bg="cyan", width=200, padx=5, pady=5)
        Label(master=emailFrame, text="Email", bg="cyan", fg='#ffffff', font=("Arial", 25)).pack(fill=Y)
        self.emails = Entry(master=emailFrame)
        self.emails.pack(fill=Y)
        #card details
        cardFrame = Frame(master=containerig2Line2, bg="cyan", width=200, padx=5, pady=5)
        Label(master=cardFrame, text="Card", bg="cyan", fg='#ffffff', font=("Arial", 25)).pack(fill=Y)
        self.cardNumber = Entry(master=cardFrame)
        self.cardNumber.pack(fill=Y)

        #TODO: Check if these packs can be done JUST AFTER their assignment 
        emailFrame.pack(fill=BOTH, side=LEFT, expand=True)
        cardFrame.pack(fill=BOTH, side=LEFT, expand=True)
        containerig2Line1.pack(fill=BOTH, side=TOP,expand=True)
        containerig2Line2.pack(fill=BOTH, side=TOP,expand=True)
        containerig2 .pack(fill=BOTH, expand=True)



        #LINE 3: EXPIRY DATE & CVV
        containerig2Line3 = Frame(master= containerig2, height=200, width=100, bg="white")
        #expirty date
        expiryFrame = Frame(master=containerig2Line3,bg="cyan", width=200, padx=5,pady=5)
        Label(master=expiryFrame, text="Expiry Date", bg="cyan", fg='#ffffff', font=("Arial", 25)).pack(fill=Y)
        self.expiryDate = DateEntry(master=expiryFrame, background="blue")
        self.expiryDate.pack(fill=Y)
        #cvv code
        cvvFrame = Frame(master=containerig2Line3, bg="cyan", width=200, padx=5, pady=5)
        Label(master=cvvFrame, text="CVV", bg="cyan", fg='#ffffff',font=("Arial", 25)).pack(fill=Y)
        self.cvv = Entry(master=cvvFrame)
        self.cvv.pack(fill=Y)

        #TODO: Check if these packs can be done JUST AFTER their assignment / why two times?
        expiryFrame.pack(fill=BOTH, side=LEFT, expand=True)
        cvvFrame.pack(fill=BOTH, side=LEFT, expand=True)
        containerig2Line1.pack(fill=BOTH, side=TOP,expand=True)
        containerig2Line2.pack(fill=BOTH, side=TOP,expand=True)
        containerig2Line3.pack(fill=BOTH, side=TOP,expand=True)
        containerig2 .pack(fill=BOTH, expand=True)
        


        #FOOTER (CANCEL & BOOKING)
        foot = Frame(self.frame2,pady=10, padx=10)
        #cancel button
        Button(foot, text="CANCEL", command=self.show_make_cancellation, font=('Arial', 25), padx=5, pady=5, bg='grey').pack(fill=BOTH, side=TOP, expand=True)
        #booking button
        self.bookButton = Button(foot, text="BOOK", font=('Arial', 25), padx=5, pady=5, bg='red', state=DISABLED, command=lambda: self.booking())
        self.bookButton.pack(fill=BOTH, side=TOP, expand=True)

        #TODO: Check if these packs can be done JUST AFTER their assignment
        foot.pack(fill=BOTH, side=TOP ,expand=True)
        
        #UPDATES
        self.upshow(self.filmlist[0])

    
    """Sude Fidan 21068639"""
    def show_make_cancellation(self):
        self.notebook.select(tab_id=2)

    #Update 'showings' panel 
    def upshow(self, film):
        print(film)
        self.seldate = self.dates.get_date().strftime("%d/%m/%Y")
        print(self.seldate,"-----",type(self.seldate))
        self.showlist = self.controller.showlist(film,self.seldate)
        self.showOptions["menu"].delete(0, "end")
        for showings in self.showlist:
            self.showOptions["menu"].add_command(label=showings, command=lambda value=showings: [self.showoption.set(value),self.uptype()])
            print(showings)
        self.showoption.set("SELECT SHOW TIME")
        print(self.showlist)
        self.uptype()
        self.rescheck()

    #Check seat avalibilites
    def uptype(self):
        count = 0
        self.point = [self.lowerhall, self.upperhall, self.vip]
        time = self.showoption.get()
        self.typeleft = self.controller.checktypes(time)
        self.reset()
        self.resam()
        if self.typeleft == None: return 0
        for i in range (len(self.typeleft)):
            if self.typeleft[i] == 0:
                (self.point[i]).deselect()
                (self.point[i]).configure(state = DISABLED)
                count+=1
            if count == 3:
                self.typeLabel.configure(text="SOLD OUT", fg='#FF0000')
                self.checkAvailability.configure(state=DISABLED)
        self.rescheck()
    
        
    #Count avalible seats
    def upamout(self, iden):
        self.typesel = iden
        self.resam()
        self.rescheck()
        print(self.typeleft)
        if self.typeleft == None: return 0
        if self.typeleft[iden] < 9:
            self.ticketAmountLabel.configure(text="Select Ticket Amount - LIMITED", fg='#FF0000')
            self.numberSpinbox.configure(to=self.typeleft[iden])
        
        
    def calculate_cost(self):
        self.cost = (self.controller.cost(self.typesel, self.numberSpinbox.get()))
        if self.cost == None: return 0
        self.checkAvailability.configure(state=DISABLED)
        self.bookButton.configure(state=NORMAL)
        self.costTitle.configure(text=("£",(round(self.cost, 2))))
        
    
    def booking(self):
        self.eminput = self.emails.get()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        print(self.expiryDate.get())
        self.expdate = datetime.strptime(self.expiryDate.get(), "%d/%m/%Y")
        
        if self.expdate < datetime.today(): self.bonotfil(0)
        elif len(self.firstName.get()) == 0:
            self.bonotfil(1)
        elif len(self.phone.get()) != 11 and len(self.phone.get()) != 13:
            print(len(self.phone.get()))
            self.bonotfil(2)
        elif len(self.cardNumber.get()) != 16:
            self.bonotfil(3)
        elif len(self.cvv.get()) != 3:
            self.bonotfil(4)
        elif len(self.lastName.get()) == 0:
            self.bonotfil(5)
        """
        elif(re.fullmatch(regex, self.eminput)):
            self.validated()
            return 0
        else:
            self.bonotfil(6)
            
        #DOESNT GO ANYWHERE"""
    
    
    #UPDATE PARTS
    def validated(self):
        self.error.configure(text="CUSTOMER INFORMATION VALIDATED", fg='#00FF00')
        bookreturn = self.controller.bookfilm(self.firstName.get(), self.lastName.get(), self.phone.get(), self.emails.get(), self.cardNumber.get(), self.expdate, self.cvv.get())
        if bookreturn == 'taken':
            print("SHIT")
    
    def bonotfil(self, errorno):
        if errorno == 0: self.error.configure(text="Please enter a valid expiry date", fg='#FF0000')
        elif errorno == 1: self.error.configure(text="Please enter a valid first name", fg='#FF0000#')
        elif errorno == 2: self.error.configure(text="Please enter a valid phone number", fg='#FF0000')
        elif errorno == 3: self.error.configure(text="Please enter a valid card number", fg='#FF0000')
        elif errorno == 4: self.error.configure(text="Please enter a valid cvv", fg='#FF0000')
        elif errorno == 5: self.error.configure(text="Please enter a valid last name", fg='#FF0000')
        elif errorno == 6: self.error.configure(text="Please enter a valid email", fg='#FF0000')
    
    def rescheck(self):
        self.checkAvailability .configure(state=NORMAL)
        self.costTitle.configure(text="PRESS CHECK FOR COST")
        self.bookButton.configure(state=DISABLED)
    
    def resam(self):
        self.ticketAmountLabel.configure(text="Select Ticket Amount", fg='#000000')
        self.numberSpinbox.configure(to=9)
                
    def reset(self):
        self.typeLabel.configure(text="Select Ticket Type", fg='#000000')
        for i in range (3):
            (self.point[i]).configure(state = ACTIVE)
            if i == 0: (self.point[i]).select()
            else: (self.point[i]).deselect()
        
        


        

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