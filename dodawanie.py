from Tkinter import *
import Tkinter
import Tkinter as tk
import tkMessageBox
import sqlite3 as lite
import sys

con = lite.connect('paliwko.db')

fuel = Tk()
fuel.title("Dodaj Tankowanie")

class Application(Frame):
        
    def dodaj(self):
        print "dodaj!"
        tank = []
        a=licznik.get()
        a1=int(a)
        tank.append(a1)
        b=ilosc.get()
        b1=int(b)
        tank.append(b1)
        c=cena.get()
        c1=int(c)
        tank.append(c1)
        cur = con.cursor()
        cur.execute("INSERT INTO tankowanie(przebieg, ilosc, koszt) VALUES(?,?,?)", tank)
        licznik.delete(0, 'end')
        ilosc.delete(0, 'end')
        cena.delete(0, 'end')
        with con:    
 			cur.execute("SELECT * FROM tankowanie")
			rows = cur.fetchall()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Koniec programu"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "bottom"})
       
        self.dodaj_tankowanie = Button(self)
        self.dodaj_tankowanie["text"] = "Dodaj",
        self.dodaj_tankowanie["command"] = self.dodaj
        self.dodaj_tankowanie.pack({"side": "top"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

var = StringVar()
label = Label( fuel, textvariable=var)
var.set("Podaj stan licznika.")
label.pack()
licznik = tk.Entry(fuel, width = 30, bg = "white", font = "Helvetica 14")  
licznik.pack()
licznik.focus()


var = StringVar()
label = Label( fuel, textvariable=var)
var.set("Podaj ilosc zatankowanego paliwa.")
label.pack()
ilosc = tk.Entry(fuel, width = 30, bg = "white", font = "Helvetica 14")
ilosc.pack()


var = StringVar()
label = Label( fuel, textvariable=var)
var.set("Podaj koszt paliwa.")
label.pack() 
cena = tk.Entry(fuel, width = 30, bg = "white", font = "Helvetica 14")
cena.pack()

fuel = Application(master=fuel)
fuel.mainloop()
fuel.destroy()
con.close()
