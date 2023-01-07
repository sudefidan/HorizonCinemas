"""Sude Fidan 21068639"""
"""Cameron Povey 21011010"""
import sqlite3
from datetime import datetime
import numbers

class ManageScreeningModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('database/horizoncinemas.db')

    """Sude Fidan 21068639"""  
    def commit_add_film(self,name, cast,rating,genre,year, description, duration, age):
        if name=='' or cast=='' or rating == '' or genre =='' or year == '' or description =='' or duration == '' or age=='':
            return 3
        elif isinstance(float(rating), numbers.Number) and isinstance(float(year), numbers.Number) and isinstance(float(duration), numbers.Number) and isinstance(float(age), numbers.Number):
            try:
                
                    cursor = self.conn.cursor()
                    # check if a row is already exist 
                    cursor.execute("SELECT id FROM Film WHERE name = ?", (name,))
                    db_result=cursor.fetchall()
                    if len(db_result)==0:
                        cursor.execute("INSERT INTO Film (name, cast, rating, genre, releaseYear, description, duration, ageRating) VALUES (?,?, ?, ?, ?, ?,?,?)",(name, cast,rating,genre, year, description,duration,age))
                        self.conn.commit()
                        cursor.close()
                        return 1
                    else:
                        print('Film %s found with id %s'%(name,','.join(map(str, next(zip(*db_result))))))
                        return 0     
            except:
                return 0
        else:
            return 2
                
    """Sude Fidan 21068639"""  
    def commit_remove_film(self,name):
        cursor = self.conn.cursor()
        if name =='':
            return 3
        else:
            try:
                cursor.execute("SELECT id FROM Film WHERE name = ?", (name,))
                db_result=cursor.fetchall()
                if len(db_result)==1:
                    cursor.execute("DELETE FROM Film WHERE name = '%s'" % (name))
                    cursor.close()
                    self.conn.commit()
                    return 1
                else :
                    print('Film could not found with name = %s'%(name))
                    return 2
            except:
                cursor.close()
                self.conn.commit()
                return 0
        