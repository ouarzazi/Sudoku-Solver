def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(map(str, ligne)))

def est_valide(grille, ligne, colonne, nombre):
    if nombre in grille[ligne] or nombre in [grille[i][colonne] for i in range(9)]:
        return False
    

    carre_ligne, carre_colonne = 3 * (ligne // 3), 3 * (colonne // 3)
    for i in range(carre_ligne, carre_ligne + 3):
        for j in range(carre_colonne, carre_colonne + 3):
            if grille[i][j] == nombre:
                return False
    
    return True

def trouver_case_vide(grille):
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0:
                return i, j
    return None, None  

def resoudre_sudoku(grille):
    ligne, colonne = trouver_case_vide(grille)

    if ligne is None and colonne is None:
        return True  

    for nombre in range(1, 10):
        if est_valide(grille, ligne, colonne, nombre):
            grille[ligne][colonne] = nombre

            if resoudre_sudoku(grille):
                return True  

            grille[ligne][colonne] = 0  

    return False


grille_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Starting grid:")
afficher_grille(grille_sudoku)

if resoudre_sudoku(grille_sudoku):
    print("\nSolved grid:")
    afficher_grille(grille_sudoku)
else:
    print("\nNo solution found.")
