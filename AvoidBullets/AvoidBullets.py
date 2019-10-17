# Alise Linda Viļuma, av17098
# Requires Python and PyGame to run
# Avoid bullets and try to get the highest score

# TODO: Add enemies and highscore

import pygame
from pygame.locals import *

# --Essentals for game running--
pygame.init()
SCR_X = 800
SCR_Y = 600
DISPLAYSURF = pygame.display.set_mode((SCR_X, SCR_Y))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
done = False

# --A couple of constants used in the game--
FPS = 60
BGCOLOR = (16, 20, 38)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (247,190,22)

# Speed in pixels per frame (default values)
x_speed = 0
y_speed = 0
speed = 3
 
# Start/current position
x_coord = SCR_X / 2 - 12
y_coord = SCR_Y / 6 * 5

# Splash, Gamewin and Gameover screen
# TODO: make the screens
# IMPORTANT: splash, gamewin and gameover cannot be all true!
display_splash = True
display_gameover = False
display_gamewin = False

# Fonts
# TODO: Choose a good font size and font family to use
title = pygame.font.Font(None, 48)
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

# -- Splash screen --
# -- TODO design and program a nice splash screen
# -- Instructions should be moved to separate page
while not done and display_splash:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            # TODO make menu items selectable via arrow keys and return key
            if event.key == pygame.K_RETURN:
                display_splash = False
    
    # Game logic

    # Refresh screen
    DISPLAYSURF.fill(BGCOLOR)

    # Drawing code
    # TODO: Proper title name and item position
    text = font.render("TODO game title", False, YELLOW)
    DISPLAYSURF.blit(text, [10, 10])

    text = font.render("Play", False, YELLOW)
    DISPLAYSURF.blit(text, [10, 40])

    text = font.render("Instructions", False, YELLOW)
    DISPLAYSURF.blit(text, [10, 70])

    pygame.display.update()
    clock.tick(FPS)

# -- Game Over screen --
# -- TODO: Make one

# -- Main game loop --
while not done and display_splash == False and display_gameover == False and display_gamewin == False:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

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

pygame.quit()