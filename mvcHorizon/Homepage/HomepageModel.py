"""Sude Fidan 21068639"""
import sqlite3

class HomepageModel:
    def __init__(self):
        self = self

    def get_films(self):
        #open database
        self.conn = sqlite3.connect('database/horizoncinemas.db')
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.execute('SELECT * from Film')
        self.records = cursor.fetchall()
        return self.records
    
    def get_film_dict(self, records,film ):
        return str(f"Film Name: {records[film][1]}\nCast: {records[film][2]}\nDescription: {records[film][6]}\n\nRating: {records[film][3]}\nGenre: {records[film][4]}\nRelease Year: {records[film][5]}\nDuration: {records[film][7]}\nAge Rating: {records[film][8]}")
    
    def show_selection(self,value):
        cursor = self.conn.execute("SELECT * from Show WHERE filmId = ?", (value,))
        records = cursor.fetchall()
        #TODO: ERROR -DOESN'T GET ALL AVAILABLE
        for listing in records:
            listing_table = listing[1],listing[2],listing[3]
        return str(listing_table)
        





    
