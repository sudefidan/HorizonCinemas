"""Sude Fidan 21068639"""
"""Cameron Povey 21011010"""
"""Fiorella Scarpino 21010043"""
import sqlite3
from datetime import datetime
from tkinter import messagebox   #TODO: MESSAGE BOX SHOULD BE IN VIEW

class HomepageModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('database/horizoncinemas.db')

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
        cursor.execute("INSERT INTO cinema VALUES (NULL,?, ?)",(city, location))
        self.conn.commit()
        #adds data to screen table
        cinemaID = cursor.lastrowid
        for i in range(len(seatEntry)):
            cursor.execute("INSERT INTO Screen VALUES (NULL,?,?,?)",(seatEntry[i].get(),cinemaID,i+1))
            self.conn.commit()
        cursor.close()

    """Cameron Povey 21011010"""
    def get_films_cinema(self, location):
        self.strscrList = ""
        self.strfilmRef = ""
        screenList = []
        filmRef = []
        filmArr = []

        #get cinema ID
        cinemasCursor = self.conn.execute("SELECT id FROM Cinema WHERE location = '%s'" % (location))
        self.cinId = cinemasCursor.fetchone()
        if self.cinId == None: return 0
        self.cinId = self.cinId[0]
        #fetch list of screens from cinema location
        screensCursor = self.conn.execute("SELECT id FROM Screen WHERE cinemaID = '%s'" % (self.cinId))
        scr = screensCursor.fetchall()
        
        #add them to a str list
        for i in range (len(scr)):
            screenList.append(scr[i][0])
            if i == 0: self.strscrList = str(screenList[i])
            else: self.strscrList = str(self.strscrList) + ", " + str(screenList[i])
        
        #get filmIds from show which have the screenIds found before 
        filmIdCursor = self.conn.execute("SELECT filmId FROM Show WHERE screenId IN (%s)" % (self.strscrList))
        filmIds = filmIdCursor.fetchall()
        
        #add them to another str list
        for i in range(len(filmIds)):
            filmRef.append(filmIds[i][0])
        filmRef = list(dict.fromkeys(filmRef))
        
        for i in range(len(filmRef)):
            if i == 0: self.strfilmRef = str(self.strfilmRef) + str(filmRef[i])
            else: self.strfilmRef = str(self.strfilmRef) + ", " + str(filmRef[i])
        
        #get film names that are showing in the cinema
        filmFindCursor = self.conn.execute("SELECT name FROM Film WHERE Id IN (%s)" % (self.strfilmRef))
        films = filmFindCursor.fetchall()
        
        #add them to array to return
        for i in range (len(films)):
            filmArr.append(films[i][0])
            
        cinemasCursor.close()
        screensCursor.close()
        filmIdCursor.close()
        filmFindCursor.close()
        
        return(filmArr)
    
    """Cameron Povey 21011010"""
    def existed_showing(self,film,date):
        self.bookingDate = self.get_timestamp(datetime.strptime(date, "%d/%m/%Y"))
        showArr = []
        self.selectedFilm = film
        findICursor = self.conn.execute("SELECT id FROM Film WHERE name = '%s'" % (film))
        self.selectedFilmId = findICursor.fetchone()
        if self.selectedFilmId == None: return 0
        
        showfFindCursor = self.conn.execute("SELECT time FROM Show WHERE filmId='%s' AND screenId IN (%s) AND date = '%s'" % (self.selectedFilmId, self.strscrList, self.bookingDate))
        showings = showfFindCursor.fetchall()
        
        for i in range (len(showings)): showArr.append(showings[i][0])
        
        findICursor.close()
        showfFindCursor.close()
        
        return showArr
    
    """Cameron Povey 21011010"""
    def update_type(self,time):
        remaining = []
        point = ["LOWER HALL", "UPPER HALL", "VIP"]
        filled = [0,0,0]
        maxSeat = [0,0,0]
        
        self.bookingTime = time
        if self.bookingTime == "SELECT SHOW TIME": return None

        screenStateCursor = self.conn.execute("SELECT id FROM Show WHERE time='%s' AND filmId='%s' AND date = '%s'" % (self.bookingTime, self.selectedFilmId, self.bookingDate))
        self.bookedShowId = screenStateCursor.fetchone()[0]
        
        for i in range(3):
            lowHallAmountCursor = self.conn.execute("SELECT Id FROM Ticket WHERE showId='%s' AND hallType = '%s'" % (self.bookedShowId, point[i]))
            filled[i] = len(lowHallAmountCursor.fetchall())
        
        fetchShowCursor = self.conn.execute("SELECT screenId FROM Show WHERE Id='%s'" % (self.bookedShowId))
        screen = fetchShowCursor.fetchone()[0]
        fetchCapacityCursor = self.conn.execute("SELECT SeatingCapacity FROM Screen WHERE Id='%s'" % (screen))
        screenCapacity = fetchCapacityCursor.fetchone()[0]
        
        maxSeat[0] = int(screenCapacity * 0.3)
        maxSeat[1] = int((screenCapacity - maxSeat[0]) - 10)
        maxSeat[2] = screenCapacity - (maxSeat[1] + maxSeat[0])
        
        for i in range(3):
            remaining.append(maxSeat[i] - filled[i])
            
        screenStateCursor.close()
        lowHallAmountCursor.close()
        fetchShowCursor.close()
        fetchCapacityCursor.close()
        return remaining
    
    """Cameron Povey 21011010"""
    def calculate_cost(self, typeSelection, amount):
        if self.bookingTime == "SELECT SHOW TIME": return None
        
        timepoint = ["MORNING", "AFTERNOON", "EVENING"]
        typeChangeDict = [1, 1.2, 1.44]
        
        adTime = str(self.bookingTime)+str(':00')
        dtTime = datetime.strptime(adTime, '%H:%M:%S').time()
        
        #end times
        timeChange = ['12:00:00', '17:00:00', '23:59:59']
        for i in range(3):
            timeChange[i] = datetime.strptime(str(timeChange[i]), '%H:%M:%S').time()
            
        for i in range(3):
            if (dtTime.hour < timeChange[i].hour):
                timeFrame = timepoint[i]
                break
            if (dtTime.hour == timeChange[i].hour):
                if (dtTime.minute > timeChange[i].minute):
                    timeFrame = timepoint[i+1]
                else:
                    timeFrame = timepoint[i]
                break
        priceCursor = self.conn.execute("SELECT price FROM Ticket_Pricing WHERE cinemaId = '%s' AND  showTimeType = '%s'" % (self.cinId, timeFrame))
        standardPrice = priceCursor.fetchone()[0]
        
        priceper = standardPrice * typeChangeDict[typeSelection]
        self.overprice = priceper * int(amount)
        priceCursor.close()
        self.selectedType = typeSelection
        return self.overprice
    
    """Cameron Povey 21011010"""
    def book_film(self, fname, lname, phone, email, card, exp, cvv, staffId, tickCount):
        hallList = ["LOWER HALL", "UPPER HALL", "VIP"]
        hallType = hallList[self.selectedType]
        cursor = self.conn.cursor()
        
        #check for customer
        customerId = self.check_customer(fname, lname, phone, email)
        #create customer if doesnt exist
        if customerId == None:
            customerId = self.create_customer(fname, lname, phone, email, card, exp, cvv)
        #create ticket
        customerId = customerId[0]
        for i in range(int(tickCount)):
            cursor.execute("INSERT INTO Ticket (price, hallType, customerId, staffId, showId) VALUES (?, ?, ?, ?, ?)", (str(self.overprice/tickCount), hallType, customerId, staffId, self.bookedShowId))
        cursor.close()
        self.conn.commit()
        
        idList=[]
        onePriceFetch = self.conn.execute("SELECT Price FROM Ticket WHERE customerId = '%s' AND showId = '%s'" % (customerId, self.bookedShowId))
        onePrice = onePriceFetch.fetchall()
        returnTicketInfoCursor = self.conn.execute("SELECT Id FROM Ticket WHERE customerId = '%s' AND showId = '%s'" % (customerId, self.bookedShowId))
        returnTicketInfo = returnTicketInfoCursor.fetchall()
        for i in range(len(returnTicketInfo)):
            idList.append(returnTicketInfo[i][0])
        returnTicketInfoCursor.close()
        return [idList, onePrice, self.selectedFilm]
    
    """Cameron Povey 21011010"""
    def create_customer(self, fname, lname, phone, email, card, exp, cvv):
        expiryDate = str(exp.strftime("%m/%y"))
        phoneNo = str(phone)
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Customer (name, surname, phone, email, cardNumber, expiryDate, CVV) VALUES(?, ?, ?, ?, ?, ?, ?)", (fname, lname, phoneNo, email, card, expiryDate, cvv))
        cursor.close()
        self.conn.commit()
        return self.check_customer(fname, lname, phone, email)
    
    """Cameron Povey 21011010"""
    def check_customer(self, fname, lname, phone, email):
        checkStateCursor = self.conn.execute("SELECT Id FROM Customer WHERE name = '%s' AND surname = '%s' AND phone = '%s' AND email = '%s'" % (fname, lname, phone, email))
        customerState = checkStateCursor.fetchone()
        checkStateCursor.close()
        return (customerState)

    """Cameron Povey 21011010"""
    def get_film_info(self, bookId):
        cursorBooking = self.conn.execute("SELECT * FROM Ticket WHERE Id = '%s'" % (bookId))
        self.allbooks = cursorBooking.fetchall()

        if self.allbooks == None: return 0
        self.bookingInfo = []

        for i in range(len(self.allbooks[0])):
            if i == 2: self.bookingInfo.append((self.allbooks[0][1])*len(self.allbooks))
            else: self.bookingInfo.append(self.allbooks[0][i])

        cursorCustomer= self.conn.execute("SELECT * FROM Customer WHERE Id = '%s'" % (self.bookingInfo[3]))
        customerInfo = cursorCustomer.fetchone()

        cursorStaff = self.conn.execute("SELECT username FROM staff WHERE Id = '%s'" % (self.bookingInfo[4]))
        staffInfo = cursorStaff.fetchone()

        cursorFilm = self.conn.execute("SELECT * FROM Film WHERE Id = '%s'" % (self.bookingInfo[5]))
        filmInfo = cursorFilm.fetchone()
        showGet = self.allbooks[0][5]

        cursorfindstaff = self.conn.execute("SELECT Id FROM staff WHERE Id = '%s'" % (self.bookingInfo[4]))
        staffid = cursorfindstaff.fetchone()

        cursorallids = self.conn.execute("SELECT Id FROM Ticket WHERE customerId = '%s' AND staffId = '%s' AND showId = '%s'" % (customerInfo[0], staffid[0],showGet))
        self.allids = cursorallids.fetchone()
        cursorBooking.close()
        return [self.bookingInfo, customerInfo, staffInfo, filmInfo]
    
    """Cameron Povey 21011010"""
    def cancel_cost(self):
        todayTime = self.get_today_unix()
        
        cursor = self.conn.execute("SELECT date, time FROM Show WHERE Id = '%s'" % (self.bookingInfo[5]))
        selectedTimeAndDate = cursor.fetchone()
        h, m = selectedTimeAndDate[1].split(':')
        
        timems = int(h)*3600000 + int(m)*60000
        selectedTimeAndDate = int(selectedTimeAndDate[0]) + int(timems)
        cursor.close()
        
        if selectedTimeAndDate < (int(todayTime) + 86400000): return "SAME_DAY"
        elif selectedTimeAndDate < (int(todayTime) + 172800000): return "DAY_PRIOR"
        else: return "CANCEL_FREE"
    
    """Cameron Povey 21011010"""
    def commit_cancel(self):
        cursor = self.conn.cursor()
        idStr = []
        for i in range(len(self.allids)):
            idStr.append(self.allids[i][0])
            if i == 0: idStr = str(self.allids[i])
            else: idStr = str(idStr) + ", " + str(self.allids[i])
        try:
            cursor.execute("DELETE FROM Ticket WHERE Id IN '%s'" % (idStr))
            cursor.close()
            self.conn.commit()
            return 1
        except:
            cursor.close()
            self.conn.commit()
            return 0
    
    def get_cinemas(self):
        cursorCinemas = self.conn.execute("SELECT location FROM Cinema")
        cinemaList = cursorCinemas.fetchall()

        return_cinemas = []
        for i in range(len(cinemaList)):
            return_cinemas.append(cinemaList[i][0])
        return return_cinemas
        
    
    






    
    
