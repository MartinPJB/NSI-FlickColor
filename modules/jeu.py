# Dépendances
from tkinter import *
from tkinter import font
from PIL import Image as Pil_image, ImageTk as Pil_imageTk


# Modules
from modules.grilles import *
from modules.interface import *


# Fonctions
def clearWin(win):
    """
    Cette fonction a pour but de retirer tous les widgets créés sur la fenêtre tkinter, s'utilise lors d'un changement de menu ou autres.
    Argument:
        win = La variable contenant la fenêtre tkinter.
    """
    for widget in win.winfo_children(): # Parcours tous les widgets
        widget.destroy() # Et les supprimes


def fin(win, coups_restants):
    """
    Cette fonction a pour but d'afficher l'écran de fin
    Arguments:
        win = La variable contenant la fenêtre tkinter.
        coups_restants = Le nombre de coups restants.
    """
    win.geometry("500x600") # Change la taille de la fenêtre
    clearWin(win) # Supprime les éléments de la fenêtre pour que tout soit vierge

    # Charge le game over, et l'implémente avec "ImageTk"
    img = Pil_image.open("./img/game_over.png")
    width, height = img.size
    img = Pil_imageTk.PhotoImage(img)
    
    # L'affiche à l'écran
    gameover = Label(image = img, bg = "white")
    gameover.photo = img
    gameover.pack(pady = 20)

    # Création d'une police d'écriture
    police = font.Font(family = "Sans-Serif", size = 12)

    # Affiche le nombre de coups
    coups = Label(win, bg = "white", text = "Vous avez terminé le jeu en " + str(coups_restants) + " coup(s).", font = police)
    coups.pack(pady = 30)

    # Bouton retour au menu
    img_backmenu = Pil_imageTk.PhotoImage(Pil_image.open("./img/buttonmenu.png"))
    btn_menu = Button(text = "menu", borderwidth = 0, command = lambda : menu(win))
    btn_menu.config(image = img_backmenu)
    btn_menu.photo = img_backmenu
    btn_menu.pack()


def menu(win):
    """
    Cette fonction a pour but d'afficher le menu du color flicker lors de son appel.
    Argument:
        win = La variable contenant la fenêtre tkinter.
    """
    win.geometry("500x600") # Change la taille de la fenêtre
    clearWin(win) # Supprime les éléments de la fenêtre pour que tout soit vierge

    # Charge le logo, et l'implémente avec "ImageTk"
    img = Pil_image.open("./img/logo.png")
    width, height = img.size
    img = Pil_imageTk.PhotoImage(img)
    
    # L'affiche à l'écran
    logo = Label(image = img, bg = "white")
    logo.photo = img
    logo.pack(pady = 70)

    # Bouton 5 x 5 | Quand cliqué, appelle la fonction jeu qui va faire commencer celui-ci avec une grille de 5 sur 5
    img_5x5 = Pil_imageTk.PhotoImage(Pil_image.open("./img/button5x5.png"))
    btn_5x5 = Button(text = "5x5", borderwidth = 0, command = lambda : jeu(win, 5))
    btn_5x5.config(image = img_5x5)
    btn_5x5.photo = img_5x5
    btn_5x5.pack()

    # Bouton 15 x 15 | Quand cliqué, appelle la fonction jeu qui va faire commencer celui-ci avec une grille de 15 sur 15
    img_15x15 = Pil_imageTk.PhotoImage(Pil_image.open("./img/button10x10.png"))
    btn_15x15 = Button(text = "15x15", borderwidth = 0, command = lambda : jeu(win, 10))
    btn_15x15.config(image = img_15x15)
    btn_15x15.photo = img_15x15
    btn_15x15.pack()


def jeu(win, gridSize):
    """
    Cette fonction a pour but de commencer le jeu.
    Argument:
        win = La variable contenant la fenêtre tkinter.
        gridSize = La taille des grilles de couleur.
    """
    win.geometry("700x740") # Change la taille de la fenêtre sur 700x750
    clearWin(win) # Supprime les éléments de la fenêtre pour que tout soit vierge

    # Initialise la variable contenant le nombre de coups max
    global nombre_coups
    nombre_coups = 0

    (labelCoups, canvas) = dessineElementsJeu(win, nombre_coups)    
    grille = genereGrille(gridSize) # Génère la grille et enregistre la liste
    cubeLongueur = dessineGrille(canvas, grille, 700, gridSize) # Dessine la grille générée et nous renvoie la longueur d'un cube
    

    # Ajoute le clic sur le canvas et appelle la fonction "clicGrille" définie si dessous
    def clicGrille(event):
        """
        Cette fonction a pour but de détecter un clic sur le canvas afin de changer les couleurs ainsi que de redessiner les cases changées.
        Argument:
            event = L'event du clic sur le canvas
        """
        x, y = event.x, event.y

        ligne = x // cubeLongueur
        colonne = y // cubeLongueur
        nouvelle_couleur = grille[ligne][colonne]
        
        # Va propager la couleur dans la grille avec la fonction "colorier"
        colorier(grille, 0, 0, grille[0][0], nouvelle_couleur)
        dessineGrille(canvas, grille, 700, gridSize)

        global nombre_coups
        nombre_coups += 1
        labelCoups["text"] = "Nombre de coups: " + str(nombre_coups)

        # Regarde si le nombre de coups est à 0 ou si toute la grille est de la même couleur
        if all(grille[x][y] == grille[0][0] for x in range(len(grille)) for y in range(len(grille))):
            return fin(win, nombre_coups)
        

    canvas.bind("<Button-1>", clicGrille)