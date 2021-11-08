# Dépendances
from tkinter import *


# Fonctions
def dessineGrille(canvas, listeGrille, longueurGrille, gridSize):
    """
    Cette fonction a pour but de dessiner la grille de couleurs.
    Arguments:
        canvas = La variable contenant le canvas.
        listeGrille = La grille de couleurs.
        longueurGrille = La longueur de la grille en pixels.
        gridSize = Le nombre de cubes qui seront dans la grille (15x15 ou 5x5).
    Retourne la longueur d'un cube afin de pouvoir la récuperer lors d'un clique
    """
    cubeLongueur = longueurGrille // gridSize + 1 # Taille des cubes qui vont constituer la grille
    
    for ligne in range(len(listeGrille)):
        for colonne in range(len(listeGrille[ligne])):

            couleurCase = listeGrille[ligne][colonne]
            
            # Coordonnées des rectangles
            x1, y1 = cubeLongueur * ligne, cubeLongueur * colonne
            x2, y2 = x1 + cubeLongueur, y1 + cubeLongueur
            
            # Dessine le rectangle sur la grille
            canvas.create_rectangle(x1, y1, x2, y2, fill = couleurCase, outline = "black", width = 1)
    
    return cubeLongueur


def dessineElementsJeu(win, nombre_coups):
    """
    Cette fonction a pour but d'afficher les éléments du jeu.
    Arguments:
        win = La fenêtre tkinter.
        nombre_coups = La variable contenant le nombre de coups à afficher dans le label.
    """
    labelCoups = Label(win, text = "Nombre de coups: " + str(nombre_coups), bg = "white") # Le label qui contiendra le nombre de coups restants
    labelCoups.grid(row = 1, column = 0, columnspan = 2, pady = 10)

    canvas = Canvas(win, width = 700, height = 700, bg = "white", bd = -2) # Canvas qui contiendra la grille de couleur
    canvas.grid(row = 0, column = 0, columnspan = 2)

    return (labelCoups, canvas)