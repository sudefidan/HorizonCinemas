import sqlite3
from datetime import datetime
from tkinter import messagebox   #TODO: MESSAGE BOX SHOULD BE IN VIEW



class HomepageModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('mvcHorizon/database/horizoncinemas.db')

    """Sude Fidan 21068639"""  
    def date_format(self, date):
        return datetime.utcfromtimestamp(date/1000).strftime("%d/%m/%Y")
    
    """Cameron Povey 21011010"""
    def get_timestamp(self,date_dmy_form):
        format = date_dmy_form.strftime("%m/%d/%Y, %H:%M:%S")
        format = datetime.strptime(format,"%m/%d/%Y, %H:%M:%S")
        timestamp = datetime.timestamp(format)
        return (int(timestamp)*1000)
    
    """Cameron Povey 21011010"""
    def get_today_unix(self):
        current_time = datetime.now()
        current_time = current_time.strftime("%m/%d/%Y, %H:%M:%S")
        current_format = datetime.strptime(current_time,"%m/%d/%Y, %H:%M:%S")
        current_timestamp = datetime.timestamp(current_format)
        return (int(current_timestamp)*1000)

    """Fiorella Scarpino 21010043"""
    def get_films(self):
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.execute('SELECT * from Film')
        self.records = cursor.fetchall()
        cursor.close()
        return self.records   

    """Fiorella Scarpino 21010043"""
    def show_selection(self,value):
        cursor = self.conn.execute("SELECT * from Show WHERE filmId = ?", (value,))
        records = cursor.fetchall()
        listing_table = []
        for listing in records:
            listing_table.append([self.date_format(listing[1]) ,listing[2],listing[3]])
        cursor.close()
        return listing_table
        
    """Fiorella Scarpino 21010043"""
    #add new cinema to the database
    def get_new_cinema(self, city,location,seatEntry):
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.cursor()
        if city == '' or location == '' or seatEntry == '':
            #TODO: MESSAGE BOX SHOULD BE IN VIEW
             messagebox.showerror(title = 'Error',message='Please enter all fields')
        else:
            self.cursor.execute("INSERT INTO cinema VALUES (NULL,?, ?)",(city, location))
            self.conn.commit()
            #adds data to screen table
            cinemaID = self.cur.lastrowid
            for i in range(len(seatEntry)):
                self.cursor.execute("INSERT INTO Screen VALUES (NULL,?,?,?)",(seatEntry[i].get(),cinemaID,i+1))
                self.conn.commit()
            #TODO: MESSAGE BOX SHOULD BE IN VIEW
            messagebox.showinfo(title='Complete', message='Data added to database successfully')
            self.cur.close()
    
    """Cameron Povey 21011010"""
    def get_films_cinema(self, location):
        self.strscrlist = ""
        self.strfilmref = ""
        self.screenlist = []
        filmref = []
        filmarr = []
        
        #get cinema ID
        cinemasCursor = self.conn.execute("SELECT id FROM Cinema WHERE location = '%s'" % (location))
        self.cinId = cinemasCursor.fetchone()[0]
        #fetch list of screens from cinema location
        screensCursor = self.conn.execute("SELECT id FROM Screen WHERE cinemaID = '%s'" % (self.cinId))
        scr = screensCursor.fetchall()
        
        #add them to a str list
        for i in range (len(scr)):
            self.screenlist.append(scr[i][0])
            if i == 0: self.strscrlist = str(self.screenlist[i])
            else: self.strscrlist = str(self.strscrlist) + ", " + str(self.screenlist[i])
        
        #get filmIds from show which have the screenIds found before 
        filmidCursor = self.conn.execute("SELECT filmId FROM Show WHERE screenId IN (%s)" % (self.strscrlist))
        filmids = filmidCursor.fetchall()
        
        #add them to another str list
        for i in range(len(filmids)):
            filmref.append(filmids[i][0])
        filmref = list(dict.fromkeys(filmref))
        
        for i in range(len(filmref)):
            if i == 0: self.strfilmref = str(self.strfilmref) + str(filmref[i])
            else: self.strfilmref = str(self.strfilmref) + ", " + str(filmref[i])
        
        #get film names that are showing in the cinema
        filmfindCursor = self.conn.execute("SELECT name FROM Film WHERE Id IN (%s)" % (self.strfilmref))
        films = filmfindCursor.fetchall()
        
        #add them to array to return
        for i in range (len(films)):
            filmarr.append(films[i][0])
            
        cinemasCursor.close()
        screensCursor.close()
        filmidCursor.close()
        filmfindCursor.close()
        
        return(filmarr)
    
    """Cameron Povey 21011010"""
    def showings_cpbook(self,film,date):
        self.cpbook_date = self.get_timestamp(datetime.strptime(date, "%d/%m/%Y"))
        showarr = []
        self.cpbookfilmsel = film
        find_idCursor = self.conn.execute("SELECT id FROM Film WHERE name = '%s'" % (film))
        self.selected_filmid = (find_idCursor.fetchone()[0])
        
        showfindCursor = self.conn.execute("SELECT time FROM Show WHERE filmId='%s' AND screenId IN (%s) AND date = '%s'" % (self.selected_filmid, self.strscrlist, self.cpbook_date))
        showings = showfindCursor.fetchall()
        
        for i in range (len(showings)): showarr.append(showings[i][0])
        
        find_idCursor.close()
        showfindCursor.close()
        
        return showarr
    
    """Cameron Povey 21011010"""
    def update_type(self,time):
        remaining = []
        point = ["LOWER HALL", "UPPER HALL", "VIP"]
        filled = [0,0,0]
        maxseat = [0,0,0]
        
        self.cpbook_time = time
        if self.cpbook_time == "SELECT SHOW TIME": return None

        screenstateCursor = self.conn.execute("SELECT id FROM Show WHERE time='%s' AND filmId='%s' AND date = '%s'" % (self.cpbook_time, self.selected_filmid, self.cpbook_date))
        self.cpbook_showid = screenstateCursor.fetchone()[0]
        
        for i in range(3):
            amountlowCursor = self.conn.execute("SELECT Id FROM Ticket WHERE showId='%s' AND hallType = '%s'" % (self.cpbook_showid, point[i]))
            filled[i] = len(amountlowCursor.fetchall())
        
        fettchshowCursor = self.conn.execute("SELECT screenId FROM Show WHERE Id='%s'" % (self.cpbook_showid))
        screen = fettchshowCursor.fetchone()[0]
        fetchcapCursor = self.conn.execute("SELECT SeatingCapacity FROM Screen WHERE Id='%s'" % (screen))
        screencap = fetchcapCursor.fetchone()[0]
        
        maxseat[0] = int(screencap * 0.3)
        maxseat[1] = int((screencap - maxseat[0]) - 10)
        maxseat[2] = screencap - (maxseat[1] + maxseat[0])
        
        for i in range(3):
            remaining.append(maxseat[i] - filled[i])
            
        screenstateCursor.close()
        amountlowCursor.close()
        fettchshowCursor.close()
        fetchcapCursor.close()
        return remaining
    
    """Cameron Povey 21011010"""
    def calculate_cost(self, typesel, amount):
        if self.cpbook_time == "SELECT SHOW TIME": return None
        
        timepoint = ["MORNING", "AFTERNOON", "EVENING"]
        type_change = [1, 1.2, 1.44]
        
        adtime = str(self.cpbook_time)+str(':00')
        dt_time = datetime.strptime(adtime, '%H:%M:%S').time()
        
        #end times
        timechange = ['12:00:00', '17:00:00', '23:59:59']
        for i in range(3):
            timechange[i] = datetime.strptime(str(timechange[i]), '%H:%M:%S').time()
            
        for i in range(3):
            if (dt_time.hour < timechange[i].hour):
                timeframe = timepoint[i]
                break
            if (dt_time.hour == timechange[i].hour):
                if (dt_time.minute > timechange[i].minute):
                    timeframe = timepoint[i+1]
                else:
                    timeframe = timepoint[i]
                break
        standardstateCursor = self.conn.execute("SELECT price FROM Ticket_Pricing WHERE cinemaId = '%s' AND  showTimeType = '%s'" % (self.cinId, timeframe))
        stan_price = standardstateCursor.fetchone()[0]
        
        priceper = stan_price * type_change[typesel]
        self.ovrprice = priceper * int(amount)
        standardstateCursor.close()
        self.type_selected = typesel
        return self.ovrprice
    
    """Cameron Povey 21011010"""
    def book_film(self, fname, lname, phone, email, card, exp, cvv, staffid):
        halllist = ["LOWER HALL", "UPPER HALL", "VIP"]
        halltype = halllist[self.type_selected]
        cursor = self.conn.cursor()
        
        #check for customer
        customerid = self.check_customer(fname, lname, phone, email)
        #create customer if doesnt exist
        if customerid == None:
            customerid = self.create_customer(fname, lname, phone, email, card, exp, cvv)
        #create ticket
        customerid = customerid[0]
        cursor.execute("INSERT INTO Ticket (price, hallType, customerId, staffId, showId) VALUES (?, ?, ?, ?, ?)", (str(self.ovrprice), halltype, customerid, staffid, self.cpbook_showid))
        cursor.close()
        self.conn.commit()
        
        returntickinfoCursor = self.conn.execute("SELECT Id, price FROM Ticket WHERE customerId = '%s' AND showId = '%s'" % (customerid, self.cpbook_showid))
        tickinfo = (returntickinfoCursor.fetchone())
        returntickinfoCursor.close()#close?
        return [tickinfo, self.cpbookfilmsel]
    
    """Cameron Povey 21011010"""
    def create_customer(self, fname, lname, phone, email, card, exp, cvv):
        expdate = str(exp.strftime("%m/%y"))
        phoneno = str(phone)
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Customer (name, surname, phone, email, cardNumber, expiryDate, CVV) VALUES(?, ?, ?, ?, ?, ?, ?)", (fname, lname, phoneno, email, card, expdate, cvv))
        cursor.close()
        self.conn.commit()
        return self.check_customer(fname, lname, phone, email)
    
    """Cameron Povey 21011010"""
    def check_customer(self, fname, lname, phone, email):
        checkstateCursor = self.conn.execute("SELECT Id FROM Customer WHERE name = '%s' AND surname = '%s' AND phone = '%s' AND email = '%s'" % (fname, lname, phone, email))
        customerstate = checkstateCursor.fetchone()
        checkstateCursor.close()
        return (customerstate)
    
    """Cameron Povey 21011010"""
    def get_film_info(self, bookId):
        cursorBooking = self.conn.execute("SELECT * FROM Ticket WHERE Id = '%s'" % (bookId))
        self.bookingInfo= cursorBooking.fetchone()
        if self.bookingInfo == None: return 0
        cursorCustomer= self.conn.execute("SELECT * FROM Customer WHERE Id = '%s'" % (self.bookingInfo[3]))
        customerInfo = cursorCustomer.fetchone()
        cursorStaff = self.conn.execute("SELECT username FROM staff WHERE Id = '%s'" % (self.bookingInfo[4]))
        staffInfo = cursorStaff.fetchone()
        cursorFilm = self.conn.execute("SELECT * FROM Film WHERE Id = '%s'" % (self.bookingInfo[5]))
        filmInfo = cursorFilm.fetchone()
        cursorBooking.close()
        return [self.bookingInfo, customerInfo, staffInfo, filmInfo]
    
    """Cameron Povey 21011010"""
    def cancel_cost(self):
        cpcanTodayTimeStamp = self.get_today_unix
        
        #DELETE - JUST TO TEST DATES
        cpcanFormatedDate = datetime.strptime("12/4/2022, 08:00:00","%m/%d/%Y, %H:%M:%S") #use backwards date
        self.Unix_timestamp = datetime.timestamp(cpcanFormatedDate)
        cpcanTodayTimeStamp = int(self.Unix_timestamp)*1000
        #END DELETE
        
        cursor = self.conn.execute("SELECT date, time FROM Show WHERE Id = '%s'" % (self.bookingInfo[5]))
        selectedTimeAndDate = cursor.fetchone()
        h, m = selectedTimeAndDate[1].split(':')
        
        timems = int(h)*3600000 + int(m)*60000
        selectedTimeAndDate = int(selectedTimeAndDate[0]) + int(timems)
        cursor.close()
        
        if selectedTimeAndDate < (cpcanTodayTimeStamp + 86400000): return "SAME_DAY"
        elif selectedTimeAndDate < (cpcanTodayTimeStamp + 172800000): return "DAY_PRIOR"
        else: return "CANCEL_FREE"
    
    """Cameron Povey 21011010"""
    def commit_cancel(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM Ticket WHERE Id = '%s'" % (self.bookingInfo[0]))
            cursor.close()
            self.conn.commit()
            return 1
        except:
            cursor.close()
            self.conn.commit()
            return 0
        
    






    
    