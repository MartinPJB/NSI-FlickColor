# Dépencances
from random import *


# Fonctions
def genereGrille(gridSize):
    """
    Cette fonction a pour but de générer la grille de couleurs.
    Argument:
        gridSize = Le nombre de cubes qui seront dans la grille (15x15 ou 5x5).
    Retourne la grille de couleurs aléatoires.
    """
    # Définition des couleurs
    couleurs = ["#ff4545", "#ff9d3b", "#1cbd27", "#00b7ff", "#4340ff", "#ff8cf4"]
    
    return [[choice(couleurs) for x in range(gridSize)] for y in range(gridSize)] 


def colorier(grille, i, j, couleur_initiale, couleur_finale):
    """ 
    Cette fonction a pour but de propager la couleur, si la case i,j est de couleur initiale, 
    la couleur finale à la case i,j et à toutes les cases adjacentes de même couleur initiale.
    Deux cases adjacentes sont côte à côte soit horizontalement, soit verticalement.
    Arguments:
        grille = La grille de couleurs.
        i = Point d'ordonnée i.
        j = Point d'abscisse j.
        couleur_initiale = Couleur initiale de la case à modifier
        couleur_finale = La couleur dont on veut modifier la case_initiale
    """
    if not(0 <= i < len(grille) and 0 <= j < len(grille)) or (not grille[j][i] == couleur_initiale or grille[j][i] == couleur_finale):
        return

    grille[j][i] = couleur_finale

    colorier(grille, i + 1, j, couleur_initiale, couleur_finale)
    colorier(grille, i - 1, j, couleur_initiale, couleur_finale)
    colorier(grille, i, j + 1, couleur_initiale, couleur_finale)
    colorier(grille, i, j - 1, couleur_initiale, couleur_finale)