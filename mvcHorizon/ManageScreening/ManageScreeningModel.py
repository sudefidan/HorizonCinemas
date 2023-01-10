"""Sude Fidan 21068639"""
"""Cameron Povey 21011010"""
"""Fiorella Scarpino 21010043"""
import sqlite3
from datetime import datetime
import numbers

class ManageScreeningModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect(r'C:\Users\maria\Downloads\HorizonCinemas11111\HorizonCinemas-main\mvcHorizon\database\horizoncinemas.db')

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
    def get_show_times(self, showId):
        showReturn = []
        self.changedShowId = showId
        
        cursor = self.conn.execute("SELECT * FROM Show WHERE Id = '%s'" % (self.changedShowId))
        showInfo = cursor.fetchone()
        if showInfo == None: return 0
        
        showReturn.append(showInfo[0])
        showReturn.append(datetime.utcfromtimestamp(showInfo[1]/1000).strftime("%d/%m/%Y"))
        showReturn.append(showInfo[2])
        
        screen = (self.conn.execute("SELECT cinemaID FROM Screen WHERE Id = '%s'" % (showInfo[3]))).fetchone()[0]
        showReturn.append((self.conn.execute("SELECT location FROM Cinema WHERE Id = '%s'" % (screen))).fetchone()[0])
        showReturn.append((self.conn.execute("SELECT name FROM Film WHERE Id = '%s'" % (showInfo[4]))).fetchone()[0])
        
        cursor.close()
        return showReturn
    
    """Cameron Povey 21011010"""
    def confirm_change(self, date, hour, min):
        cursor = self.conn.cursor()
        
        if int(min) == str(00): pass
        elif int(min) < 10: min = str(0) + str(min)
        time = str(hour) + ":" + str(min)
        
        date = datetime.strptime(date, "%d/%m/%Y")
        date = date.strftime("%m/%d/%Y, %H:%M:%S")
        formatedDate = datetime.strptime(date,"%m/%d/%Y, %H:%M:%S")
        self.timeStamp = int(datetime.timestamp(formatedDate))*1000
        
        cursor.execute("UPDATE Show SET date = ?, time = ? WHERE Id = ?", (int(self.timeStamp),time,self.changedShowId))
        cursor.close()
        self.conn.commit()
        return 0
    
    def fetch_screen_numbers(self, showId):
        showReturn = []
        self.attachedShowId = showId
        
        cursor = self.conn.execute("SELECT * FROM Show Where Id = '%s'" % (self.attachedShowId))
        showInfo = cursor.fetchone()
        
        if showInfo == None: return 0
        
        showReturn.append(showInfo[0])
        showReturn.append(datetime.utcfromtimestamp(showInfo[1]/1000).strftime("%d/%m/%Y"))
        showReturn.append(showInfo[2])
        showReturn.append((self.conn.execute("SELECT name FROM Film WHERE Id = '%s'" % (showInfo[4]))).fetchone()[0])
        
        cursor.close()
        return showReturn
    
    def commit_change(self, screenId):
        cursor = self.conn.cursor()
        screenFetch = self.conn.execute("SELECT Id FROM Screen WHERE Id = '%s'" % (screenId))
        screenCheck = screenFetch.fetchone()
        if screenCheck == None: return False
        cursor.execute("UPDATE Show SET screenId = ? WHERE Id = ?", (screenId, self.attachedShowId))
        self.conn.commit()
        cursor.close()
        screenFetch.close()
        return 1

    """Fiorella Scarpino 21010043"""
    def createNewFilm(self):
        self.listOfFilms = []
        #get film
        self.curCreateNewShows = self.conn.execute("SELECT * from Film")
        filmNewShow = self.curCreateNewShows.fetchall()
        for i in filmNewShow:
            self.listOfFilms.append([i[0],i[1]]) #id and location
        self.curCreateNewShows.close()
        return self.listOfFilms

    """Fiorella Scarpino 21010043"""
    def createNewCinema(self):
        self.listOfCinemas = []
        #get cinema
        self.curCreateNewShowscinema = self.conn.execute("SELECT * from Cinema")
        cinemaNewShow = self.curCreateNewShowscinema.fetchall()
        for i in cinemaNewShow:
            self.listOfCinemas.append([i[0],i[2]]) #id and location
        self.curCreateNewShowscinema.close()
        return self.listOfCinemas

    """Fiorella Scarpino 21010043"""
    def createNewScreen(self,userSelectionNewShows):
        #get screeen
        self.listOfScreens = []
        userChoice = userSelectionNewShows[0]
        self.curCreateNewscreen = self.conn.execute("SELECT * from Screen WHERE cinemaID = ?",(userChoice,))
        screenNewShow = self.curCreateNewscreen.fetchall()
        for i in screenNewShow:
            self.listOfScreens.append([i[0],i[3]]) #id and screen number 
        self.curCreateNewscreen.close()
        return self.listOfScreens

    """Fiorella Scarpino 21010043"""
    def addDataForNewShow(self,newDateForShow,newTimeShow,screenUserShow,userSelectionNewShowsName):
        print(newDateForShow,newTimeShow,screenUserShow,userSelectionNewShowsName)
        self.conn.row_factory = sqlite3.Row
        self.cursornewdata = self.conn.cursor()
        self.cursornewdata.execute("INSERT INTO Show VALUES (NULL,?, ?, ?, ?)",(newDateForShow,newTimeShow,screenUserShow[0],userSelectionNewShowsName))
        self.conn.commit()
