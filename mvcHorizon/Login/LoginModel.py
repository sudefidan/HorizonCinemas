import sqlite3
from Entities.User import User

class LoginModel:
    def __init__(self):
        self = self
        
    def login(self, username, password):
        #get login data
        if username=='' or password=='':
            raise ValueError(f'Username or password cannot be empty!')
        else:
            #open database
            conn = sqlite3.connect('database/horizoncinemas.db')
            #select query
            cursor = conn.execute('SELECT * from staff where USERNAME="%s" and PASSWORD="%s"'%(username,password))
            #fetch data 
            userDict = cursor.fetchone()
            if userDict:
                return User(userDict[0], userDict[1],userDict[2],userDict[3],userDict[4])
            else:
                raise ValueError(f"Wrong username or password!")