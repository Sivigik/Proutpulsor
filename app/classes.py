#-------------------------------------------------------------------------------
# Name:        class - Proutpulsor
#
# Author:      Sivigik
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from constantes import *

from math import sin, cos, pi

class Astronaut(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = ASTRONAUT
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.extinguisher = False
        self.fart = False
        self.angle = 0


    def affiche(self, screen):
        self.rotation()
        screen.blit(self.image, self.rect)
        radiangle = (self.angle*pi)/180
        pygame.draw.line(screen, (255,0,0), (50,50),  (50+50*(cos(radiangle)),50+50*(sin(radiangle))), 5)

    def mouvement(self):
        if self.extinguisher:
            self.angle += 5
            if self.angle > 360:
                self.angle = 0
        elif self.fart:
            radiangle = (self.angle*pi)/180
            self.rect.x = self.rect.x + 10*(cos(radiangle))
            self.rect.y = self.rect.y + 10*(sin(radiangle))
    def collision(self, rectangle):
        pass

    def rotation(self):
        self.image = ASTRONAUT
        origine_rectangle = self.image.get_rect()
        rotation_image = pygame.transform.rotate(self.image, self.angle)
        rotation_rectangle = origine_rectangle.copy()
        rotation_rectangle.center = rotation_image.get_rect().center
        #self.image = rotation_image.subsurface(rotation_rectangle).copy()

        loc = rotation_image.get_rect().center
        rot_sprite = pygame.transform.rotate(self.image, self.angle)
        rot_sprite.get_rect().center = loc

        #self.rect = rot_sprite.get_rect()
        #elf.rect.topleft = (self.x, self.y)

        self.image=rot_sprite



class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit, message
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)