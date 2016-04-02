# -------------------------------------------------------------------------------
# Name:        class - Proutpulsor
#
# Author:      S.L-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
# -------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from constantes import *

import random

from math import sin, cos, pi

class Astronaut(pygame.sprite.Sprite):

    def __init__(self, screencenter):
        pygame.sprite.Sprite.__init__(self)

        self.image_astronaut = ASTRONAUT
        self.image_astronautext = ASTRONAUTEXT
        self.image = self.image_astronaut
        self.rect = self.image.get_rect()
        self.rect.center = screencenter
        self.astroposition_x = 0
        self.astroposition_y = 0
        self.extinguisher = False
        self.fart = False
        self.angle = -89

        self.takeextinguisher = True

        self.fartx, self.farty = screencenter


    def affiche(self, screen):
        self.rotation()
        radiangle = (self.angle*pi)/180 # fart shower
        pygame.draw.line(screen, (150, 65, 12), (self.fartx, self.farty),  (self.fartx-50*(cos(radiangle)),self.farty-50*(sin(radiangle))), 10)  #affiche l'angle de rotation

        screen.blit(self.image, self.rect)

    def mouvement(self):
        if self.extinguisher and self.takeextinguisher:
            self.angle -= 5
            if self.angle > 360:
                self.angle = 0

        elif self.fart:
            radiangle = (self.angle*pi)/180
            self.astroposition_x += 1*(cos(radiangle))
            self.astroposition_y += 1*(sin(radiangle))

        else:
            self.angle -= (10 * pi / 180)  # pour faire bouger l'astronaute en continu

    def collision(self, rectangle):
        pass

    def rotation(self):  # retourne l'image par son milieu
        if self.takeextinguisher:
            self.image = self.image_astronautext
        else:
            self.image = self.image_astronaut
        self.image= pygame.transform.rotate(self.image, 270-self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)



#class Steam(Astronaut): # Heritage
#    def __init__(self):




class Extinguisher(pygame.sprite.Sprite):
    def __init__(self, x, y, screencenter):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = screencenter
        self.image = EXTINGUISHER
        self.rect = self.image.get_rect()
        self.x = self.x + (random.randint(-200,200))
        self.y = self.y + (random.randint(-200,200))
        self.rect.topleft = (self.x, self.y)
        self.anglederotation = random.randint(10,50)
        self.angle = 0

    def affiche(self, screen, astroposition_x, astroposition_y, fart):
        self.rotation()
        if fart:
            self.rect.x = self.rect.x - astroposition_x
            self.rect.y = self.rect.y - astroposition_y
        screen.blit(self.image, self.rect)
        radiangle = (self.angle*pi)/180
        pygame.draw.line(screen, (0,255,0), (150,150),  (150+50*(cos(radiangle)),150+50*(sin(radiangle))), 5)

    def rotation(self):
        self.angle = self.angle - self.anglederotation*pi/180
        self.image = EXTINGUISHER
        self.image= pygame.transform.rotate(self.image, 270-self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)