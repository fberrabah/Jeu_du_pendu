"""import functions random"""
from random import * 
from nom_fichier import *

"""this function allows you to add the letter if it matches your search"""
def lettre_dans_mot(lettre, mot_a_trouver):
    positions = []
    position_actuelle = 0
    for lettre_mot in mot_a_trouver:
        if lettre_mot == lettre :
            positions.append(position_actuelle)
        position_actuelle += 1

    return positions

"""this function allows you to replace the letter if it matches your search"""
def affiche_lettres_trouvees(positions, mot_a_trouver):
    mot_a_aficher = ""
    position_actuelle = 0
    for lettre_mot in mot_a_trouver:
        if position_actuelle in positions :
            mot_a_aficher += lettre_mot
        else:
            mot_a_aficher += "#"
        position_actuelle += 1

    return mot_a_aficher
"""this function allows you to choose the word to be found randomly in the list"""
def choisir_mot():
    
    return choice(mots)
