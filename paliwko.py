from Tkinter import *
import Tkinter
import Tkinter as tk
import tkMessageBox
import sqlite3 as lite
import sys
from os import popen

fuel = Tk()
fuel.title("Paliwko ver. 2.5")

frame = Frame(fuel, height = 10, width = 200)
frame.pack()

class Application(Frame):
        
    def dodawanie(self):
        popen('python dodawanie.py')
        
    def tankowania(self):
		popen('python dziennik.py')

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Koniec programu"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "bottom"})
       
        self.dodaj = Button(self)
        self.dodaj["text"] = "Dodaj_Tankowanie",
        self.dodaj["command"] = self.dodawanie 
        self.dodaj.pack({"side": "top"})
        
        self.dziennik = Button(self)
        self.dziennik["text"] = "Dziennik_Tankowan",
        self.dziennik["command"] = self.tankowania
        self.dziennik.pack({"side":"top"})
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

fuel = Application(master=fuel)
fuel.mainloop()