from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox 
import numpy as np
from ManageScreening.ManageScreeningController import ManageScreeningController
from ManageScreening.ManageScreeningModel import ManageScreeningModel
from ManageScreening.ManageScreeningView import ManageScreeningView
from GenerateReport.GenerateReportController import GenerateReportController
from GenerateReport.GenerateReportModel import GenerateReportModel
from GenerateReport.GenerateReportView import GenerateReportView
import re

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
        self.listings_view()
        self.booking_view()
        self.cancellation_view()
        #admin and manager access
        if self.controller.showManageScreening:
            self.manage_view()
        #admin and manager access
        if self.controller.showGenerateReport:
            self.report_view()
        #only manager access
        if self.controller.showAddCinema:
            self.new_cinema_view()
            
        #staff details 
        Label(self, text=self.controller.get_user(), width=30, height=5, fg= '#ffffff',font=("Arial",12,"bold")).place(relx = 1.0, rely = 0.0,anchor="ne")

        #logout button
        Button(self, text="Logout", width=10, height=1, command=self.logout_clicked, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM, anchor="e")

    """Fiorella Scarpino 21010043"""
    def listings_view(self):
        #listing frame
        self.listing = Frame(self.notebook, width=800, height=280)
        self.listing.pack(fill='both', expand=True)
        self.notebook.add(self.listing, text='Listings')
        #self.controller.listings()

        #proceed booking button
        Button(self.listing, text="Proceed Booking", width=10, height=1, command=self.show_make_booking, bg="#0E6655",font=("Arial",12,"bold")).pack(side=BOTTOM)
        
        #movie scrollbar
        scrollbar = Scrollbar(self.listing, orient="vertical")
        self.movieFrame=Listbox(self.listing,bg = "grey64",selectbackground="grey",activestyle = 'dotbox',yscrollcommand=scrollbar.set)
        self.movieFrame.pack(side=LEFT, fill='both', expand=True, anchor="n")
        scrollbar.config(command=self.movieFrame.yview)

        #insert movie names
        self.records = self.controller.get_films()
        for row in self.records:
            movieName=row[1]
            self.movieFrame.insert('end',movieName)

        #movie info scrollbar
        self.textOutput = Text(self.listing,bg = "grey64",wrap=WORD)   
        self.textOutput.pack(side=TOP, fill='both', expand=True, anchor="e")

        #correlate film selection to data from database        
        self.movieFrame.bind('<<ListboxSelect>>',self.get_selection)

        #show scrollbar
        columns = ('date', 'time', 'screenid')
        self.tree = ttk.Treeview(self.listing, columns=columns, show='headings')
        self.tree.pack(side=RIGHT, fill='both', expand=True, anchor="n")
        self.tree.heading('date', text='Date')
        self.tree.heading('time', text='Time')
        self.tree.heading('screenid', text='Screen')

    """Fiorella Scarpino 21010043"""
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
    def booking_view(self):
        #booking frame
        self.booking = Frame(self.notebook, width=800, height=280)
        self.booking.pack(fill='both', expand=True)
        self.notebook.add(self.booking, text='Make Booking')
        
        #Options set
        self.filmlist = self.controller.get_films_cinema()
        self.filmoption = StringVar()
        self.filmoption.set(self.filmlist[0])
        
        self.showoption = StringVar()
        self.showlist = ["--SELECT SHOW TIME--"]
        self.showoption.set(self.showlist[0])
        
        #screen
        Label(self.booking, text="Enter Booking Details", bg=None, font=("Arial", 25), fg='White', pady=2).pack(fill=X)
        
        line1 = Frame(self.booking, bg="white")
        line1.pack(fill=X)
        
        film = Frame(master=line1, bg="cyan", width=200, padx=5, pady=5)
        film.pack(fill=BOTH, side=LEFT, expand=True)
        self.filmt = Label(master=film, text="Select Film", bg="cyan", font=("Arial", 15), fg='black')
        self.films = OptionMenu(film, self.filmoption, *self.filmlist)
        self.filmt.pack(fill=Y)
        self.films.pack(fill=Y)
        
        date = Frame(master=line1,bg="cyan", width=200, padx=50,pady=5)
        date.pack()
        Label(master=date, text="Select Date", bg="cyan", font=("Arial", 15), fg='black').pack(fill=Y)
        self.dates = DateEntry(master=date, background="blue")
        self.dates.pack(fill=BOTH, side=LEFT, expand=True)
        Button(master=date, background="blue", command=lambda: self.update_shows(self.filmoption.get()), text="confirm").pack(fill=BOTH, side=LEFT, expand=True)
        
        line2 = Frame(self.booking, bg="white")
        line2.pack(fill=X)
        
        showing = Frame(line2, bg="cyan", width=200, padx=5, pady=5)
        showing.pack(fill=BOTH, side=LEFT, expand=True)
        Label(showing, text="Select Film Showing", bg="cyan", font=("Arial", 15), fg='black').pack(fill=Y)
        self.cpbook_shows = OptionMenu(showing, self.showoption, *self.showlist, command=lambda: self.update_type()) #uptype
        self.cpbook_shows.pack(fill=Y)
        
        type = Frame(line2, bg="cyan", width=200, padx=5, pady=5)
        type.pack(fill=BOTH, side=LEFT, expand=True)
        self.cpbook_typet = Label(type, text="Select Ticket Type", bg="cyan", font=("Arial", 15), fg='black')
        self.cpbook_typet.pack()
        
        types = Frame(type, width=200, bg='cyan')
        types.pack(fill=BOTH, expand=True)
        
        self.ticktype = StringVar(types, "low")
        self.lowcheck = Radiobutton(types, variable=self.ticktype, text="Lower", value="low", command=lambda: self.update_amount(0))#upamount0
        self.upcheck = Radiobutton(types, variable=self.ticktype, text="Upper", value="up", command=lambda: self.update_amount(1))#upamount1
        self.vipcheck = Radiobutton(types, variable=self.ticktype, text="VIP", value="vip", command=lambda: self.update_amount(2))#upamount2
        self.lowcheck.pack(fill=X, side=LEFT, expand=True)
        self.upcheck.pack(fill=X, side=LEFT, expand=True)
        self.vipcheck.pack(fill=X, side=LEFT, expand=True)
        
        line3 = Frame(self.booking, bg="white")
        line3.pack(fill=X)
        
        numb = Frame(line3, bg="cyan", width=200, padx=5, pady=5)
        numb.pack(fill=BOTH, side=LEFT, expand=True)
        self.cpbook_numbt = Label(numb, text="Select Ticket Amount", bg="cyan", font=("Arial", 15), fg='black')
        self.cpbook_numbs = Spinbox(numb, from_=1, to=9, command=lambda: self.reset_check())#rescheck
        self.cpbook_numbt.pack(fill=Y)
        self.cpbook_numbs.pack(fill=Y)
        
        check = Frame(line3, bg="cyan", width=200, padx=5, pady=5)
        check.pack(fill=BOTH, side=LEFT, expand=True)
        self.checkb = Button(check, text="Check Avalibility",padx=5, pady=5, bg="cyan", command=lambda: self.calculate_cost())#calculate_cost
        self.checkb.pack(fill=BOTH, expand=True)
        
        self.cpbook_sec2 = Label(self.booking, text="£~COST~", font=('Arial', 20), padx=25, pady=5)
        self.cpbook_sec2.pack(fill=BOTH, expand=False)
        self.cpbook_error = Label(self.booking,text="Enter customer info:", font=('Arial', 15), padx=5, pady=5)
        self.cpbook_error.pack(fill=BOTH, expand=False)
        
        part2 = Frame(self.booking, padx=10, pady=10)
        part2.pack(fill=X)
        
        p2line1 = Frame(part2)
        p2line1.pack(fill=X)
        
        name = Frame(p2line1, pady=5)
        name.pack(fill=BOTH, side=LEFT, expand=True)
        Label(name, text="First and Last Names", font=("Arial", 15), fg='white').pack(fill=X)
        self.fname = Entry(name)
        self.lname = Entry(name)
        self.fname.pack(fill=X, side=LEFT, expand=True)
        self.lname.pack(fill=X, side=LEFT, expand=True)
        
        phone = Frame(p2line1, pady=5)
        phone.pack(fill=BOTH, side=LEFT, expand=True)
        Label(phone, text="Phone", font=("Arial", 15), fg='white').pack(fill=Y)
        self.phones = Entry(phone)
        self.phones.pack(fill=X, expand=True)
        
        p2line2 = Frame(part2)
        p2line2.pack(fill=X)
        
        email = Frame(p2line2)
        email.pack(fill=BOTH, side=LEFT, expand=True)
        Label(email, text="Email", font=("Arial", 15), fg='white').pack(fill=X)
        self.cpbook_emails = Entry(email)
        self.cpbook_emails.pack(fill=Y)
        
        card = Frame(p2line2)
        card.pack(fill=BOTH, side=LEFT, expand=True)
        Label(card, text="Card", font=("Arial", 15), fg='white').pack(fill=X)
        self.cpbook_card = Entry(card)
        self.cpbook_card.pack(fill=X)
        
        p2line3 = Frame(part2)
        p2line3.pack(fill=X)
        
        exp = Frame(p2line3)
        exp.pack(fill=BOTH, side=LEFT, expand=True)
        Label(exp, text="Expiry Date", font=("Arial", 15), fg='white').pack(fill=X)
        self.cpbook_exp = DateEntry(exp)
        self.cpbook_exp.pack(fill=X)
        
        cvv = Frame(p2line3)
        cvv.pack(fill=BOTH, side=LEFT, expand=True)
        Label(cvv, text="CVV", font=("Arial", 15), fg='white').pack(fill=X)
        self.cpbook_cvv = Entry(cvv)
        self.cpbook_cvv.pack(fill=X)
        
        #Footer
        foot = Frame(self.booking,pady=10, padx=10,bg="cyan")
        foot.pack(fill=BOTH, side=TOP ,expand=True)
        
        Button(foot, text="CANCEL", font=('Arial', 15), padx=2, pady=2, bg='grey').pack(fill=BOTH, side=TOP, expand=True) #RESET ALL?
        self.cpbook_book = Button(foot, text="BOOK", font=('Arial', 15), padx=2, pady=2, bg='red', state=DISABLED, command=lambda: self.start_booking())
        self.cpbook_book.pack(fill=BOTH, side=TOP, expand=True)
        
        self.update_shows(self.filmlist[0])
    
    """Cameron Povey 21011010"""
    def update_shows(self, film):
        self.seldate = self.dates.get_date().strftime("%d/%m/%Y")
        showlist = self.controller.showings_cpbook(film,self.seldate)
        self.cpbook_shows["menu"].delete(0, "end")
        for showings in showlist:
            self.cpbook_shows["menu"].add_command(label=showings, command=lambda value=showings: [self.showoption.set(value),self.update_type()]) #uptype
        self.showoption.set("SELECT SHOW TIME")
        self.update_type()
        self.reset_check()
    
    """Cameron Povey 21011010"""
    def update_type(self):
        count = 0
        self.point = [self.lowcheck, self.upcheck, self.vipcheck]
        self.typeleft = self.controller.update_type(self.showoption.get())
        self.reset_type()
        self.reset_amount()
        if self.typeleft == None: return 0
        for i in range (len(self.typeleft)):
            if self.typeleft[i] == 0:
                (self.point[i]).deselect()
                (self.point[i]).configure(state = DISABLED)
                count+=1
            if count == 3:
                self.cpbook_typet.configure(text="SOLD OUT", fg='Red')
                self.checkb.configure(state=DISABLED) #checkout
        self.reset_check()
    
    """Cameron Povey 21011010"""     
    def update_amount(self, iden):
        self.cpbook_typesel = iden
        self.reset_amount()
        self.reset_check()
        if self.typeleft == None: return 0
        if self.typeleft[iden] < 9:
            self.cpbook_numbt.configure(text="Select Ticket Amount - LIMITED", fg='RED')
            self.cpbook_numbs.configure(to=self.typeleft[iden])
    
    """Cameron Povey 21011010"""   
    def calculate_cost(self):
        self.cost = self.controller.calculate_cost(self.cpbook_typesel, self.cpbook_numbs.get())
        if self.cost == None: return 0
        self.checkb.configure(state=DISABLED)
        self.cpbook_book.configure(state=NORMAL)
        self.cpbook_sec2.configure(text=("£",(round(self.cost, 2))))
    
    """Cameron Povey 21011010"""
    def start_booking(self):
        eminput = self.cpbook_emails.get()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        self.expdate = datetime.strptime(self.cpbook_exp.get(), "%d/%m/%Y")
        if self.expdate < datetime.today(): self.cusinfo_error(0)
        elif len(self.fname.get()) == 0: self.cusinfo_error(1)
        elif len(self.phones.get()) != 11 and len(self.phones.get()) != 13: self.cusinfo_error(2)
        elif len(self.cpbook_card.get()) != 16: self.cusinfo_error(3)
        elif len(self.cpbook_cvv.get()) != 3: self.cusinfo_error(4)
        elif len(self.lname.get()) == 0: self.cusinfo_error(5)
        elif(re.fullmatch(regex, eminput)):
            self.validated()
            return 0
        else:
            self.cusinfo_error(6)
    
    """Cameron Povey 21011010"""
    def validated(self):
        self.cpbook_error.configure(text="CUSTOMER INFORMATION VALIDATED", fg='GREEN')
        ticket_info = self.controller.book_film(self.fname.get(), self.lname.get(), self.phones.get(), self.cpbook_emails.get(), self.cpbook_card.get(), self.expdate, self.cpbook_cvv.get())
        self.confirmation_screen(ticket_info)
    
    """Cameron Povey 21011010"""
    #reset forms
    def cusinfo_error(self, errorno):
        if errorno == 0: self.cpbook_error.configure(text="Please enter a valid expiry date", fg='RED')
        elif errorno == 1: self.cpbook_error.configure(text="Please enter a valid first name", fg='RED')
        elif errorno == 2: self.cpbook_error.configure(text="Please enter a valid phone number", fg='RED')
        elif errorno == 3: self.cpbook_error.configure(text="Please enter a valid card number", fg='RED')
        elif errorno == 4: self.cpbook_error.configure(text="Please enter a valid cvv", fg='RED')
        elif errorno == 5: self.cpbook_error.configure(text="Please enter a valid last name", fg='RED')
        elif errorno == 6: self.cpbook_error.configure(text="Please enter a valid email", fg='RED')

    """Cameron Povey 21011010"""
    def reset_amount(self):
        self.cpbook_numbt.configure(text="Select Ticket Amount", fg='Black')
        self.cpbook_numbs.configure(to=9)
    
    """Cameron Povey 21011010"""
    def reset_check(self):
        self.checkb.configure(state=NORMAL)
        self.cpbook_sec2.configure(text="PRESS CHECK FOR COST")
        self.cpbook_book.configure(state=DISABLED)
    
    """Cameron Povey 21011010"""
    def reset_type(self):
        self.cpbook_typet.configure(text="Select Ticket Type", fg='Black')
        for i in range (3):
            (self.point[i]).configure(state = ACTIVE)
            if i == 0: (self.point[i]).select()
            else: (self.point[i]).deselect()
        
    """Cameron Povey 21011010"""
    #return ticket screen
    def confirmation_screen(self, ticket_info):
        self.cpbook_widgetlist = []
        for widget in self.booking.winfo_children():
            widget.pack_forget()
            self.cpbook_widgetlist.append(widget)
            
        self.bookidreturn = Label(self.booking, text="Booking ID: "+str(ticket_info[0][0]), font=('Arial', 25) ,pady=10)
        self.bookidreturn.pack()
        self.pricereturn = Label(self.booking, text="Price: "+str(ticket_info[0][1]), font=('Arial', 25) ,pady=10)
        self.pricereturn.pack()
        self.filmreturn = Label(self.booking, text="Film: "+str(ticket_info[1]), font=('Arial', 25) ,pady=10)
        self.filmreturn.pack()
        self.backbutton = Button(self.booking, text="Back to booking", font=('Arial', 25), pady=10, command=lambda: self.reset_screen())
        self.backbutton.pack()
        
    def reset_screen(self):
        for items in self.cpbook_widgetlist:
            items.pack(fill=X)
        self.bookidreturn.pack_forget()
        self.pricereturn.pack_forget()
        self.filmreturn.pack_forget()
        self.backbutton.pack_forget()
        clearlist = [self.cpbook_cvv, self.cpbook_exp, self.cpbook_card, self.cpbook_emails, self.phones, self.fname, self.lname]
        for labels in clearlist:
            labels.delete(0, END)
        self.update_shows(self.filmoption.get())
        self.reset_check()
        self.reset_amount()
        
    """Cameron Povey 21011010"""
    def cancellation_view(self):
        #cancellation frame    
        self.cancellation = Frame(self.notebook, width=800, height=280)
        self.cancellation.pack(fill='both', expand=True)
        self.notebook.add(self.cancellation, text='Make Cancellation')
        
        Label(self.cancellation, text="Enter Booking no", bg="cyan", font=("Arial", 25), fg='Black').pack(fill=X)
        self.cpcan_booknos = Spinbox(self.cancellation, from_=1, to=999999)
        self.cpcan_booknos.pack()
        Button(self.cancellation, text="Find Booking info", bg="cyan", padx=2,pady=2, command=lambda: self.get_film_info()).pack()
        
        #LIST OF INFO
        self.cpcan_line1 = Frame(self.cancellation)
        self.cpcan_line1.pack(fill=X)
        self.cpcan_bookid = Label(self.cpcan_line1, text="ID: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookprice = Label(self.cpcan_line1, text="Price: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookhall = Label(self.cpcan_line1, text="Hall Type: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookstaff = Label(self.cpcan_line1, text="Staff: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookid.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookprice.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookhall.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookstaff.pack(fill=X, side=LEFT, expand=True)
        
        self.cpcan_line2 = Frame(self.cancellation)
        self.cpcan_line2.pack(fill=X)
        self.cpcan_bookcusname = Label(self.cpcan_line2, text="First Name: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookcusphone = Label(self.cpcan_line2, text="Last Name: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookcusphone = Label(self.cpcan_line2, text="Phone: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookcusemail = Label(self.cpcan_line2, text="E-Mail: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookcusname.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookcusphone.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookcusphone.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookcusemail.pack(fill=X, side=LEFT, expand=True)
        
        self.cpcan_line3 = Frame(self.cancellation)
        self.cpcan_line3.pack(fill=X)
        self.cpcan_bookfilm = Label(self.cpcan_line3, text="Film: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookgenre = Label(self.cpcan_line3, text="Genre: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookyear = Label(self.cpcan_line3, text="Year: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookduration = Label(self.cpcan_line3, text="Duration: ", bg=None, fg="White", padx=10, pady=10)
        self.cpcan_bookfilm.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookgenre.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookyear.pack(fill=X, side=LEFT, expand=True)
        self.cpcan_bookduration.pack(fill=X, side=LEFT, expand=True)
        #END OF LIST
        
        self.cpcan_bookactionstitle = Label(self.cancellation, text="Cancel Cost: ", font=('Arial', 25) ,pady=10, bg="cyan", fg="black")
        self.cpcan_bookactionstitle.pack(fill=X)
        
        self.cpcan_bookcancel =Button(self.cancellation, height=2, padx=25, pady=25, text="Cancel", state=DISABLED)
        self.cpcan_bookcancel.pack(fill=X)
    
    """Cameron Povey 21011010"""
    def get_film_info(self):
        try: self.after_message.pack_forget()
        except: pass
        self.cpcan_filminfo = self.controller.get_film_info(self.cpcan_booknos.get())
        if self.cpcan_filminfo == 0:
            self.cpcan_resetbook()
            return 0
        else:
            self.cpcan_bookid.configure(text="ID: " + str(self.cpcan_filminfo[0][0]))
            self.cpcan_bookprice.configure(text="Price: £" + str(self.cpcan_filminfo[0][1]))
            self.cpcan_bookhall.configure(text="Hall Type: " + str(self.cpcan_filminfo[0][2]))
            self.cpcan_bookstaff.configure(text="Staff: " + str(self.cpcan_filminfo[2][0]))
            
            self.cpcan_bookcusname.configure(text="First Name: " + str(self.cpcan_filminfo[1][1]))
            self.cpcan_bookcusphone.configure(text="Last Name: " + str(self.cpcan_filminfo[1][2]))
            self.cpcan_bookcusphone.configure(text="Phone: " + str(self.cpcan_filminfo[1][3]))
            self.cpcan_bookcusemail.configure(text="E-Mail: " + str(self.cpcan_filminfo[1][4]))
            
            self.cpcan_bookfilm.configure(text="Film: " + str(self.cpcan_filminfo[3][1]))
            self.cpcan_bookgenre.configure(text="Genre: " + str(self.cpcan_filminfo[3][4]))
            self.cpcan_bookyear.configure(text="Year: " + str(self.cpcan_filminfo[3][5]))
            self.cpcan_bookduration.configure(text="Duration: " + str(self.cpcan_filminfo[3][7]))
            
            cpcan_cancelcost = self.controller.cancel_cost()
            #cpcan_cancelcost = "DAY_PRIOR" #Placeholder
            if cpcan_cancelcost == "SAME_DAY":
                self.cpcan_bookactionstitle.configure(text="CANNOT CANCEL ON DAY OF SHOW")
                self.cpcan_bookcancel.configure(state=DISABLED, command=None)
                return 0
            elif cpcan_cancelcost == "DAY_PRIOR":
                self.cpcan_bookactionstitle.configure(text="Cancel Cost: " + str(self.cpcan_filminfo[0][1]/2))
                self.cpcan_bookcancel.configure(state=NORMAL, command=lambda: self.cpcan_cancel())
            else:
                self.cpcan_bookactionstitle.configure(text="Cancel Cost: FREE")
                self.cpcan_bookcancel.configure(state=NORMAL, command=lambda: self.cpcan_cancel())
    
    """Cameron Povey 21011010"""
    def cpcan_cancel(self):
        cancel_state = self.controller.commit_cancel()
        if cancel_state == 1: self.after_message = Label(self.cancellation, text="Ticket Removed!", font=('Arial', 25) ,pady=10,width=20, bg=None, fg="Green")
        else: self.after_message = Label(self.cancellation, text="ERROR, Contact Admin", font=('Arial', 25) ,pady=10,width=20, bg=None, fg="Red")
        self.after_message.pack()
    
    """Cameron Povey 21011010"""
    def cpcan_resetbook(self):
        self.cpcan_bookid.configure(text="ID: ")
        self.cpcan_bookprice.configure(text="Price: ")
        self.cpcan_bookhall.configure(text="Hall Type: ")
        self.cpcan_bookstaff.configure(text="Staff: ")
        self.cpcan_bookcusname.configure(text="First Name: ")
        self.cpcan_bookcusphone.configure(text="Last Name: ")
        self.cpcan_bookcusphone.configure(text="Phone: ")
        self.cpcan_bookcusemail.configure(text="E-Mail: ")
        self.cpcan_bookfilm.configure(text="Film: ")
        self.cpcan_bookgenre.configure(text="Genre: ")
        self.cpcan_bookyear.configure(text="Year: ")
        self.cpcan_bookduration.configure(text="Duration: ") 
        self.cpcan_bookactionstitle.configure(text="INVALID BOOKING NUMBER")
        self.cpcan_bookcancel.configure(state=DISABLED, command=None)
        try: self.after_message.pack_forget()
        except: pass
        
    
    """Sude Fidan 21068639"""
    def manage_view(self):
        #manage frame
        self.manage = Frame(self.notebook, width=800, height=280)
        self.manage.pack(fill='both', expand=True)
        self.notebook.add(self.manage, text='Manage Screening')

        #create a model
        self.manageModel = ManageScreeningModel()

        #create a view and place it on the root window
        self.manageView = ManageScreeningView(self.manage)
        self.manageView.pack(expand=True, fill='both')

        #create a controller
        self.manageController = ManageScreeningController(self, self.manageModel, self.manageView)

        #set the controller to view
        self.manageView.set_controller(self.manageController)

        self.manageView.manage_screening()

    """Sude Fidan 21068639"""
    def report_view(self):
        #report frame
        self.report = Frame(self.notebook, width=800, height=280)
        self.report.pack(fill='both', expand=True)
        self.notebook.add(self.report, text='Generate Report')

        #create a model
        self.reportModel = GenerateReportModel()

        #create a view and place it on the root window
        self.reportView = GenerateReportView(self.report)
        self.reportView.pack(expand=True, fill='both')

        #create a controller
        self.reportController = GenerateReportController(self, self.reportModel, self.reportView)

        #set the controller to view
        self.reportView.set_controller(self.reportController)

        self.reportView.generate_report()

    """Fiorella Scarpino 21010043"""
    def new_cinema_view(self):
        #new_cinema frame
        self.new_cinema = Frame(self.notebook, width=800, height=280)
        self.new_cinema.pack(fill='both', expand=True)
        self.notebook.add(self.new_cinema, text='Add New Cinema')

        padding = {'ipadx': 10, 'ipady': 10}
        title = Label(self.new_cinema,text="Add New Cinema",font=14).pack(**padding)

        self.cityText = StringVar()
        city_Label = Label(self.new_cinema, text='City', font=12).pack(**padding, fill=X)
        self.city_Entry = Entry(self.new_cinema, textvariable=self.cityText)
        self.city_Entry.pack(**padding, fill=X)

        self.locationText = StringVar()
        location_Label = Label(self.new_cinema, text='Location', font=12).pack(**padding, fill=X)
        self.location_Entry = Entry(self.new_cinema, textvariable=self.locationText)
        self.location_Entry.pack(**padding, fill=X)

        self.screenNumber = IntVar()
        screen_Label = Label(self.new_cinema, text='Number of Screens', font=12).pack(**padding, fill=X)
        self.screen_Entry = Entry(self.new_cinema, textvariable=self.screenNumber)
        self.screen_Entry.pack(**padding, fill=X)

        #to edit the capacity for each screen
        self.getScreenNumber = Button(self.new_cinema, text='Edit Screens',command=lambda: self.getscreensChange(), width=12)
        self.getScreenNumber.pack(**padding)
    
    """Fiorella Scarpino 21010043"""
    def getscreensChange(self):
        #capacity for each screen 
        try:
            self.getScreenNumber['state'] = DISABLED
            self.seatEntryArray = []
            self.screenGet = self.screenNumber.get()

            #number of screens
            self.Screenlist = np.arange(1,self.screenGet+1)
            self.seatingCap_Label = Label(self.new_cinema, text='Seating Capacity', font=12).pack()

            #makes the same amount of labels as screens
            for screens in range(len(self.Screenlist)):
                #label for each screen
                self.screenNumber = Label(self.new_cinema, text=f'Screen {screens+1}', font=12).pack()
                self.screenEntry = Entry(self.new_cinema)
                self.screenEntry.pack()
                self.seatEntryArray.append(self.screenEntry)
            
            self.addCinemaButton = Button(self.new_cinema, text='Add New Cinema',command=lambda: self.add_new_cinema(), width=12).pack()
        except TclError:  #validation for integer
            self.getScreenNumber['state'] = NORMAL
            messagebox.showerror(title = 'Error',message='Please enter an integer')

    """Fiorella Scarpino 21010043"""
    def add_new_cinema(self):
         #get user data for new cinema
        self.cityGet = self.cityText.get()
        self.locationGet = self.locationText.get()
        allValid = True # to validate
        #seat capacities
        self.seatingArray = ''
        for s in self.seatEntryArray:
            self.seatingArray = self.seatingArray + str(s.get()) + '\n'
        self.seatEntry = self.seatEntryArray

        if self.cityGet.isalpha() and self.locationGet.isalpha():
            allValid = True
            for valid in range(len(self.seatEntry)):
                if self.seatEntry[valid].get().isdigit():
                    allValid = True
                else:
                    allValid = False
        else:
            allValid = False
            
        #final validation
        if allValid == True:
            self.dataToAdd = self.controller.get_new_cinema(self.cityGet, self.locationGet,self.seatEntry) ###HERE
        else:
            messagebox.showerror(title = 'Error',message='Please enter integer for seating capacity and string for city/location')

    """Fiorella Scarpino 21010043"""
    def clear_text(self):
        #clears entry text
        self.city_Entry.delete(0,END)
        self.location_Entry.delete(0, END)
        self.screen_Entry.delete(0, END) # number of screens
        self.getScreenNumber['state'] = NORMAL


    """Sude Fidan 21068639"""
    def logout_clicked(self):
        if self.controller:
            self.controller.logout()

    """Sude Fidan 21068639"""
    def set_controller(self, controller):
        self.controller = controller