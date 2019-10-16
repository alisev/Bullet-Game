# Alise Linda Viļuma, av17098
# Requires Python and PyGame to run
# Avoid bullets and try to get the highest score

import pygame, sys
from pygame.locals import *

# --Essentals for game running--
pygame.init()
SCR_X = 236
SCR_Y = 420
DISPLAYSURF = pygame.display.set_mode((SCR_X, SCR_Y))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()

# --A couple of constants used in the game--
FPS = 60
BGCOLOR = (16, 20, 38)
WHITE = (255, 255, 255)

# Speed in pixels per frame (default values)
x_speed = 0
y_speed = 0
speed = 3
 
# Start/current position
x_coord = SCR_X / 2 - 12
y_coord = SCR_Y / 6 * 5

# Splash, Gamewin and Gameover screen
# TODO: make the splash screen
# IMPORTANT: splash, gamewin and gameover cannot be all true!
display_splash = True
display_gameover = False
display_gamewin = False
font = pygame.font.Font(None, 36)

# Player object
# TODO: replace with a sprite
def drawPlayer(screen, x, y):
    pygame.draw.polygon(screen, WHITE, [[x + 16, y], [x, y + 24], [x + 32, y + 24]], 0)

def movePlayer(x, y):
    global x_coord
    global y_coord

    # Player's new coordinates
    x_coord = x_coord + x
    y_coord = y_coord + y

    # Player's bounds
    bound_x = SCR_X - 32
    bound_y = SCR_Y - 24

    # Keeps player within screen's bounds
    if x_coord > bound_x:
        x_coord = bound_x
    elif x_coord < 0:
        x_coord = 0

    if y_coord > bound_y:
        y_coord = bound_y
    elif y_coord < 0:
        y_coord = 0

# --Main game loop--
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print("User pressed a key")
            if event.key == pygame.K_LEFT:
                x_speed = speed * (-1)
            elif event.key == pygame.K_RIGHT:
                x_speed = speed
            elif event.key == pygame.K_UP:
                y_speed = speed * (-1)
            elif event.key == pygame.K_DOWN:
                y_speed = speed

        elif event.type == pygame.KEYUP:
            print("User let go of a key")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # Game logic
    movePlayer(x_speed, y_speed)

    # Refresh screen
    DISPLAYSURF.fill(BGCOLOR)

    # Drawing code
    drawPlayer(DISPLAYSURF, x_coord, y_coord)

    pygame.display.update()
    clock.tick(FPS)