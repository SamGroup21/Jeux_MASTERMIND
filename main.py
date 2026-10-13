import pygame as pg
import random
import mm           
 
NB_PIONS = 5         
NB_ESSAIS_MAX = 2
 
 

def genererSecret() -> list:# # main()

    secret = []                                  #on cree une liste secrete            
    for i in range(0,NB_PIONS):                    #on parcours du premier couleur au 4 eme
        couleur = random.choice(mm.TabCouleur)    #on choisit une couleur par hasard
        secret.append(couleur)                   # et a chaque fois on ajoute en secret une couleur
    return secret
 
 

def nbBienPlaces(secret: list, prop: list) -> int:
    nb = 0
    for i in range(0,NB_PIONS):       # on compte(ou parcours les nombre de pion a partir du promier
        if secret[i] == prop[i]:     # même couleur à la même position
            nb = nb + 1
    return nb
 
 

def nbMalPlaces(secret: list, prop: list) -> int:
    communs = 0
    for couleur in mm.TabCouleur:              # parcourir la liste des couleur de la biblioteche mm
        communs = communs + min(secret.count(couleur), prop.count(couleur))
    # parmi les pions communs, ceux déjà bien placés ne sont pas "mal placés"
    return communs - nbBienPlaces(secret, prop)
 
 

def calculerResultat(secret: list, prop: list) -> tuple:
    return (nbBienPlaces(secret, prop), nbMalPlaces(secret, prop))
 
 

# afficher le message en bas : 

def afficherMessage(fenetre: pg.Surface, texte: str) -> None:
    pg.font.init                       #initialise le module de la police
    police = pg.font.SysFont("Arial", 20)                          # monospace
    etiquette = police.render(texte, True, mm.Bleu)
    fenetre.blit(etiquette, (300, 680))
    pg.display.update()
 
def main() -> None:
    # a) Affichage de l'IHM(ineterface homme machine)
    pg.display.set_caption("Bienvenu sur notre page de Jeux")
    fenetre = pg.display.set_mode((800, 720))
    fenetre.fill(mm.Blanc)               
    mm.afficherPlateau(fenetre)          
    mm.afficherChoixCouleur(fenetre)    
 
    secret = genererSecret()
 
    # c) Boucle de jeu
    essai = 0
    gagne = False
    while essai < NB_ESSAIS_MAX and not gagne:
        essai = essai + 1
        ligne = essai + 1                # la 1re ligne du plateau est la ligne 2 pour mm.py
 
        prop = mm.construireProposition(fenetre, ligne)   #
        res = calculerResultat(secret, prop)           
        mm.afficherResultat(fenetre, res, ligne)          # iii. affichage du résultat
 
        if res[0] == NB_PIONS:           
            gagne = True
 
    mm.afficherSecret(fenetre, secret)
    if gagne:
        afficherMessage(fenetre, "Bravo, gagne en " + str(essai) + " coup(s) !")
    else:
        afficherMessage(fenetre, "Vous avez perdu !")
    
  
    fini = False
    while not fini:
        for event in pg.event.get():# # main()

            if event.type == pg.QUIT:
                fini = True
    pg.quit()
main()
 
 