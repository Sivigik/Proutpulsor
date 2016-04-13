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

        #pygame.draw.line(screen, (150, 65, 12), (self.fartx, self.farty),  (self.fartx-50*(cos(radiangle)),self.farty-50*(sin(radiangle))), 10)  #affiche l'angle de rotation

        screen.blit(self.image, self.rect)

    def mouvement(self):
        if self.extinguisher and self.takeextinguisher:
            self.angle -= 1
            if self.angle > 360:
                self.angle = 0

        elif self.fart:
            radiangle = (self.angle*pi)/180
            self.astroposition_x += 1*(cos(radiangle))
            self.astroposition_y += 1*(sin(radiangle))

        else:
            self.angle -= (0.25 * pi / 180)  # pour faire bouger l'astronaute en continu

    def collision(self, rectangle):
        pass

    def rotation(self):  # retourne l'image par son milieu
        if self.takeextinguisher:
            self.image = self.image_astronautext
        else:
            self.image = self.image_astronaut
        self.image = pygame.transform.rotate(self.image, 270-self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)



#class Steam(Astronaut): # Heritage
#    def __init__(self):




class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, screencenter, IMAGE):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = screencenter
        self.imageorigin = IMAGE
        self.image = self.imageorigin
        self.rect = self.image.get_rect()
        self.posx = self.x + (random.randint(-5*self.x,self.x*5))
        self.posy = self.y + (random.randint(-5*self.y,self.y*5))
        self.rect.topleft = (self.x, self.y)
        self.anglederotation = random.randint(-20,20)
        self.angle = 0

    def affiche(self, screen, astroposition_x, astroposition_y):
        self.rotation()

        self.x = self.posx - astroposition_x
        self.y = self.posy - astroposition_y
        self.rect.center = (self.x, self.y)

        screen.blit(self.image, self.rect)
        #radiangle = (self.angle*pi)/180
        #pygame.draw.line(screen, (0,255,0), (150,150),  (150+50*(cos(radiangle)),150+50*(sin(radiangle))), 5) #affiche vecteur direction

    def rotation(self):
        self.angle -= self.anglederotation * pi / 180
        self.image = self.imageorigin
        self.image = pygame.transform.rotate(self.image, 270-self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)