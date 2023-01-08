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
        self.conn = sqlite3.connect('mvcHorizon/database/horizoncinemas.db')

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
    
    """Cameron Povey 21011010"""
    def getShowTimes(self, showid):
        showreturn = []
        self.UST_showid = showid
        
        fetchShow = self.conn.execute("SELECT * FROM Show WHERE Id = '%s'" % (self.UST_showid))
        showInfo = fetchShow.fetchone()
        if showInfo == None: return 0
        
        showreturn.append(showInfo[0])
        showreturn.append(datetime.utcfromtimestamp(showInfo[1]/1000).strftime("%d/%m/%Y"))
        showreturn.append(showInfo[2])
        
        screen = (self.conn.execute("SELECT cinemaID FROM Screen WHERE Id = '%s'" % (showInfo[3]))).fetchone()[0]
        showreturn.append((self.conn.execute("SELECT location FROM Cinema WHERE Id = '%s'" % (screen))).fetchone()[0])
        showreturn.append((self.conn.execute("SELECT name FROM Film WHERE Id = '%s'" % (showInfo[4]))).fetchone()[0])
        
        fetchShow.close()
        return showreturn
    
    """Cameron Povey 21011010"""
    def confirmChange(self, date, timeh, timem):
        cursor = self.conn.cursor()
        
        if int(timem) == str(00): pass
        elif int(timem) < 10: timem = str(0) + str(timem)
        time = str(timeh) + ":" + str(timem)
        
        date = datetime.strptime(date, "%d/%m/%Y")
        date = date.strftime("%m/%d/%Y, %H:%M:%S")
        formated_date = datetime.strptime(date,"%m/%d/%Y, %H:%M:%S")
        self.timestamp = int(datetime.timestamp(formated_date))*1000
        
        cursor.execute("UPDATE Show SET date = ?, time = ? WHERE Id = ?", (int(self.timestamp),time,self.UST_showid))
        cursor.close()
        self.conn.commit()
        return 0
    
    def fetchScreenNumbers(self, showId):
        showReturn = []
        self.ASVshowId = showId
        
        showfetch = self.conn.execute("SELECT * FROM Show Where Id = '%s'" % (self.ASVshowId))
        showInfo = showfetch.fetchone()
        
        if showInfo == None: return 0
        
        showReturn.append(showInfo[0])
        showReturn.append(datetime.utcfromtimestamp(showInfo[1]/1000).strftime("%d/%m/%Y"))
        showReturn.append(showInfo[2])
        showReturn.append((self.conn.execute("SELECT name FROM Film WHERE Id = '%s'" % (showInfo[4]))).fetchone()[0])
        
        showfetch.close()
        return showReturn
    
    def commitChange(self, screenId):
        cursor = self.conn.cursor()
        screenFetch = self.conn.execute("SELECT Id FROM Screen WHERE Id = '%s'" % (screenId))
        screenCheck = screenFetch.fetchone()
        if screenCheck == None: return False
        cursor.execute("UPDATE Show SET screenId = ? WHERE Id = ?", (screenId, self.ASVshowId))
        self.conn.commit()
        cursor.close()
        screenFetch.close()
        return 1