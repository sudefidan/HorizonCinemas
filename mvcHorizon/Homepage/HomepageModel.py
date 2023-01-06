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
            cursor.close()

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
        cpcan_todaytimestamp = self.get_today_unix
        
        #DELETE - JUST TO TEST DATES
        cpcan_formated_date = datetime.strptime("12/4/2022, 08:00:00","%m/%d/%Y, %H:%M:%S") #use backwards date
        self.Unix_timestamp = datetime.timestamp(cpcan_formated_date)
        cpcan_todaytimestamp = int(self.Unix_timestamp)*1000
        print(cpcan_todaytimestamp, "- EMULATED DATE! of:" ,cpcan_formated_date)
        #END DELETE
        
        cursor = self.conn.execute("SELECT date, time FROM Show WHERE Id = '%s'" % (self.bookingInfo[5]))
        cpcan_seltimeanddate = cursor.fetchone()
        h, m = cpcan_seltimeanddate[1].split(':')
        
        timems = int(h)*3600000 + int(m)*60000
        cpcan_seltimeanddate = int(cpcan_seltimeanddate[0]) + int(timems)
        cursor.close()
        
        if cpcan_seltimeanddate < (cpcan_todaytimestamp + 86400000): return "SAME_DAY"
        elif cpcan_seltimeanddate < (cpcan_todaytimestamp + 172800000): return "DAY_PRIOR"
        else: return "CANCEL_FREE"
    
    """Cameron Povey 21011010"""
    def commit_cancel(self):
        cursor = self.conn.cursor()
        try:
            self.cursor.execute("DELETE FROM Ticket WHERE Id = '%s'" % (self.bookingInfo[0]))
            cursor.close()
            self.conn.commit()
            return 1
        except:
            cursor.close()
            self.conn.commit()
            return 0
        
    
    






    
    