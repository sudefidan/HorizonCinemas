import sqlite3
from datetime import datetime

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

    









    
    