#-------------------------------------------------------------------------------
# Name:        Proutpulsor
#
# Author:      Sivigik
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------
import pygame
from pygame.locals import *
# Set the screen size.
screen = pygame.display.set_mode((0,0), FULLSCREEN)#(800, 480))
pygame.init()



import classes
from constantes import *

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

def main():
    astronaut = classes.Astronaut(350, 240)

    # Map the back button to the escape key.
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    # Use a timer to control FPS.
    pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

    screenleft = screen.get_width()/2

    while True:

        ev = pygame.event.wait()

        # Android-specific:
        if android:
            if android.check_pause():
                android.wait_for_resume()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.pos[0] <= screenleft:
                astronaut.extinguisher = True
            elif ev.pos[0] > screenleft:
                astronaut.fart = True


        elif ev.type == pygame.MOUSEBUTTONUP:
            astronaut.extinguisher = False
            astronaut.fart = False


        # When the user hits back, ESCAPE is sent. Handle it and end
        # the game.
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            break
        astronaut.mouvement()
        screen.blit(BACKGROUND, (0,0))
        astronaut.affiche(screen)
        pygame.display.flip()

# This isn't run on Android.
if __name__ == "__main__":
    main()