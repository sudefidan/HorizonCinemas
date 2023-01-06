import sqlite3
from datetime import datetime
from collections import Counter

class GenerateReportModel:
    """Sude Fidan 21068639"""
    def __init__(self):
        self = self
        #open database
        self.conn = sqlite3.connect('mvcHorizon/database/horizoncinemas.db')

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