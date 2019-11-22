"""call all the functions"""

from functions import *
from nom_fichier import *

"""these variables will start the program"""

mot_a_trouver = choisir_mot()
position_tout = []
essais = 0
lettres_trouvees = []

"""loop when the game does not exceed 6 tries"""

while essais < 6:

    lettre_joueur = ""
    lettre_joueur = input("Entrez une lettre: ").lower()

    """condition to check the entry of the user"""

    if len(lettre_joueur) > 1 or not lettre_joueur.isalpha():
        print("Entrez seulement une lettre et non pas des chiffres ou des caratéres !")

    """if the entry of the user is identical to the first one at the level of the letters chosen"""

    while lettre_joueur in lettres_trouvees : 
        lettre_joueur = input("Entrer a nouveau une lettre, vous avez déjà choisit cette lettre : ").lower()
        if len(lettre_joueur) > 1 or not lettre_joueur.isalpha():
            print("Entrez seulement une lettre et non pas des chiffres ou des caratéres !")

    lettres_trouvees.append(lettre_joueur)
    position_actuelle = lettre_dans_mot(lettre_joueur, mot_a_trouver)

    """indicates the number of remaining parties if user error"""

    if position_actuelle == []:
        essais += 1
    print("Attention ! vous avez utilisé {} essais sur 6 possibles.".format(essais))
    position_tout += position_actuelle
    mot_a_aficher = affiche_lettres_trouvees(position_tout, mot_a_trouver)
    print(mot_a_aficher)
    print(PENDAISON[essais])

    """if the number of errors is identical to the number of tests and tells him the right word"""

    if essais == 6 :
        print("Désoler :( vous avez perdu ! Le bon mot était {} ".format((mot_a_trouver).upper()))

    if mot_a_aficher == mot_a_trouver:
        print("Bravo! vous avez trouver le bon mot")
    
    """this loop allows the user to replay or quit the program"""

    while essais == 6 or mot_a_aficher == mot_a_trouver :
        restart = input("Voulez-vous rejouer ? oui/non ? ").lower()

        if restart == "oui":
            mot_a_trouver = choisir_mot()
            position_tout = []
            essais = 0
            lettres_trouvees = []

        elif restart == "non":
            print("À trés bientot :) !")
            exit()

        else:
            print("Choisissez entre oui et non")