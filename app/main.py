# -------------------------------------------------------------------------------
# Name:        main - Proutpulsor
#
# Author:      S.L-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
# -------------------------------------------------------------------------------
import pygame
from pygame.locals import *
# Set the screen size.
screen = pygame.display.set_mode((0,0), FULLSCREEN) #(800, 480)) #
pygame.init()

import classes
from constantes import *

import random

scrrec = screen.get_rect()
BACKGROUND = pygame.transform.scale(BACKGROUND, (scrrec.right, scrrec.bottom))

# Import the android module. If we can't import it, set it to None - this
# lets us test it, and check to see if we want android-specific behavior.
try:
    import android
except ImportError:
    android = None

# Event constant.
TIMEREVENT = pygame.USEREVENT

# The FPS the game runs at.
FPS = 30


def universegenerator(number_ext, number_ast, number_hamb):
    extinguisher = [0]*number_ext
    for i in range(0,number_ext):
        extinguisher[i] = classes.Item(scrrec.center, EXTINGUISHER)

    asteroid = [0]*number_ast
    for i in range(0,number_ast):
        randomvar = random.randint(1,4)
        if randomvar == 1:
            asteroid[i] = classes.Item(scrrec.center, ASTEROID1)
        if randomvar == 2:
            asteroid[i] = classes.Item(scrrec.center, ASTEROID2)
        if randomvar == 3:
            asteroid[i] = classes.Item(scrrec.center, ASTEROID3)
        if randomvar == 4:
            asteroid[i] = classes.Item(scrrec.center, ASTEROID4)

    hamburger = [0]*number_hamb
    for i in range(0,number_hamb):
        hamburger[i] = classes.Item(scrrec.center, HAMBURGER)

    return extinguisher, asteroid, hamburger

def displayuniverse(extinguisher, asteroid, hamburger, screen, astronautx, astronauty):

    for i in range(0,len(extinguisher)):
        extinguisher[i].display(screen, astronautx, astronauty)
    for i in range(0,len(asteroid)):
        asteroid[i].display(screen, astronautx, astronauty)
    for i in range(0,len(hamburger)):
        hamburger[i].display(screen, astronautx, astronauty)

def main():
    astronaut = classes.Astronaut(scrrec.center)
    extinguisher, asteroid, hamburger = universegenerator(50,200,50) # nombre d'items au depart

    # Map the back button to the escape key.
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    #a reactiver pour python 2.7
    #pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

    screenleft = screen.get_width()/2
    screentop = screen.get_height()/2

    game = True

    while game:

        # Android-specific:
        if android:
            if android.check_pause():
                android.wait_for_resume()

        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.pos[0] <= screenleft:
                    if ev.pos[1] <= screentop:
                        astronaut.extinguisher_right = True
                    if ev.pos[1] > screentop:
                        astronaut.extinguisher_left = True

                if ev.pos[0] > screenleft:
                    astronaut.fart = True

            if ev.type == pygame.MOUSEBUTTONUP:
                astronaut.extinguisher_right = False
                astronaut.extinguisher_left = False
                astronaut.fart = False

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                game = False

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                if astronaut.takeextinguisher == False:
                    astronaut.takeextinguisher = True
                else:
                    astronaut.takeextinguisher = False

        astronaut.mouvement()

        screen.blit(BACKGROUND, (0,0))

        pygame.draw.line(screen, (255, 0, 0), (screenleft, 0), (screenleft,screentop*2), 5) # afficher delimitation
        pygame.draw.line(screen, (255, 0, 0), (0, screentop), (screenleft,screentop), 5) # afficher delimitation

        displayuniverse(extinguisher, asteroid, hamburger, screen, astronaut.astroposition_x, astronaut.astroposition_y)

        astronaut.display(screen)

        pygame.display.flip()

    pygame.quit()

#a reactiver pour python 2.7
#if __name__ == '__main__':
#    main()

#a desactiver pour python 2.7
main()