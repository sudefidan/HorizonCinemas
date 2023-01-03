import sqlite3
from datetime import datetime

class Model():
    def __init__(self):
        print("TEST - MODEL")
        print("ATTEMPTING CONNECTION")
        self.strscrlist = ""
        #self.dbconnect()
        
        #update on login
        self.cinemaid = 2 #CHANGE
        self.staffid = 3
        
        self.screenlist = []
        db = self.dbconnect()
        cursor = db.cursor()
        screens = db.execute("SELECT id FROM Screen WHERE CinemaID = '%s'" % (self.cinemaid))
        scr = screens.fetchall()
        for i in range (len(scr)):
            self.screenlist.append(scr[i][0])
            if i == 0:
                self.strscrlist = str(self.strscrlist) + str(self.screenlist[i])
            else:
                self.strscrlist = str(self.strscrlist) + ", " + str(self.screenlist[i])
        cursor.close()
        #print(self.screeno)
            
        
    def dbconnect(self):
        try:
            db = sqlite3.connect(database='decon/database/horizoncinemas.sqlite')
            return (db)
        except:
            return (sqlite3.Error)
            
    def filmlist(self):
        filmarr = []
        filmref = []
        self.strfilmref = ""
        db = self.dbconnect()
        cursor = db.cursor()
        
        print(self.strscrlist)
        filmfind = db.execute("SELECT filmId FROM Show WHERE screenId IN (%s)" % (self.strscrlist))
        #filmfind = db.execute("SELECT filmId FROM Show WHERE screenId IN (1,2,3)")
        #take these film id and collect view names from 'film' table
        filmids = filmfind.fetchall()
        for i in range(len(filmids)):
            filmref.append(filmids[i][0])
        filmref = list(dict.fromkeys(filmref))
        for i in range(len(filmref)):
            if i == 0: self.strfilmref = str(self.strfilmref) + str(filmref[i])
            else: self.strfilmref = str(self.strfilmref) + ", " + str(filmref[i])
        print(filmref)
        
        filmfind = db.execute("SELECT name FROM Film WHERE Id IN (%s)" % (self.strfilmref))
        films = filmfind.fetchall()
        
        for i in range (len(films)):
            print(films[i][0])
            filmarr.append(films[i][0])
        cursor.close()
        print("------")
        print(filmarr)
        return(filmarr)
    
    def getshowings(self, selfilm, seldate):
        self.seldate = seldate
        self.seldate = str(seldate.strftime("%m/%d/%Y, %H:%M:%S"))
        formated_date = datetime.strptime(self.seldate,"%m/%d/%Y, %H:%M:%S")
        self.Unix_timestamp = datetime.timestamp(formated_date)
        self.timestamp = int(self.Unix_timestamp)*1000
        print(self.timestamp)
        
        showarr = []
        db = self.dbconnect()
        cursor = db.cursor()
        print(selfilm)
        IDfind = db.execute("SELECT id FROM Film WHERE name='%s'" % (selfilm))
        self.selected_filmid = (IDfind.fetchone())[0]
        print(self.strscrlist)
        showfind = db.execute("SELECT time FROM Show WHERE filmId='%s' AND screenId IN (%s) AND date = '%s'" % (self.selected_filmid, self.strscrlist, self.timestamp))
        showings = showfind.fetchall()
        for i in range (len(showings)):
            #print(showings[i][0])
            showarr.append(showings[i][0])
        cursor.close()
        return(showarr)
    
    
    def getids(self, time):
        self.time = time
        db = self.dbconnect()
        cursor = db.cursor()
        print(self.selected_filmid)
        #cinema(self)/film(self)/time
        screenstate = db.execute("SELECT id FROM Show WHERE time='%s' AND filmId='%s' AND date = '%s'" % (self.time, self.selected_filmid, self.timestamp))
        self.showid = screenstate.fetchone()[0]
        
        cursor.close()
        return (self.showid, self.time, self.selected_filmid)
    
    def filled(self):
        db = self.dbconnect()
        cursor = db.cursor()
        point = ["LOWER HALL", "UPPER HALL", "VIP"]
        filled = [0, 0, 0]
        for i in range(3):
            amountlow = db.execute("SELECT Id FROM Ticket WHERE showId='%s' AND hallType = '%s'" % (self.showid, point[i]))
            filled[i] = len(amountlow.fetchall())
        print(filled)
        cursor.close()
        return filled
    
    def getstand(self, timeframe):
        db = self.dbconnect()
        cursor = db.cursor()
        standardstate = db.execute("SELECT price FROM Ticket_Pricing WHERE cinemaId = '%s' AND  showTimeType = '%s'" % (self.cinemaid, timeframe))
        stan_price = standardstate.fetchone()[0]
        cursor.close()
        return stan_price
    
    def typesmax(self):
        self.maxseat = []
        pointmax = ["LOWER HALL MAX", "UPPER HALL MAX", "VIP MAX"]
        
        db = self.dbconnect()
        cursor = db.cursor()
        
        self.maxseat = [0, 0, 0]
        
        #NEED TO UPDATE SQL TABLE TO HAVE HOW MANY TICKETS WAS PURCHASED
            
        #NEED SCREEN MAX FOR EACH TYPE OF SEAT
        #for i in range(3):
            #print("MAX SEATING: ", point[i])
        
            #fetch showid where film = film time = time 
            #fetch select LHM,UHM,VIPM Where showId = showID
        fettchshow = db.execute("SELECT screenId FROM Show WHERE Id='%s'" % (self.showid))
        self.screen = fettchshow.fetchone()[0]
        fetchcap = db.execute("SELECT SeatingCapacity FROM Screen WHERE Id='%s'" % (self.screen))
        self.screencap = fetchcap.fetchone()[0]
        self.maxseat[0] = int(self.screencap * 0.3)
        self.maxseat[1] = int((self.screencap - self.maxseat[0]) - 10)
        self.maxseat[2] = self.screencap - (self.maxseat[1] + self.maxseat[0])
        print(self.maxseat)
        cursor.close()
        return(self.maxseat)

    def checkforcustomer(self, book_name, book_last, book_phone, book_email, book_card, book_expdate, book_cvv):
        print("CHECK CUS")
        db = self.dbconnect()
        cursor = db.cursor()
        checkstate = db.execute("SELECT Id FROM Customer WHERE name = '%s' AND surname = '%s' AND phone = '%s' AND email = '%s'" % (book_name, book_last, book_phone, book_email))
        returnedcheck = checkstate.fetchone()
        print(returnedcheck)
        cursor.close()
        if returnedcheck == None: return 0
        else:
            print("EX CUS TRUE")
            return returnedcheck[0]
            
        
    def createcustomer(self, book_name, book_last, book_phone, book_email, book_card, book_expdate, book_cvv):
        print("CUSTOMER")
        db = self.dbconnect()
        cursor = db.cursor()
        book_expdate = str(book_expdate.strftime("%m/%y"))
        book_phone = str(book_phone)
        
        print(book_expdate, type(book_expdate))
        try:
            #cursor.execute('''INSERT INTO Customer (name, surname, phone, email, cardNumber, expiryDate, CVV) VALUES ('test', 'test', 12345678901, 'test', 1234567890123, 1/25, 123)''')
            cursor.execute("INSERT INTO Customer (name, surname, phone, email, cardNumber, expiryDate, CVV) VALUES(?, ?, ?, ?, ?, ?, ?)", (book_name, book_last, book_phone, book_email, book_card, "1/25", book_cvv))
            db.commit()
            newcusid = (self.checkforcustomer())
        except sqlite3.Error as error:
            print(error)
            return 0
        cursor.close()
        db.close()
        return newcusid
    
    def createticket (self, cusno, price,halltype):
        print("TICKET")
        db = self.dbconnect()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO Ticket (price, hallType, customerId, staffId, showId) VALUES (?, ?, ?, ?, ?)", (price, halltype, cusno, self.staffid, self.showid))
            db.commit()
        except sqlite3.Error as error:
            print(error)
            return 0
        cursor.close()
        db.close()
        return 1
    
    def relocstaff(self):
        print("RELOCSTAFF")
        db = self.dbconnect()
        cursor = db.cursor()
        findstaff = db.execute("SELECT username FROM staff WHERE Id = '%s'" % (self.staffid))
        findloc = db.execute("SELECT location FROM Cinema WHERE Id = '%s'" % (self.cinemaid))
        staffun = findstaff.fetchone()[0]
        locname = findloc.fetchone()[0]
        return [locname,staffun]