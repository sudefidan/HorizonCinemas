import tkinter as tk
from models import Model
from views import View
from datetime import datetime

class Controller():
    def __init__(self):
        self.root = tk.Tk()
        
        self.model = Model()
        self.view = View(self.root, self)
        
        self.root.geometry('1000x1000')
        self.root.mainloop()
        
    def topinfo(self):
        return self.model.relocstaff()
        
    def getfilms(self):
        print("FETCHING FILM LIST")
        return self.model.filmlist()
    
    def showlist(self, film, date):
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.showings = self.model.getshowings(film, self.date)
        print("RETRIEVED")
        return self.showings
    
    def checktypes(self, time):
        self.remaining = []
        self.time = time
        print("TIME: ", self.time)
        if self.time == "SELECT SHOW TIME": return None
        self.ids_for_type = self.model.getids(self.time)
        print(self.ids_for_type)
        print("GETTING FILLED")
        self.filled = self.model.filled()
        print("GETTING MAXs")
        self.typemax = self.model.typesmax()
        for i in range(3):
            self.remaining.append(self.typemax[i] - self.filled[i])
        return self.remaining
        
    def cost(self, type, amount):
        if self.time == "SELECT SHOW TIME": return None
        
        self.timepoint = ["MORNING", "AFTERNOON", "EVENING"]
        self.timechange = ['12:00:00', '17:00:00', '23:59:59'] #end times
        self.type = type
        self.dt_change = []
        self.type_change = [1, 1.2, 1.44]
        
        #convert times to datetime format
        self.adtime = str(self.time)+str(':00')
        self.dt_time = datetime.strptime(self.adtime, '%H:%M:%S').time()
        for i in range(3):
            self.timechange[i] = datetime.strptime(str(self.timechange[i]), '%H:%M:%S').time()
        
        for i in range(3):
            if (self.dt_time.hour < self.timechange[i].hour):
                self.timeframe = self.timepoint[i]
                break
            if (self.dt_time.hour == self.timechange[i].hour):
                if (self.dt_time.minute > self.timechange[i].minute):
                    self.timeframe = self.timepoint[i+1]
                else:
                    self.timeframe = self.timepoint[i]
                break
            
        print(self.timeframe)
        pricelow = self.model.getstand(self.timeframe)
        priceper = pricelow * self.type_change[type]
        print(amount)
        self.ovrprice = priceper * int(amount)
        print(pricelow)
        print(priceper)
        print(self.ovrprice)
        return self.ovrprice

    def bookfilm(self, book_name, book_last, book_phone, book_email, book_card, book_expdate, book_cvv):
        self.halllist = ["LOWER HALL", "UPPER HALL", "VIP"]
        self.halltype = self.halllist[self.type]
        checkifcustomer = self.model.checkforcustomer(book_name, book_last, book_phone, book_email, book_card, book_expdate, book_cvv)
        if checkifcustomer != 0: c_cus = checkifcustomer
        else:
            c_cus = self.model.createcustomer(book_name, book_last, book_phone, book_email, book_card, book_expdate, book_cvv)
        c_tick = self.model.createticket(c_cus,self.ovrprice,self.halltype)
        if c_tick == 1:
            print("SUCCESS!")
            
            
if __name__ == '__main__':
    app = Controller()