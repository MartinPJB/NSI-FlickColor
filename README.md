# NSI - Projet n°1 [Classe de terminale]
*Instructions du projet*

## Règles du FlickColor
Le but du FlickColor est de faire se propager les couleurs sur une grille jusqu'à ce qu'il n'en reste plus qu'une à la fin du jeu. Le joueur doit pouvoir remplir la grille d'une seule couleur en un minimum de coups.

![image](https://user-images.githubusercontent.com/29103374/140794057-0ea3d71e-1315-4642-9fbf-f370fe3c2f93.png)

## Projet
- Nous devons utiliser TKinter pour l'interface graphique.
- Notre programme devra comporter:
  - Un écran d'accueil pour démarrer le jeu
  - Un écran de jeu
  - Un écran de sortie à la fin du jeu
- Notre programme devra proposer deux niveaux de jeu:
  - Niveau 1 : Grille 5*5
  - Niveau 2 : Grille 10*10
- Nous considérerons qu'une grille de jeu est une liste de listes, et que chaque ligne de la grille de jeu est une liste de couleurs.
- Les cases de la grille de jeu peuvent prendre jusqu'à 6 couleurs différentes.
- Les grilles de jeu sont générées de manière aléatoire et sont différentes à chaque partie.
- L'écran de jeu doit posséder une zone d'affichage du nombre de coups joués. Cet affichage doit se mettre à jour chaque fois que le joueur choisit une nouvelle couleur.
- Nous devons utiliser une foncion récursive pour "propager la couleur" en suivant ce schéma:
```py
def colorier(grille,i,j,couleur_initiale,couleur_finale):
  """ Propage, si la case i,j est de couleur initiale,
  la couleur finale à la case i,j et à toutes les cases adjacentes
  de même couleur initiale.
  Deux cases adjacentes sont côte à côte soit horizontalement, soit verticalement.
  """
```
- Notre code doit être structuré avec des fonctions de taille raisonnable.
- Notre projet devra adopter une approche modulaire, et nous devons séparer la partie graphique de la partie fonctionnelle.

## Critères
- Résultat final
- Implication en classe durant les séances de projet
- Respect des consignes
- Organisation et propreté du code informatique
- Présence de commentaires dans le code (Avec #)
- Spécifications des fonctions ("""...""")
- Rapport clair avec un contenu significatif

## Remise du projet
Fichier zip contenant les programmes et le rapport **pour le 15/11/2021**.
