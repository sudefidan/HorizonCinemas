import sqlite3
from datetime import datetime
from tkinter import messagebox
from collections import Counter

class HomepageModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('database/horizoncinemas.db')

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


    """Fiorella Scarpino 21010043"""
    #add new cinema to the database
    def getCinemaNew(self, city,location,seatEntry):
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        if city == '' or location == '' or seatEntry == '':
             messagebox.showerror(title = 'Error',message='Please enter all fields')
        else:
            self.cur.execute("INSERT INTO cinema VALUES (NULL,?, ?)",(city, location))
            self.conn.commit()
            #adds data to screen table
            cinemaID = self.cur.lastrowid
            for i in range(len(seatEntry)):
                self.cur.execute("INSERT INTO Screen VALUES (NULL,?,?,?)",(seatEntry[i].get(),cinemaID,i+1))
                self.conn.commit()
            messagebox.showinfo(title='Complete', message='Data added to database successfully')
            self.cur.close()

    """Fiorella Scarpino 21010043"""
    def ticketAndShowDb(self):
        #gets ticket data
        ticketListReport = []
        showListReport = []
        #gets all the tickets
        cur = self.conn.execute("SELECT * from Ticket")
        records = cur.fetchall()
        for listing in records:
            ticketListReport.append(listing[5])
        for i in range(len(ticketListReport)): 
            self.countAmount = dict(Counter(ticketListReport))
        #gets the id of the shows   
        for x in self.countAmount:
            cur1 = self.conn.execute("SELECT * from Show WHERE id = ?",(x,))
            showrecords = cur1.fetchall()
            for records in showrecords:
                #gets the shows that correlate with the tickets and the count of the tickets
                showListReport.append([[self.date_format(records[1])],records[2],records[3],records[4],self.countAmount[x]])
        cur.close()
        cur1.close()
        return showListReport,self.countAmount
    

    """Sude Fidan 21068639""" 
    
"""
    def add_film(self,filmName, filmCast, filmRating, filmGenre, filmYear, filmDescription, filmDuration, filmAge):
        cursor = self.conn.execute("INSERT INTO Film (name, cast, rating, genre, releaseYear, description, duration, ageRating) VALUES (filmName, filmCast, filmRating, filmGenre, filmYear, filmDescription, filmDuration, filmAge)" )
    def remove_film(self, filmName):
        cursor = self.conn.execute("DELETE FROM Film WHERE name="%s"%(filmName))
    """

    



    
    



    
    
