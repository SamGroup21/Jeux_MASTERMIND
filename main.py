import pygame as pg
import random
import mm           
 
NB_PIONS = 5         
NB_ESSAIS_MAX = 15
 
 

def genererCombSecret() -> list:# # main()
    CombSecret = []                                  #on cree une liste secrete            
    for i in range(0,NB_PIONS):                    #on parcours du premier couleur au 4 eme
        couleur = random.choice(mm.TabCouleur)    #on choisit une couleur par hasard
        CombSecret.append(couleur)                   # et a chaque fois on ajoute en CombSecret une couleur
    return CombSecret
 
 

def nbBienPlaces(CombSecret: list, prop: list) -> int:
    nb = 0
    for i in range(0,NB_PIONS):       # on compte(ou parcours les nombre de pion a partir du promier
        if CombSecret[i] == prop[i]:     # même couleur à la même position
            nb = nb + 1
    return nb
 
 

 
def nbMalPlaces(prop: list, CombSecret: list) -> int:
    nb = 0
    liste = []                                  # couleurs du secret qui ne sont PAS bien placées
    for i in range(len(CombSecret)):
        if CombSecret[i] != prop[i]:            # pion du secret mal couvert par la proposition
            liste.append(CombSecret[i])         # on le garde en réserve
    for i in range(len(CombSecret)):
        if CombSecret[i] != prop[i]:            # pion de la proposition qui n'est pas bien placé
            if prop[i] in liste:                # sa couleur existe encore dans la réserve
                nb += 1                         # c'est un mal placé
                liste.remove(prop[i])           # on l'enlève pour ne pas le compter deux fois
    return nb

def calculerResultat(CombSecret: list, prop: list) -> tuple:
    return (nbBienPlaces(CombSecret, prop), nbMalPlaces(CombSecret, prop))
 
 

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
    CombSecret = genererCombSecret()
   
    # c) Boucle de jeu
    essai = 0
    gagne = False
    while essai < NB_ESSAIS_MAX and not gagne:
        essai = essai + 1
        ligne = essai + 1                # la 1re ligne du plateau est la ligne 2 pour mm.py
 
        prop = mm.construireProposition(fenetre, ligne)   #
        res = calculerResultat(CombSecret, prop)           
        mm.afficherResultat(fenetre, res, ligne)          # iii. affichage du résultat
 
        if res[0] == NB_PIONS:           
            gagne = True
 
    mm.afficherSecret(fenetre, CombSecret)
    
    if gagne:
        afficherMessage(fenetre, "Felicitation vous avez, gagnez en " + str(essai) + " coup(s) !")
    else:
        afficherMessage(fenetre, "Oups Vous avez perdu !")
    
  
    fini = False
    while not fini:
        for event in pg.event.get():# # main()

            if event.type == pg.QUIT:
                fini = True
    pg.quit()
try:              # on essaie de lancer le jeu
    main() 
    
except pg.error:            # si pygame signale une erreur 
    print("Fenêtre fermée, fin du programme.")   #  au lieu d'afficher les erreur ,afficher ce message
    
    

 
 