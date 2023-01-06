import sqlite3
from datetime import datetime

class ManageScreeningModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('database/horizoncinemas.db')
    
    """Sude Fidan 21068639"""  
    def date_format(self, date):
        return datetime.utcfromtimestamp(date/1000).strftime("%d/%m/%Y")

    def add_film(self,name, cast,rating,genre,year, description, duration, age):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Film VALUES(?, ?,?, ?, ?, ?, ?,?)",(name, cast,rating,genre, year, description,duration,age))
        self.conn.commit()
        