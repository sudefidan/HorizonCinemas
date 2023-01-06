import sqlite3
from datetime import datetime
from collections import Counter
import pandas as pd

class GenerateReportModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('database/horizoncinemas.db')

    """Sude Fidan 21068639"""  
    def date_format(self, date):
        return datetime.utcfromtimestamp(date/1000).strftime("%d/%m/%Y")
    
    """Fiorella Scarpino 21010043"""
    def get_ticket_show_report(self):
        #gets ticket data
        ticketListReport = []
        showListReport = []
        #gets all the tickets
        cur = self.conn.execute("SELECT * from Ticket")
        records = cur.fetchall()
        for listing in records:
            ticketListReport.append(listing[5])
        for i in range(len(ticketListReport)): 
            self.countAmount = dict(Counter(ticketListReport))
        #gets the id of the shows   
        for x in self.countAmount:
            cur1 = self.conn.execute("SELECT * from Show WHERE id = ?",(x,))
            showrecords = cur1.fetchall()
            for records in showrecords:
                #gets the shows that correlate with the tickets and the count of the tickets
                showListReport.append([[self.date_format(records[1])],records[2],records[3],records[4],self.countAmount[x]])
        cur.close()
        cur1.close()
        return showListReport,self.countAmount

    """Fiorella Scarpino 21010043"""
    def get_monthly_cinema_report(self):
        cinemaListMonthly = []
        self.tempDbColumns = []
        dbColumns = []

        #gets price and showid from ticket
        self.curForMonthly = self.conn.execute("SELECT * from Ticket")
        ticketRecords = self.curForMonthly.fetchall()
        for i in ticketRecords:
            cinemaListMonthly.append([i[1],i[5]])
        self.getDbRowforMonthlyCinema()
        dbColumns.extend([self.tempDbColumns[1],self.tempDbColumns[5]])
        self.tempDbColumns.clear()
       
        #get screenid and date from show
        for x in range(len(cinemaListMonthly)):
            self.curForMonthly = self.conn.execute("SELECT * from Show WHERE id = ?",(cinemaListMonthly[x][1],))
            showRecords = self.curForMonthly.fetchall()
            for i in showRecords:
                cinemaListMonthly[x].extend([self.date_format(i[1]),i[3]])
        self.getDbRowforMonthlyCinema()
        dbColumns.extend([self.tempDbColumns[1],self.tempDbColumns[3]])
        self.tempDbColumns.clear()
     
        #get cinema from screen
        for x in range(len(cinemaListMonthly)):
            self.curForMonthly = self.conn.execute("SELECT * from Screen WHERE id = ?",(cinemaListMonthly[x][3],))
            screenRecords = self.curForMonthly.fetchall()
            for i in screenRecords:
                cinemaListMonthly[x].extend([i[2]])
        self.getDbRowforMonthlyCinema()
        dbColumns.extend([self.tempDbColumns[2]])
        self.tempDbColumns.clear()

        #get city and location from cinema
        for x in range(len(cinemaListMonthly)):
            self.curForMonthly = self.conn.execute("SELECT * from Cinema WHERE id = ?",(cinemaListMonthly[x][4],))
            cinemaRecords = self.curForMonthly.fetchall()
            for i in cinemaRecords:
                cinemaListMonthly[x].extend([i[1],i[2]])
        self.getDbRowforMonthlyCinema()
        dbColumns.extend([self.tempDbColumns[1],self.tempDbColumns[2]])
        self.tempDbColumns.clear()
        #creates dataframe to calculate monthly revenue
        df = pd.DataFrame(cinemaListMonthly, columns =dbColumns) 
        tempPD = df.groupby([pd.to_datetime(df['date'],dayfirst =True).dt.month,'city','location'])
        monthlyCinemaGet = tempPD['price'].sum().reset_index()
        self.curForMonthly.close()
        return monthlyCinemaGet

    """Fiorella Scarpino 21010043"""
    def getDbRowforMonthlyCinema(self):
        for column in self.curForMonthly.description:
            self.tempDbColumns.append(column[0])
        return self.tempDbColumns