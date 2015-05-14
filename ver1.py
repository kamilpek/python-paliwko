from Tkinter import *
import Tkinter
import Tkinter as tk
import tkMessageBox
import sqlite3 as lite
import sys

con = lite.connect('paliwko.db')

fuel = Tk()
fuel.title("Paliwko ver. 1.3")

class Application(Frame):
    def say_hi(self):
        print "hi there!"
        
    def dodaj(self):
        print "dodaj!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Wyjscie"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
        
        self.dodaj_tankowanie = Button(self)
        self.dodaj_tankowanie["text"] = "dodaj",
        self.dodaj_tankowanie["command"] = self.dodaj 

        self.dodaj_tankowanie.pack({"side": "left"})
       

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

var = StringVar()
label = Label( fuel, textvariable=var, relief=RAISED )
var.set("Podaj stan licznika.")
label.pack()
licznik = tk.Entry(fuel, width = 30, bg = "white", font = "Helvetica 14")  
licznik.pack()
licznik.focus()
a=licznik.get()

var = StringVar()
label = Label( fuel, textvariable=var, relief=RAISED )
var.set("Podaj ilosc zatankowanego paliwa.")
label.pack()
ilosc = tk.Entry(fuel, width = 30, bg = "white", font = "Helvetica 14")
ilosc.pack()
b=ilosc.get()

var = StringVar()
label = Label( fuel, textvariable=var, relief=RAISED )
var.set("Podaj koszt paliwa.")
label.pack() 
cena = tk.Entry(fuel, width = 30, bg = "white", font = "Helvetica 14")
cena.pack()
c=cena.get()

fuel = Application(master=fuel)
fuel.mainloop()
fuel.destroy()
