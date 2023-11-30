# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:35:48 2023

@author: anyta
"""

from tkinter import *
import random

root = Tk()
root.title("Adivina el personaje >:D")
root.geometry("900x500")

personaje = Label(root)

personajes = ["Spierman", "Venom", "Spider-kid", "Duende verde", "Iron-spider", "Dock ock", "Anti-spiderman", "Black cat", "Electro"]

def aleatorio():
    Personaje_aleatorio = random.randint(0,8)
    Personaje_aleatorio2 = random.randint(0,8)
    Personaje_aleatorio3 = random.randint(0,8)
    Personaje_aleatorio4 = random.randint(0,8)
    Personaje = personajes[Personaje_aleatorio]
    Personaje2 = personajes[Personaje_aleatorio2]
    Personaje3 = personajes[Personaje_aleatorio3]
    Personaje4 = personajes[Personaje_aleatorio4]
    
    personaje["text"] = " Este te ataca " + Personaje + " Este te defiende " + Personaje2 + " Este intenta m4t4rt3 " + Personaje3 + " Este te salva " + Personaje4
    
btn = Button(root, text = "Tu historia", command = aleatorio)

btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
personaje.place(relx = 0.5, rely = 0.3, anchor = CENTER)

root.mainloop()