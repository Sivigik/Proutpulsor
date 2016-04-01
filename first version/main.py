#-------------------------------------------------------------------------------
# Name:        Proutpulsor
#
# Author:      Sivigik
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
pygame.init()

import classes
fenetre = pygame.display.set_mode((800,480))#,FULLSCREEN)

pygame.display.set_caption("Proutpulsor")

fond = pygame.image.load("images/background.png")

astronaut = classes.Astronaut("images/astronaut.png", 400, 240)

jeu = True
while jeu:
    for event in pygame.event.get():
        if event.type == QUIT:
            jeu = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                astronaut.mouvement(True,False,False,False)
    fenetre.blit(fond, (0,0))
    astronaut.affiche(fenetre)
    pygame.display.flip()
pygame.quit()