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

# def nbMalPlaces(prop:list,secret :list)  -> int :
#     nb = 0
#     for i in range(len(secret)) :
#         if secret[i] != prop[i] :
#             nb +=1
            
#     return nb 



