import tkinter as tk
from datetime import datetime
from tkcalendar import *
import re

class View():
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.typesel = 0
        
        #Options set
        self.filmlist = controller.getfilms()
        self.filmoption = tk.StringVar()
        self.filmoption.set(self.filmlist[0])
        
        self.showoption = tk.StringVar()
        self.showlist = ["--SELECT SHOW TIME--"]
        self.showoption.set(self.showlist[0])
        
        #ACUTAL UI
        #HEADER BLOCK
        self.titlecon = tk.Frame(self.parent, pady=2, padx=2)

        self.time = tk.Label(self.titlecon, text="~TIME~", padx=25, pady=25)
        self.title = tk.Label(self.titlecon, text="H.C. Booking", font=('Arial', 50) ,pady=25,width=100)
        self.logcon = tk.Frame(self.titlecon, padx=25,pady=25,width=25)

        self.location = tk.Label(self.logcon, text="~LOCATION~")
        self.staff = tk.Label(self.logcon, text="~STAFF MEMBER~")
        self.staff.pack(fill=tk.Y, side=tk.TOP, expand=True)
        self.location.pack(fill=tk.Y, side=tk.TOP, expand=True)

        self.time.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.logcon.pack(fill=tk.Y, side=tk.RIGHT, expand=True)
        self.title.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

        self.titlecon.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
        self.getinfo()
        #container for first part booking system (selecting seats, film, amount, date, type)
        self.containerig = tk.Frame(self.parent, height=200, bg="white", padx=0,pady=0)

        #LINE 1 FILM & DATE
        self.line1 = tk.Frame(master=self.containerig, height=200, width=200, bg="white")

        self.film = tk.Frame(master=self.line1, bg="cyan", width=200, padx=5, pady=5)
        self.filmt = tk.Label(master=self.film, text="Select Film", bg="cyan", font=("Arial", 25), fg='black')
        self.films = tk.OptionMenu(self.film, self.filmoption, *self.filmlist, command=self.upshow)
        self.filmt.pack(fill=tk.Y)
        self.films.pack(fill=tk.Y)

        self.date = tk.Frame(master=self.line1,bg="cyan", width=200, padx=50,pady=5)
        self.datet = tk.Label(master=self.date, text="Select Date -null", bg="cyan", font=("Arial", 25), fg='black')
        self.dates = DateEntry(master=self.date, background="blue")
        self.dateconfirm = tk.Button(master=self.date, background="blue", command=lambda: self.upshow(self.filmoption.get()), text="confirm")
        self.datet.pack(fill=tk.Y)
        self.dates.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.dateconfirm.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.film.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.date.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        #LINE2 SHOWING & TICKET TYPES
        self.line2 = tk.Frame(master=self.containerig, height=200, width=200, bg="black")

        self.showing = tk.Frame(self.line2, bg="cyan", width=200, padx=5, pady=5)
        self.showt = tk.Label(self.showing, text="Select Film Showing", bg="cyan", font=("Arial", 25), fg='black')
        self.shows = tk.OptionMenu(self.showing, self.showoption, *self.showlist, command=self.uptype)
        self.showt.pack(fill=tk.Y)
        self.shows.pack(fill=tk.Y)


        self.type = tk.Frame(self.line2, bg="cyan", width=200, padx=5, pady=5)
        self.typet = tk.Label(self.type, text="Select Ticket Type", bg="cyan", font=("Arial", 25), fg='black')
        
        self.types = tk.Frame(self.type, width=200, bg='cyan')
        
        self.ticktype = tk.StringVar(self.types, "low")
        self.lowcheck = tk.Radiobutton(self.types, variable=self.ticktype, text="Lower", value="low", command=lambda: self.upamout(0))
        self.upcheck = tk.Radiobutton(self.types, variable=self.ticktype, text="Upper", value="up", command=lambda: self.upamout(1))
        self.vipcheck = tk.Radiobutton(self.types, variable=self.ticktype, text="VIP", value="vip", command=lambda: self.upamout(2))
        
        self.lowcheck.pack(fill=tk.X, side=tk.LEFT, expand=True)
        self.upcheck.pack(fill=tk.X, side=tk.LEFT, expand=True)
        self.vipcheck.pack(fill=tk.X, side=tk.LEFT, expand=True)
        
        self.typet.pack(fill=tk.Y)
        self.types.pack(fill=tk.BOTH, expand=True)

        self.showing.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.type.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        #LINE3 TICKET NUMBERS & CHECK AVALIBILITY
        self.line3 = tk.Frame(master=self.containerig,width=200, height=200, bg="green")

        self.numb = tk.Frame(self.line3, bg="cyan", width=200, padx=5, pady=5)
        self.numbt = tk.Label(self.numb, text="Select Ticket Amount", bg="cyan", font=("Arial", 25), fg='black')
        self.numbs = tk.Spinbox(self.numb, from_=1, to=9, command=lambda: self.rescheck())
        self.numbt.pack(fill=tk.Y)
        self.numbs.pack(fill=tk.Y)

        self.check = tk.Frame(self.line3, bg="cyan", width=200, padx=5, pady=5)
        self.checkb = tk.Button(self.check ,text="Check Avalibility",padx=5, pady=5, bg="cyan", command=lambda: self.calculate_cost())
        self.checkb.pack(fill=tk.BOTH, expand=True)

        self.numb.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.check.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


        #PACK LINES
        self.line1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.line2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.line3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.containerig.pack(fill=tk.X, side=tk.TOP, expand=False)

        #info = tk.Frame(self.parent, width=200)
        self.tit2 = tk.Label(self.parent, text="£~COST~", font=('Arial', 25), padx=25, pady=10)
        self.error = tk.Label(self.parent,text="Enter customer info:", font=('Arial', 25), padx=5, pady=5)
        self.tit2.pack(fill=tk.BOTH, expand=False)
        self.error.pack(fill=tk.BOTH, expand=False)


        #CREATE SECTION2 #-----------------
        self.con2 = tk.Frame(self.parent, height=200, bg="cyan")

        #LINE 1 NAME & PHONE
        self.c2line1 = tk.Frame(master=self.con2, height=200, width=200, bg="cyan")

        self.name = tk.Frame(master=self.c2line1, bg="cyan", width=200, padx=100, pady=5)
        self.nameidlast = tk.Label(master=self.name, text="First and Last Names", bg="cyan", font=("Arial", 25), fg='black')
        self.names = tk.Entry(master=self.name)
        self.namelast = tk.Entry(master=self.name)
        self.nameidlast.pack(fill=tk.X)
        self.names.pack(fill=tk.X, side=tk.LEFT, expand=True)
        self.namelast.pack(fill=tk.X, side=tk.LEFT, expand=True)

        self.phone = tk.Frame(master=self.c2line1, bg="cyan", width=200, padx=50, pady=10)
        self.phonet = tk.Label(master=self.phone, text="Phone", bg="cyan", font=("Arial", 25), fg='black')
        self.phones = tk.Entry(master=self.phone)
        self.phonet.pack(fill=tk.Y)
        self.phones.pack(fill=tk.X, expand=True)

        self.name.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.phone.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        #LINE 2 EMAIL & CARDNO
        self.c2line2 = tk.Frame(master=self.con2, height=200, width=100, bg="white")

        self.email = tk.Frame(master=self.c2line2, bg="cyan", width=200, padx=5, pady=5)
        self.emailt = tk.Label(master=self.email, text="Email", bg="cyan", font=("Arial", 25), fg='black')
        self.emails = tk.Entry(master=self.email)
        self.emailt.pack(fill=tk.Y)
        self.emails.pack(fill=tk.Y)

        self.card = tk.Frame(master=self.c2line2, bg="cyan", width=200, padx=5, pady=5)
        self.cardt = tk.Label(master=self.card, text="Card", bg="cyan", font=("Arial", 25), fg='black')
        self.cards = tk.Entry(master=self.card)
        self.cardt.pack(fill=tk.Y)
        self.cards.pack(fill=tk.Y)

        self.email.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, )
        self.card.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.c2line1.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
        self.c2line2.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
        self.con2.pack(fill=tk.BOTH, expand=True)

        #LINE 3 EXPIRY DATE & CVV
        self.c2line3 = tk.Frame(master=self.con2, height=200, width=100, bg="cyan")

        self.exp = tk.Frame(master=self.c2line3, bg="cyan", width=200, padx=5,pady=5)
        self.expt = tk.Label(master=self.exp, text="Expiry Date", bg="cyan", font=("Arial", 25), fg='black')
        self.exps = DateEntry(master=self.exp, bg="cyan")
        self.expt.pack(fill=tk.Y)
        self.exps.pack(fill=tk.Y)

        self.cvv = tk.Frame(master=self.c2line3, bg="cyan", width=200, padx=5, pady=5)
        self.cvvt = tk.Label(master=self.cvv, text="CVV", bg="cyan", font=("Arial", 25), fg='black')
        self.cvvs = tk.Entry(master=self.cvv)
        self.cvvt.pack(fill=tk.Y)
        self.cvvs.pack(fill=tk.Y)

        self.exp.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.cvv.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.c2line1.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
        self.c2line2.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
        self.c2line3.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
        self.con2.pack(fill=tk.BOTH, expand=False)

        #FOOTER (CANCEL & BOOKING)
        self.foot = tk.Frame(self.parent,pady=10, padx=10)

        self.cancel = tk.Button(self.foot, text="CANCEL", font=('Arial', 25), padx=5, pady=5, bg='grey') #LINK TO CANCEL
        self.book = tk.Button(self.foot, text="BOOK", font=('Arial', 25), padx=5, pady=5, bg='red', state=tk.DISABLED, command=lambda: self.booking())

        self.cancel.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.book.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.foot.pack(fill=tk.BOTH, side=tk.TOP ,expand=True)
        
        #UPDATES
        self.upshow(self.filmlist[0]) 
        self.uptime()
        
        #UPDATES
        #self.showlist = controller.showlist(self.filmlist[0])
        #controller.upshow
        
    def uptime(self):
        now = datetime.now().strftime('%H:%M')
        self.time.configure(text=now)
        self.parent.after(1000, self.uptime)
        
    #Update 'showings' panel 
    def upshow(self, film):
        print(film)
        self.seldate = self.dates.get_date().strftime("%d/%m/%Y")
        print(self.seldate,"-----",type(self.seldate))
        self.showlist = self.controller.showlist(film,self.seldate)
        self.shows["menu"].delete(0, "end")
        for showings in self.showlist:
            self.shows["menu"].add_command(label=showings, command=lambda value=showings: [self.showoption.set(value),self.uptype()])
            print(showings)
        self.showoption.set("SELECT SHOW TIME")
        print(self.showlist)
        self.uptype()
        self.rescheck()
    
    #Check seat avalibilites
    def uptype(self):
        count = 0
        self.point = [self.lowcheck, self.upcheck, self.vipcheck]
        time = self.showoption.get()
        self.typeleft = self.controller.checktypes(time)
        self.reset()
        self.resam()
        if self.typeleft == None: return 0
        for i in range (len(self.typeleft)):
            if self.typeleft[i] == 0:
                (self.point[i]).deselect()
                (self.point[i]).configure(state = tk.DISABLED)
                count+=1
            if count == 3:
                self.typet.configure(text="SOLD OUT", fg='Red')
                self.checkb.configure(state=tk.DISABLED)
        self.rescheck()
            
    #Count avalible seats
    def upamout(self, iden):
        self.typesel = iden
        self.resam()
        self.rescheck()
        print(self.typeleft)
        if self.typeleft == None: return 0
        if self.typeleft[iden] < 9:
            self.numbt.configure(text="Select Ticket Amount - LIMITED", fg='RED')
            self.numbs.configure(to=self.typeleft[iden])
        
            
    def calculate_cost(self):
        self.cost = (self.controller.cost(self.typesel, self.numbs.get()))
        if self.cost == None: return 0
        self.checkb.configure(state=tk.DISABLED)
        self.book.configure(state=tk.NORMAL)
        self.tit2.configure(text=("£",(round(self.cost, 2))))
        
    
    def booking(self):
        self.eminput = self.emails.get()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        print(self.exps.get())
        self.expdate = datetime.strptime(self.exps.get(), "%d/%m/%Y")
        
        if self.expdate < datetime.today(): self.bonotfil(0)
        elif len(self.names.get()) == 0:
            self.bonotfil(1)
        elif len(self.phones.get()) != 11 and len(self.phones.get()) != 13:
            print(len(self.phones.get()))
            self.bonotfil(2)
        elif len(self.cards.get()) != 16:
            self.bonotfil(3)
        elif len(self.cvvs.get()) != 3:
            self.bonotfil(4)
        elif len(self.namelast.get()) == 0:
            self.bonotfil(5)
        
        elif(re.fullmatch(regex, self.eminput)):
            self.validated()
            return 0
        else:
            self.bonotfil(6)
            
        #DOESNT GO ANYWHERE
    
    
    #UPDATE PARTS
    def validated(self):
        self.error.configure(text="CUSTOMER INFORMATION VALIDATED", fg='GREEN')
        bookreturn = self.controller.bookfilm(self.names.get(), self.namelast.get(), self.phones.get(), self.emails.get(), self.cards.get(), self.expdate, self.cvvs.get())
        if bookreturn == 'taken':
            print("SHIT")
    
    def bonotfil(self, errorno):
        if errorno == 0: self.error.configure(text="Please enter a valid expiry date", fg='RED')
        elif errorno == 1: self.error.configure(text="Please enter a valid first name", fg='RED')
        elif errorno == 2: self.error.configure(text="Please enter a valid phone number", fg='RED')
        elif errorno == 3: self.error.configure(text="Please enter a valid card number", fg='RED')
        elif errorno == 4: self.error.configure(text="Please enter a valid cvv", fg='RED')
        elif errorno == 5: self.error.configure(text="Please enter a valid last name", fg='RED')
        elif errorno == 6: self.error.configure(text="Please enter a valid email", fg='RED')
    
    def rescheck(self):
        self.checkb.configure(state=tk.NORMAL)
        self.tit2.configure(text="PRESS CHECK FOR COST")
        self.book.configure(state=tk.DISABLED)
    
    def resam(self):
        self.numbt.configure(text="Select Ticket Amount", fg='Black')
        self.numbs.configure(to=9)
                
    def reset(self):
        self.typet.configure(text="Select Ticket Type", fg='Black')
        for i in range (3):
            (self.point[i]).configure(state = tk.ACTIVE)
            if i == 0: (self.point[i]).select()
            else: (self.point[i]).deselect()
            
    def getinfo(self):
        info = []
        info = self.controller.topinfo()
        self.location.configure(text=info[0])
        self.staff.configure(text=info[1])