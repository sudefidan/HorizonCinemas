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
        self.cur = self.conn.cursor()
        if city == '' or location == '' or seatEntry == '':
            #TODO: MESSAGE BOX SHOULD BE IN VIEW
             messagebox.showerror(title = 'Error',message='Please enter all fields')
        else:
            self.cur.execute("INSERT INTO cinema VALUES (NULL,?, ?)",(city, location))
            self.conn.commit()
            #adds data to screen table
            cinemaID = self.cur.lastrowid
            for i in range(len(seatEntry)):
                self.cur.execute("INSERT INTO Screen VALUES (NULL,?,?,?)",(seatEntry[i].get(),cinemaID,i+1))
                self.conn.commit()
            #TODO: MESSAGE BOX SHOULD BE IN VIEW
            messagebox.showinfo(title='Complete', message='Data added to database successfully')
            self.cur.close()
    
    






    
    