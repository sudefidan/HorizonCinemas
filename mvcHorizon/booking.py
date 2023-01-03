import tkinter as tk
from datetime import datetime
from tkcalendar import *

class Model():
    def __init__(self):
        pass
    

class View():
    def __init__(self, parent):
        self.parent = parent
        
        #Options set
        self.filmlist = getfilms()
        self.filmoption = tk.StringVar()
        self.filmoption.set(self.filmlist[0])
        
        self.showoption = tk.StringVar()
        self.showlist = ["--SELECT SHOW TIME--"]
        self.showoption.set(self.showlist[0])
        
        #ACUTAL UI
        #TITLE BLOCK
        self.titlecon = tk.Frame(self.parent, pady=2, padx=2)

        self.time = tk.Label(self.titlecon, text="~TIME~", padx=25, pady=25)
        self.title = tk.Label(self.titlecon, text="H.C. Booking", font=('Arial', 50) ,pady=25,width=100)
        self.logcon = tk.Frame(self.titlecon, padx=25,pady=25,width=25)

        self.location = tk.Label(self.logcon, text="~LOCATION~")
        self.staff = tk.Label(self.logcon, text="~STAFF MEMBER~")
        self.location.pack(fill=tk.Y, side=tk.TOP, expand=True)
        self.staff.pack(fill=tk.Y, side=tk.TOP, expand=True)

        self.time.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.logcon.pack(fill=tk.Y, side=tk.RIGHT, expand=True)
        self.title.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

        self.titlecon.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        #container for first part booking system (selecting seats, film, amount, date, type)
        self.containerig = tk.Frame(self.parent, height=200, bg="white", padx=0,pady=0)

        #LINE 1 FILM & DATE
        self.line1 = tk.Frame(master=self.containerig, height=200, width=200, bg="white")

        self.film = tk.Frame(master=self.line1, bg="red", width=200, padx=5, pady=5)
        self.filmt = tk.Label(master=self.film, text="Select Film", background="red", font=("Arial", 25))
        self.films = tk.OptionMenu(self.film, self.filmoption, *self.filmlist, command=self.upshow)
        self.filmt.pack(fill=tk.Y)
        self.films.pack(fill=tk.Y)

        self.date = tk.Frame(master=self.line1,bg="blue", width=200, padx=5,pady=5)
        self.datet = tk.Label(master=self.date, text="Select Date -null", background="blue", font=("Arial", 25))
        self.dates = DateEntry(master=self.date, background="blue")
        self.datet.pack(fill=tk.Y)
        self.dates.pack(fill=tk.Y)

        self.film.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.date.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        #LINE2 SHOWING & TICKET TYPES
        self.line2 = tk.Frame(master=self.containerig, height=200, width=200, bg="black")

        self.showing = tk.Frame(self.line2, bg="purple", width=200, padx=5, pady=5)
        self.showt = tk.Label(self.showing, text="Select Film Showing", background="purple", font=("Arial", 25))
        self.shows = tk.OptionMenu(self.showing, self.showoption, *self.showlist)
        self.showt.pack(fill=tk.Y)
        self.shows.pack(fill=tk.Y)


        self.type = tk.Frame(self.line2, bg="Grey", width=200, padx=5, pady=5)
        self.typet = tk.Label(self.type, text="Select Ticket Type", background="grey", font=("Arial", 25))
        
        self.types = tk.Frame(self.type, width=200, bg="Red")
        
        self.ticktype = tk.StringVar(self.types, "low")
        self.lowcheck = tk.Radiobutton(self.types, variable=self.ticktype, text="Lower", value="low")
        self.upcheck = tk.Radiobutton(self.types, variable=self.ticktype, text="Upper", value="up")
        self.vipcheck = tk.Radiobutton(self.types, variable=self.ticktype, text="VIP", value="vip")
        
        self.lowcheck.pack(fill=tk.X, side=tk.LEFT, expand=True)
        self.upcheck.pack(fill=tk.X, side=tk.LEFT, expand=True)
        self.vipcheck.pack(fill=tk.X, side=tk.LEFT, expand=True)
        
        self.typet.pack(fill=tk.Y)
        self.types.pack(fill=tk.BOTH, expand=True)

        self.showing.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.type.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        #LINE3 TICKET NUMBERS & CHECK AVALIBILITY
        self.line3 = tk.Frame(master=self.containerig,width=200, height=200, bg="green")

        self.numb = tk.Frame(self.line3, bg="orange", width=200, padx=5, pady=5)
        self.numbt = tk.Label(self.numb, text="Select Ticket Amount", background="orange", font=("Arial", 25))
        self.numbs = tk.Spinbox(self.numb, from_=1, to=9)
        self.numbt.pack(fill=tk.Y)
        self.numbs.pack(fill=tk.Y)

        self.check = tk.Frame(self.line3, bg="green", width=200, padx=5, pady=5)
        self.checkb = tk.Button(self.check ,text="Check Avalibility",padx=5, pady=5, bg="green", command= lambda: self.calculate_cost(self.filmoption.get(), self.ticktype.get(), self.numbs.get()))
        self.checkb.pack(fill=tk.BOTH, expand=True)

        self.numb.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.check.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


        #PACK LINES
        self.line1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.line2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.line3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.containerig.pack(fill=tk.X, side=tk.TOP, expand=False)

        #info = tk.Frame(self.parent, width=200)
        self.tit2 = tk.Label(self.parent, text="£~COST~", font=('Arial', 25), padx=25, pady=25)
        self.tit2.pack(fill=tk.BOTH, expand=False)


        #CREATE SECTION2 #-----------------
        self.con2 = tk.Frame(self.parent, height=200,bg="Black")

        #LINE 1 NAME & PHONE
        self.c2line1 = tk.Frame(master=self.con2, height=200, width=200, bg="white")

        self.name = tk.Frame(master=self.c2line1, bg="red", width=200, padx=5, pady=5)
        self.namet = tk.Label(master=self.name, text="Name", background="red", font=("Arial", 25))
        self.names = tk.Entry(master=self.name)
        self.namet.pack(fill=tk.Y)
        self.names.pack(fill=tk.Y)

        self.phone = tk.Frame(master=self.c2line1, bg="blue", width=200, padx=10, pady=10)
        self.phonet = tk.Label(master=self.phone, text="Phone", background="blue", font=("Arial", 25))
        self.phones = tk.Entry(master=self.phone)
        self.phonet.pack(fill=tk.Y)
        self.phones.pack(fill=tk.Y)

        self.name.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.phone.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        #LINE 2 EMAIL & CARDNO
        self.c2line2 = tk.Frame(master=self.con2, height=200, width=100, bg="white")

        self.email = tk.Frame(master=self.c2line2, bg="green", width=200, padx=5, pady=5)
        self.emailt = tk.Label(master=self.email, text="Email", background="green", font=("Arial", 25))
        self.emails = tk.Entry(master=self.email)
        self.emailt.pack(fill=tk.Y)
        self.emails.pack(fill=tk.Y)

        self.card = tk.Frame(master=self.c2line2, bg="orange", width=200, padx=5, pady=5)
        self.cardt = tk.Label(master=self.card, text="Card", background="orange", font=("Arial", 25))
        self.cards = tk.Entry(master=self.card)
        self.cardt.pack(fill=tk.Y)
        self.cards.pack(fill=tk.Y)

        self.email.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.card.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.c2line1.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
        self.c2line2.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
        self.con2.pack(fill=tk.BOTH, expand=True)

        #LINE 3 EXPIRY DATE & CVV
        self.c2line3 = tk.Frame(master=self.con2, height=200, width=100, bg="white")

        self.exp = tk.Frame(master=self.c2line3,bg="purple", width=200, padx=5,pady=5)
        self.expt = tk.Label(master=self.exp, text="Expiry Date", background="purple", font=("Arial", 25))
        self.exps = DateEntry(master=self.exp, background="blue")
        self.expt.pack(fill=tk.Y)
        self.exps.pack(fill=tk.Y)

        self.cvv = tk.Frame(master=self.c2line3, bg="pink", width=200, padx=5, pady=5)
        self.cvvt = tk.Label(master=self.cvv, text="CVV", background="pink", font=("Arial", 25))
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

        self.cancel = tk.Button(self.foot, text="CANCEL", font=('Arial', 25), padx=5, pady=5, bg='grey')
        self.book = tk.Button(self.foot, text="BOOK", font=('Arial', 25), padx=5, pady=5, bg='red')

        self.cancel.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.book.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.foot.pack(fill=tk.BOTH, side=tk.TOP ,expand=True)
        
        #UPDATES
        self.upshow(self.filmlist[0])
        self.uptime()
        
    def uptime(self):
        now = datetime.now().strftime('%H:%M')
        self.time.configure(text=now)
        self.parent.after(1000, self.uptime)
        
    #Update 'showings' panel
    def upshow(self, film):
        self.showlist = getshowings(film)
        self.shows["menu"].delete(0, "end")
        for showings in self.showlist:
            self.shows["menu"].add_command(label=showings, command=lambda value=showings:self.showoption.set(value))
        self.showoption.set("SELECT SHOW TIME")
        self.uptype(film)
        
        print(self.showlist)
        
    def uptype(self, film):
        types = gettypes(film)
        self.maxlower = types[0]
        self.maxupper = types[1]
        self.maxvip = types[2]
        
    def calculate_cost(self, film, type, amount):
        cost(film, type, amount)

class App(tk.TK):
    def __init__(self):
        super().__init__()
        
        self.titel("HC Staff Booking")
        
        model = Model(self)
        
        view = View(self)

root = tk.Tk()
root.geometry('1000x1000')
view(root)

root.mainloop()