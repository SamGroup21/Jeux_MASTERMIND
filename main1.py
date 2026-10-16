import pygame as pg
import random
import mm

NB_PIONS = 5
NB_ESSAIS_MAX  = 15

def genererSecret()->  list :
    secret = []
    for i in range(0,NB_PIONS) :
        couleur = random.choice(mm.TabCouleur)
        secret.append(couleur)
    return secret

def nbBienPlaces(secret:list,prop : list) -> int :
    nb = 0
    for i in range(0,NB_PIONS) :
        if secret[i] == prop[i] :
            nb = nb+1
            
    return nb

#  mm.afficherSecret(fenetre, CombSecret)    vaincre le jeu

# 
# def nbMalPlaces(secret: list, prop: list) -> int:
#     communs = 0
#     for couleur in mm.TabCouleur:              # parcourir la liste des couleur de la biblioteche mm
#         communs = communs + min(secret.count(couleur), prop.count(couleur))
#     # parmi les pions communs, ceux déjà bien placés ne sont pas "mal placés"
#     return communs - nbBienPlaces(secret, prop)



