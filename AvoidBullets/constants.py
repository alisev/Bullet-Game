'''
    A list of constants used in the game.
'''

import pygame

# Window dimensions
SCREEN_X = 800
SCREEN_Y = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_X, SCREEN_Y)) # Moved here, so that the variable can be used across files.

FPS = 30
TITLE = "Space Cruise"

# Colors used
BGCOLOR = (16, 20, 38)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (247,190,22)
