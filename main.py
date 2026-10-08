import pygame as pg
import random
import mm           
 
NB_PIONS = 5         
NB_ESSAIS_MAX = 15 
 
 
# ------------------------------------------------------------
# 1) Générer la combinaison secrète (liste de 5 couleurs)
# ------------------------------------------------------------
def genererSecret() -> list:
    secret = []                                  # liste vide au départ
    for i in range(NB_PIONS):                    # on répète 5 fois
        couleur = random.choice(mm.TabCouleur)   # une couleur au hasard
        secret.append(couleur)                   # on l'ajoute au secret
    return secret
 
 
# ------------------------------------------------------------
# 2) Compter les pions bien placés (bonne couleur, bonne place)
# ------------------------------------------------------------
def nbBienPlaces(secret: list, prop: list) -> int:
    nb = 0
    for i in range(NB_PIONS):
        if secret[i] == prop[i]:     # même couleur à la même position
            nb = nb + 1
    return nb
 
 
# ------------------------------------------------------------
# 3) Compter les pions mal placés (bonne couleur, mauvaise place)
# ------------------------------------------------------------
def nbMalPlaces(secret: list, prop: list) -> int:
    communs = 0
    for couleur in mm.TabCouleur:
        # pour chaque couleur, on garde le plus petit nombre d'apparitions
        # (on ne peut pas compter plus de pions que l'un des deux n'en a)
        communs = communs + min(secret.count(couleur), prop.count(couleur))
    # parmi les pions communs, ceux déjà bien placés ne sont pas "mal placés"
    return communs - nbBienPlaces(secret, prop)
 
 
# ------------------------------------------------------------
# 4) Résultat sous forme de tuple (bien placés, mal placés)
# ------------------------------------------------------------
def calculerResultat(secret: list, prop: list) -> tuple:
    return (nbBienPlaces(secret, prop), nbMalPlaces(secret, prop))
 
 
# ------------------------------------------------------------
# 5) Afficher un texte en bas de la fenêtre
# ------------------------------------------------------------
def afficherMessage(fenetre: pg.Surface, texte: str) -> None:
    police = pg.font.SysFont("monospace", 20)
    etiquette = police.render(texte, 1, mm.Noir)
    fenetre.blit(etiquette, (300, 680))
    pg.display.update()
 
 
# ------------------------------------------------------------
# 6) Programme principal
# ------------------------------------------------------------
def main() -> None:
    # a) Affichage de l'IHM
    fenetre = pg.display.set_mode((800, 720))
    fenetre.fill(mm.Blanc)               # fond blanc
    mm.afficherPlateau(fenetre)          # plateau marron
    mm.afficherChoixCouleur(fenetre)     # palette de couleurs à gauche
 
    # b) Combinaison secrète (cachée pendant la partie)
    secret = genererSecret()
 
    # c) Boucle de jeu
    essai = 0
    gagne = False
    while essai < NB_ESSAIS_MAX and not gagne:
        essai = essai + 1
        ligne = essai + 1                # la 1re ligne du plateau est la ligne 2 pour mm.py
 
        prop = mm.construireProposition(fenetre, ligne)   # i.   proposition du joueur
        res = calculerResultat(secret, prop)              # ii.  (bien placés, mal placés)
        mm.afficherResultat(fenetre, res, ligne)          # iii. affichage du résultat
 
        if res[0] == NB_PIONS:           # 5 bien placés = gagné
            gagne = True
 
    # d) Message de fin + on révèle le secret
    mm.afficherSecret(fenetre, secret)
    if gagne:
        afficherMessage(fenetre, "Bravo, gagne en " + str(essai) + " coup(s) !")
    else:
        afficherMessage(fenetre, "Vous avez perdu !")
 
    # e) On attend que l'utilisateur ferme la fenêtre
    fini = False
    while not fini:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fini = True
    pg.quit()
 
 
main()