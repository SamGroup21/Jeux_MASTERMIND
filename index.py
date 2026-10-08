
# Bleu = (0,0,255)
# Orange = (225,127,0)
# Blanc = (255,255,255)

# height,weigth = 800,1000

# x ,y = 450,350
# taille = 50
# vitesse = 1
# fenetre = None


# horloge = pg.time.Clock


# def afficherIHM() :
#     global fenetre
    
#     fenetre= pg.display.set_mode((height,weigth))
#     pg.display.set_caption("Bienvenu sur notre page de Jeux")
    
# afficherIHM()
    
    

# def processus_en_cours() :
#  global x,y
#  en_cours = True 
#  while en_cours :
#             for event in pg.event.get() :
#             #    recuperer les evenement ed la file d'attente
#                 if event.type == pg.QUIT :
#                 #  si l'evenement cliquer esr quiter, quite la fonction

#                  en_cours = False
#         # gestion du touche sur le clavier
#             touche = pg.key.get_pressed()
#             if touche[pg.K_LEFT] :
#                 x -= vitesse
#             if touche[pg.K_RIGHT] :
#                 x += vitesse

#             if touche[pg.K_UP] :
#                 y -= vitesse

#             if touche [pg.K_DOWN] :
#                 y  += vitesse
#             # remplisser l'image par un couleur blanc : 
#             fenetre.fill(Blanc)
#             pg.draw.rect(fenetre, Bleu, (x, y, taille, taille))
#             pg.display.flip()


            
        

# processus_en_cours()


