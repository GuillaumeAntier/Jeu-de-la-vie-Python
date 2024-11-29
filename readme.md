# Jeu de la Vie en Python

Ce projet implémente le célèbre "Jeu de la Vie" de John Conway en Python. Le jeu est une simulation de cellules vivantes et mortes sur une grille, où chaque cellule évolue à chaque tour selon des règles simples.

## Structure du projet

Le projet est organisé en plusieurs fichiers pour une meilleure modularité :

- `grid.py` : Contient les fonctions liées à la création et à la mise à jour de la grille.
- `io.py` : Contient les fonctions liées à l'entrée/sortie, comme l'impression et la sauvegarde de la grille.
- `game_manager.py` : Contient la fonction `game_manager` qui gère la logique principale du jeu.
- `main.py` : Contient le point d'entrée principal du programme.

## Fonctionnalités

- Crée une grille de cellules vivantes et mortes de taille spécifiée par l'utilisateur.
- Met à jour la grille à chaque tour selon les règles du jeu de la vie.
- Sauvegarde l'état actuel de la grille et le numéro du tour dans un fichier `last_save.txt`.
- Charge la dernière grille sauvegardée pour reprendre la simulation.
- Détecte les motifs récurrents dans la grille.

## Installation

1. Clonez le dépôt :
    git clone https://github.com/GuillaumeAntier/Jeu-de-la-vie-Python.git
    cd jeu-de-la-vie-python

2. Assurez-vous d'avoir Python installé sur votre machine.

## Utilisation

1. Exécutez le script principal :
    python main.py

2. Suivez les instructions à l'écran :
    - Entrez `n` pour commencer une nouvelle partie.
    - Entrez `l` pour charger la dernière partie sauvegardée.

3. Entrez la longueur de la grille (entre 1 et 50).

4. À chaque tour, appuyez sur `Enter` pour mettre à jour la grille ou `q` pour quitter et sauvegarder l'état actuel.

## Règles du Jeu de la Vie

1. Une cellule vivante avec moins de deux voisins vivants meurt (sous-population).
2. Une cellule vivante avec deux ou trois voisins vivants survit.
3. Une cellule vivante avec plus de trois voisins vivants meurt (surpopulation).
4. Une cellule morte avec exactement trois voisins vivants devient vivante (reproduction).

## Exemple de sortie

⬛ ⬛ ⬛ ⬜ ⬜ ⬛ ⬛ ⬜ ⬛
⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬜ ⬜ ⬜
⬛ ⬜ ⬜ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛
⬛ ⬜ ⬛ ⬜ ⬛ ⬛ ⬛ ⬜ ⬛
⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬜ ⬜ ⬛
⬛ ⬜ ⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬜
⬛ ⬜ ⬛ ⬜ ⬛ ⬛ ⬛ ⬜ ⬜
⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬜ ⬜ ⬛
⬜ ⬛ ⬛ ⬛ ⬛ ⬜ ⬛ ⬜ ⬛