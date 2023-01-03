from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkinter.messagebox import showinfo

import sqlite3
import numpy as np

#connect to db
con = sqlite3.connect('database/horizoncinemas.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

#configure window
window = tk.Tk() 
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

def select_film(x):
    recordsShow = []
    value = movieFrame.curselection()[0]
    templist = (f"Film Name: {records[value][1]}\nCast: {records[value][2]}\nDescription: {records[value][6]}\n\nRating: {records[value][3]}\nGenre: {records[value][4]}\nRelease Year: {records[value][5]}\nDuration: {records[value][7]}\nAge Rating: {records[value][8]}")
    
    textOutput.delete(1.0,'end')
    for t in templist:
        textOutput.insert('end',t)

        #table
        sqlShows = """SELECT * from Show WHERE filmId = ?"""
        tree.delete(*tree.get_children()) #clear tree
        for listing in cur.execute(sqlShows, [value+1]):
            listing_table = listing[1],listing[2],listing[3]
            tree.insert('', END, values=listing_table)


#row 1
scrollbar = tk.Scrollbar(window, orient="vertical")
movieFrame=Listbox(window,bg = "light blue",selectbackground="grey",activestyle = 'dotbox',yscrollcommand=scrollbar.set)
movieFrame.grid(row=1,column=0,sticky='NESW')
scrollbar.config(command=movieFrame.yview)

textOutput = Text(window,bg = "light blue",wrap=WORD)
textOutput.grid(row=1,column=1,sticky='NESW')

#get data from db for movie names
cur = cur.execute("SELECT * from Film")
records = cur.fetchall()

for row in records:
    movieName=row[1]
    movieFrame.insert('end',movieName)

#correlate user selection to data from database        
movieFrame.bind('<<ListboxSelect>>',select_film)

#row 2
columns = ('date', 'time', 'screenid')
tree = ttk.Treeview(window, columns=columns, show='headings')
tree.grid(row = 2,column=1,sticky = "NSWE")
tree.heading('date', text='Date')
tree.heading('time', text='Time')
tree.heading('screenid', text='Screen')
   
window.mainloop()