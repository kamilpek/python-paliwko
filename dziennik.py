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

class Application(Frame):
        
    def wyswietlanie(self):
		with con: 
			cur = con.cursor()    
			cur.execute("SELECT * FROM tankowanie")
			rows = cur.fetchall()
			for row in rows:
				paliwo.append(row)
				paliwo.append("\n")
		wszystkie = Text(fuel)
		wszystkie.insert(INSERT, paliwo)
       
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Wstecz"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "bottom"})
             
        self.dziennik = Button(self)
        self.dziennik["text"] = "Wyswietl_wszystkie_tankowania",
        self.dziennik["command"] = self.wyswietlanie
        self.dziennik.pack({"side":"top"})
        
        self.w_tankowania = Text(self, height = 10, width = 80)
        self.w_tankowania.insert(INSERT, paliwo)
        self.w_tankowania.pack({"side":"top"})
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

fuel = Application(master=fuel)
fuel.mainloop()
