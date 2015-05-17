from Tkinter import *
import Tkinter
import Tkinter as tk
import tkMessageBox
import sqlite3 as lite
import sys

con = lite.connect('paliwko.db')
cur = con.cursor()

paliwo = []
ost = []
ilosc = []

fuel = Tk()

fuel.title("Dziennik tankowan")

with con: 
	cur = con.cursor()    
	cur.execute("SELECT * FROM tankowanie")
	rows = cur.fetchall()
	for row in rows:
		paliwo.append(row)
		
with con: 
	cur = con.cursor()    
	cur.execute("SELECT * FROM tankowanie")
	rows = cur.fetchall()
	ost.append(row)
	
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

fuel = Application(master=fuel)
fuel.mainloop()
