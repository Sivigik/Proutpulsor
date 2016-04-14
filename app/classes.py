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
        self.image_astronautext_flip = ASTRONAUTEXT_FLIP

        self.image = self.image_astronaut
        self.rect = self.image.get_rect()
        self.rect.center = screencenter
        self.astroposition_x = 0
        self.astroposition_y = 0
        self.extinguisher_right = False
        self.extinguisher_left = False
        self.fart = False
        self.angle = 270

        self.horizontal_speed = 0
        self.vertical_speed = 0
        self.rotation_speed = 0

        self.takeextinguisher = True

        self.fartx, self.farty = screencenter


    def display(self, screen):
        self.rotation()
        radiangle = (self.angle*pi)/180 # fart shower

        #pygame.draw.line(screen, (150, 65, 12), (self.fartx, self.farty),
        #(self.fartx-50*(cos(radiangle)),self.farty-50*(sin(radiangle))), 10)  #affiche l'angle de rotation

        screen.blit(self.image, self.rect)

    def mouvement(self):
        if self.takeextinguisher:
            if self.extinguisher_right:
                self.rotation_speed = -1
            elif self.extinguisher_left:
                self.rotation_speed = 1

        if self.fart:
            radiangle = (self.angle*pi)/180
            self.horizontal_speed = 1*(cos(radiangle))
            self.vertical_speed = 1*(sin(radiangle))

        #inertie:
        self.angle += self.rotation_speed
        if self.angle > 360: #pour eviter des angles trop grands
            self.angle = 0
        if self.angle < 0:
            self.angle = 360
        self.astroposition_x += self.horizontal_speed
        self.astroposition_y += self.vertical_speed

    def collision(self, rectangle):
        pass

    def rotation(self):  # retourne l'image par son milieu
        if self.takeextinguisher:
            if self.rotation_speed <= 0:
                self.image = self.image_astronautext
            else:
                self.image = self.image_astronautext_flip
        else:
            self.image = self.image_astronaut
        self.image = pygame.transform.rotate(self.image, 270-self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)



#class Steam(Astronaut): # Heritage
#    def __init__(self):




class Item(pygame.sprite.Sprite):
    def __init__(self, screencenter, IMAGE):
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

    def display(self, screen, astroposition_x, astroposition_y):
        self.rotation()

        self.x = self.posx - astroposition_x
        self.y = self.posy - astroposition_y
        self.rect.center = (self.x, self.y)

        screen.blit(self.image, self.rect)

        #radiangle = (self.angle*pi)/180
        #pygame.draw.line(screen, (0,255,0), (150,150),
        #(150+50*(cos(radiangle)),150+50*(sin(radiangle))), 5) #affiche vecteur direction

    def rotation(self):
        self.angle -= self.anglederotation * pi / 180
        self.image = self.imageorigin
        self.image = pygame.transform.rotate(self.image, 270-self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)