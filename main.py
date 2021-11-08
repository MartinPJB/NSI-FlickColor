# Dépendances
from tkinter import *
from modules.jeu import *


# Variables globales
win = Tk() # Fenêtre Tkinter


# Configuration de la fenêtre Tkinter
win.title("FlickColor")
win.resizable(False, False)
win.configure(background = "white")
win.iconphoto(False, Pil_imageTk.PhotoImage(file = "./img/icon.png"))


# Appel du menu
menu(win)
win.mainloop()