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
    police = pg.font.SysFont("Arial", 20)                          # la police de la message (Arial) à 20 pixel
    etiquette = police.render(texte, True, mm.Bleu)      #pour afficher le texte en bleu et trasnformer le texte en image
    fenetre.blit(etiquette, (300, 680))                  #coller l'image sur les cordonne 300 et 680
    pg.display.update()                                 # reflachir la page pour que le nouvelle modification apparaissent
 
def main() -> None: #fonction principal
    # a) Affichage de l'IHM(ineterface homme machine)
    pg.display.set_caption("Bienvenu sur notre page de Jeux") #fonctionnalité de pygame qui est de Récupérer le titre de la fenêtre actuelle
    fenetre = pg.display.set_mode((800, 720))           # fenetre de 800 pixels de hauteur et 720 pixels de largeur
    fenetre.fill(mm.Blanc)               #couleur blanche comme couleur principal dans la fenetre
    mm.afficherPlateau(fenetre)              # dessine le plateau : rectangle marron, cases quadrillées et textes d'aide  
    mm.afficherChoixCouleur(fenetre)     #dessine la palette : les 8 pastilles de couleur et la pastille marron "retirer dernier pion"
    CombSecret = genererCombSecret()   # crée la combinaison secrète : liste de 5 couleurs tirées au hasard (cachée au joueur)
   
    # c) Boucle de jeu
    essai = 0
    gagne = False
    while essai < NB_ESSAIS_MAX and not gagne:  # tant qu'il reste des essais ET que le joueur n'a pas gagné on continu

        essai = essai + 1       # on passe à l'essai suivant (1, 2, 3...)
        ligne = essai + 1          #a chaque essaie on change de ligne      
 
        prop = mm.construireProposition(fenetre, ligne)   # attend 5 clics du joueur dans un tel pion, dessine les dans  la ligne
                                                            # et retourne la proposition : une liste de 5 couleurs
        res = calculerResultat(CombSecret, prop)           # compare la proposition
        mm.afficherResultat(fenetre, res, ligne)          # affichage du résultat dans la fenetre selon les mal place(rond noir) et les bien placé(rond blanche)
 
        if res[0] == NB_PIONS:       # le nombre de pions bien placés ; s'il vaut 5,
            gagne = True          # tous les pions sont corrects : le joueur a trouve le secret
 
    mm.afficherSecret(fenetre, CombSecret)  # à la fin, on montre le secret dans la ligne du haut
    
    if gagne:
        afficherMessage(fenetre, "Felicitation vous avez, gagnez en " + str(essai) + " coup(s) !")
    else:
        afficherMessage(fenetre, "Oups Vous avez perdu !")
    
  
    fini = False
    while not fini:                  # quand l programme n'est pas encore fini         
        for event in pg.event.get():# # main()

            if event.type == pg.QUIT: # l'utilisateur clique sur quitter
                fini = True
    pg.quit()                           #sors dans le programme
try:              # on essaie de lancer le jeu
    main() 
    
except pg.error:            # si pygame signale une erreur 
    print("Fenêtre fermée, fin du programme.")   #  au lieu d'afficher les erreur ,afficher ce message
    
    

 
 