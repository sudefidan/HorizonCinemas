"""Sude Fidan 21068639"""
import sqlite3
from Entities.User import User
import os
import hashlib

class LoginModel:
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('mvcHorizon/database/horizoncinemas.db')
        
    def login(self, username, password):
        #get login data
        if username=='' or password=='':
            raise ValueError(f'Username or password cannot be empty!')
        else:
            #encryption
            password_crypt = hashlib.sha256((password).encode()).hexdigest()
            #select query
            cursor = self.conn.execute('SELECT * from staff where USERNAME="%s" and PASSWORD="%s"'%(username,password_crypt))
            #fetch data 
            userDict = cursor.fetchone()
            cursor.close()
            if userDict:
                return User(userDict[0], userDict[1],userDict[2],userDict[3],userDict[4],userDict[5],userDict[6])
            else:
                raise ValueError(f"Wrong username or password!")
            