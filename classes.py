#-------------------------------------------------------------------------------
# Name:        class - Proutpulsor
#
# Author:      Sivigik
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *

from random import randint

class Astronaut(pygame.sprite.Sprite):

    def __init__(self, fichier, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.fichier = fichier
        self.image = pygame.image.load(self.fichier).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


    def affiche(self, fenetre):
        fenetre.blit(self.image, self.rect)

    def mouvement(self, haut, bas, gauche, droite):
        if haut == True:
            self.rotation()
    def collision(self, rectangle):
        pass

    def rotation(self): #rotation arme, par le milieu de l'image
        origine_rectangle = self.image.get_rect()
        rotation_image = pygame.transform.rotate(self.image, 10)
        rotation_rectangle = origine_rectangle.copy()
        rotation_rectangle.center = rotation_image.get_rect().center
        rotation_image = rotation_image.subsurface(rotation_rectangle).copy()
        self.image = rotation_image
