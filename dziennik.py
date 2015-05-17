from Tkinter import *
import Tkinter
import Tkinter as tk
import tkMessageBox
import sqlite3 as lite
import sys

con = lite.connect('paliwko.db')
cur = con.cursor()

paliwo = []

fuel = Tk()

fuel.title("Dziennik tankowan")

with con: 
	cur = con.cursor()    
	cur.execute("SELECT * FROM tankowanie")
	rows = cur.fetchall()
	for row in rows:
		paliwo.append(row)
	ost = row
		
with con: 
	cur = con.cursor()    
	cur.execute("SELECT MIN(cena) FROM tankowanie;")
	najtansze_rows = cur.fetchall()
	najtansze = najtansze_rows
	
with con: 
	cur = con.cursor()    
	cur.execute("SELECT MAX(cena) FROM tankowanie;")
	najdrozsze_rows = cur.fetchall()
	najdrozsze = najdrozsze_rows
	
with con: 
	cur = con.cursor()    
	cur.execute("SELECT MAX(ilosc) FROM tankowanie;")
	naj_paliwa_rows = cur.fetchall()
	naj_paliwa = naj_paliwa_rows	

class Application(Frame):
	
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Wstecz"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "bottom"})
                
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

var = StringVar()
label = Label( fuel, textvariable=var)
var.set("Wszystkie tankowania.")
label.pack({"side":"top"})

w_tankowania = Text(fuel, height = 6, width = 42)
w_tankowania.insert(INSERT, paliwo)
w_tankowania.pack({"side":"top"})

var = StringVar()
label = Label( fuel, textvariable=var)
var.set("Ostatnie tankowanie.")
label.pack({"side":"top"})

ost_tankowanie = Text(fuel, height = 1, width = 42)
ost_tankowanie.insert(INSERT, ost)
ost_tankowanie.pack({"side":"top"})

var = StringVar()
label = Label( fuel, textvariable=var)
var.set("Najnizsza cena paliwa.")
label.pack({"side":"top"})

ost_tankowanie = Text(fuel, height = 1, width = 42)
ost_tankowanie.insert(INSERT, najtansze[0])
ost_tankowanie.pack({"side":"top"})

var = StringVar()
label = Label( fuel, textvariable=var)
var.set("Najwyzsza cena paliwa.")
label.pack({"side":"top"})

ost_tankowanie = Text(fuel, height = 1, width = 42)
ost_tankowanie.insert(INSERT, najdrozsze[0])
ost_tankowanie.pack({"side":"top"})

var = StringVar()
label = Label( fuel, textvariable=var)
var.set("Najwieksza ilosc zatankowanego paliwa.")
label.pack({"side":"top"})

ost_tankowanie = Text(fuel, height = 1, width = 42)
ost_tankowanie.insert(INSERT, naj_paliwa[0])
ost_tankowanie.pack({"side":"top"})

fuel = Application(master=fuel)
fuel.mainloop()
