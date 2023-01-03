import sqlite3
from datetime import datetime

class HomepageModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('database/horizoncinemas.db')

        """Cameron Povey 21011010"""
        self.strscrlist = ""
        #update on login
        self.cinemaid = 2 #CHANGE
        
        self.screenlist = []
        cursor = self.conn.cursor()
        screens = self.conn.execute("SELECT id FROM Screen WHERE CinemaID = '%s'" % (self.cinemaid))
        scr = screens.fetchall()
        for i in range (len(scr)):
            self.screenlist.append(scr[i][0])
            if i == 0:
                self.strscrlist = str(self.strscrlist) + str(self.screenlist[i])
            else:
                self.strscrlist = str(self.strscrlist) + ", " + str(self.screenlist[i])
        cursor.close()
        #print(self.screeno)

    """Sude Fidan 21068639"""  
    def date_format(self, date):
        return datetime.utcfromtimestamp(date/1000).strftime("%d/%m/%Y")

    """Fiorella Scarpino"""
    def get_films(self):
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.execute('SELECT * from Film')
        self.records = cursor.fetchall()
        cursor.close()
        return self.records
    
    """Fiorella Scarpino"""
    def get_film_dict(self, records,film ):
        return str(f"Film Name: {records[film][1]}\nCast: {records[film][2]}\nDescription: {records[film][6]}\n\nRating: {records[film][3]}\nGenre: {records[film][4]}\nRelease Year: {records[film][5]}\nDuration: {records[film][7]}\nAge Rating: {records[film][8]}")

    """Fiorella Scarpino"""
    def show_selection(self,value):
        cursor = self.conn.execute("SELECT * from Show WHERE filmId = ?", (value,))
        records = cursor.fetchall()
        listing_table = []
        for listing in records:
            listing_table.append([self.date_format(listing[1]) ,listing[2],listing[3]])
        cursor.close()
        return listing_table

    """
    def add_film(self,filmName, filmCast, filmRating, filmGenre, filmYear, filmDescription, filmDuration, filmAge):
        cursor = self.conn.execute("INSERT INTO Film (name, cast, rating, genre, releaseYear, description, duration, ageRating) VALUES (filmName, filmCast, filmRating, filmGenre, filmYear, filmDescription, filmDuration, filmAge)" )
    def remove_film(self, filmName):
        cursor = self.conn.execute("DELETE FROM Film WHERE name="%s"%(filmName))
    """









    
    """Cameron Povey 21011010"""
    def filmlist(self):
        filmarr = []
        filmref = []
        self.strfilmref = ""
        cursor = self.conn.cursor()
        
        print(self.strscrlist)
        filmfind = self.conn.execute("SELECT filmId FROM Show WHERE screenId IN (%s)" % (self.strscrlist))
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
        
        filmfind = self.conn.execute("SELECT name FROM Film WHERE Id IN (%s)" % (self.strfilmref))
        films = filmfind.fetchall()
        
        for i in range (len(films)):
            print(films[i][0])
            filmarr.append(films[i][0])
        cursor.close()
        print("------")
        print(filmarr)
        return(filmarr)

    """Cameron Povey 21011010"""
    def getshowings(self, selfilm, seldate):
        self.seldate = seldate
        self.seldate = str(seldate.strftime("%m/%d/%Y, %H:%M:%S"))
        formated_date = datetime.strptime(self.seldate,"%m/%d/%Y, %H:%M:%S")
        self.Unix_timestamp = datetime.timestamp(formated_date)
        self.timestamp = int(self.Unix_timestamp)*1000
        print(self.timestamp)
        
        showarr = []
        cursor = self.conn.cursor()
        print(selfilm)
        IDfind = self.conn.execute("SELECT id FROM Film WHERE name='%s'" % (selfilm))
        self.selected_filmid = (IDfind.fetchone())[0]
        print(self.strscrlist)
        showfind = self.conn.execute("SELECT time FROM Show WHERE filmId='%s' AND screenId IN (%s) AND date = '%s'" % (self.selected_filmid, self.strscrlist, self.timestamp))
        showings = showfind.fetchall()
        for i in range (len(showings)):
            #print(showings[i][0])
            showarr.append(showings[i][0])
        cursor.close()
        return(showarr)

    """Cameron Povey 21011010"""    
    def get_show_id(self, time):
        self.time = time
        cursor = self.conn.cursor()
        print(self.selected_filmid)
        screenstate = self.conn.execute("SELECT id FROM Show WHERE time='%s' AND filmId='%s' AND date = '%s'" % (self.time, self.selected_filmid, self.timestamp))
        self.showid = screenstate.fetchone()[0]
        cursor.close()
        return (self.showid, self.time, self.selected_filmid)
    
    """Cameron Povey 21011010"""    
    def filled(self):
        cursor = self.conn.cursor()
        point = ["LOWER HALL", "UPPER HALL", "VIP"]
        filled = [0, 0, 0]
        for i in range(3):
            amountlow = self.conn.execute("SELECT Id FROM Ticket WHERE showId='%s' AND hallType = '%s'" % (self.showid, point[i]))
            filled[i] = len(amountlow.fetchall())
        print(filled)
        cursor.close()
        return filled
    
    """Cameron Povey 21011010"""    
    def getstand(self, timeframe):
        cursor = self.conn.cursor()
        standardstate = self.conn.execute("SELECT price FROM Ticket_Pricing WHERE cinemaId = '%s' AND  showTimeType = '%s'" % (self.cinemaid, timeframe))
        stan_price = standardstate.fetchone()[0]
        cursor.close()
        return stan_price
    
    """Cameron Povey 21011010"""    
    def typesmax(self):
        self.maxseat = []
        pointmax = ["LOWER HALL MAX", "UPPER HALL MAX", "VIP MAX"]
        
        cursor = self.conn.cursor()
        
        self.maxseat = [0, 0, 0]
        
        #NEED TO UPDATE SQL TABLE TO HAVE HOW MANY TICKETS WAS PURCHASED
            
        #NEED SCREEN MAX FOR EACH TYPE OF SEAT
        #for i in range(3):
            #print("MAX SEATING: ", point[i])
        
            #fetch showid where film = film time = time 
            #fetch select LHM,UHM,VIPM Where showId = showID
        fettchshow = self.conn.execute("SELECT screenId FROM Show WHERE Id='%s'" % (self.showid))
        self.screen = fettchshow.fetchone()[0]
        fetchcap = self.conn.execute("SELECT SeatingCapacity FROM Screen WHERE Id='%s'" % (self.screen))
        self.screencap = fetchcap.fetchone()[0]
        self.maxseat[0] = int(self.screencap * 0.3)
        self.maxseat[1] = int((self.screencap - self.maxseat[0]) - 10)
        self.maxseat[2] = self.screencap - (self.maxseat[1] + self.maxseat[0])
        print(self.maxseat)
        cursor.close()
        return(self.maxseat)

    """Cameron Povey 21011010"""    
    def checkforcustomer(self, book_name, book_last, book_phone, book_email, book_card, book_expdate, book_cvv):
        print("CHECK CUS")
        cursor = self.conn.cursor()
        checkstate = self.conn.execute("SELECT Id FROM Customer WHERE name = '%s' AND surname = '%s' AND phone = '%s' AND email = '%s'" % (book_name, book_last, book_phone, book_email))
        returnedcheck = checkstate.fetchone()
        print(returnedcheck)
        cursor.close()
        if returnedcheck == None: return 0
        else:
            print("EX CUS TRUE")
            return returnedcheck[0]
            
    """Cameron Povey 21011010"""    
    def createcustomer(self, book_name, book_last, book_phone, book_email, book_card, book_expdate, book_cvv):
        print("CUSTOMER")
        cursor = self.conn.cursor()
        book_expdate = str(book_expdate.strftime("%m/%y"))
        book_phone = str(book_phone)
        
        print(book_expdate, type(book_expdate))
        try:
            #cursor.execute('''INSERT INTO Customer (name, surname, phone, email, cardNumber, expiryDate, CVV) VALUES ('test', 'test', 12345678901, 'test', 1234567890123, 1/25, 123)''')
            cursor.execute("INSERT INTO Customer (name, surname, phone, email, cardNumber, expiryDate, CVV) VALUES(?, ?, ?, ?, ?, ?, ?)", (book_name, book_last, book_phone, book_email, book_card, "1/25", book_cvv))
            self.conn.commit()
            newcusid = (self.checkforcustomer())
        except sqlite3.Error as error:
            print(error)
            return 0
        cursor.close()
        return newcusid

    """Cameron Povey 21011010"""    
    def createticket (self, customerId, price,hallType):
        print("TICKET")
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO Ticket (price, hallType, customerId, staffId, showId) VALUES (?, ?, ?, ?, ?)", (price, hallType, customerId, self.staffid, self.showid))
            self.conn.commit()
        except sqlite3.Error as error:
            print(error)
            return 0
        cursor.close()
        return 1
    
    """Cameron Povey 21011010"""    
    def relocstaff(self):
        print("RELOCSTAFF")
        cursor = self.conn.cursor()
        findstaff = self.conn.execute("SELECT username FROM staff WHERE Id = '%s'" % (self.staffid))
        findloc = self.conn.execute("SELECT location FROM Cinema WHERE Id = '%s'" % (self.cinemaid))
        staffun = findstaff.fetchone()[0]
        locname = findloc.fetchone()[0]
        cursor.close()
        return [locname,staffun]

    







    
