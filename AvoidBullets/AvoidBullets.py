# Alise Linda Viļuma, av17098
# Requires Python and PyGame to run
# Avoid bullets and try to get the highest score

# TODO: Add enemies and highscore

import pygame
import constants
import chara
import bullet

# --Essentals for game running--
pygame.init()
constants.DISPLAYSURF
pygame.display.set_caption(constants.TITLE)
clock = pygame.time.Clock()
done = False

# --Loads a couple of sprites--
TITLE_LOGO = pygame.image.load("sprites\\title.png").convert_alpha()

# Splash, Gamewin and Gameover screen
# TODO: make the screens
# IMPORTANT: splash, gamewin and gameover cannot be all true!
display_splash = True
display_gameover = False
display_gamewin = False

# Fonts
# TODO: Choose a good font size and font family to use
title = pygame.font.Font(None, 48)
font = pygame.font.Font(None, 48)

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
    constants.DISPLAYSURF.fill(constants.BGCOLOR)

    # Drawing code
    # TODO: Proper title name and item position
    constants.DISPLAYSURF.blit(TITLE_LOGO,(121,100))

    text = font.render('Play', False, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [10, 300])

    text = font.render('Level select', False, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [10, 350])

    text = font.render('Instructions', False, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [10, 400])

    text = font.render('Quit', False, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [10, 450])

    pygame.display.update()
    clock.tick(constants.FPS)

# -- Game Over screen --
# -- TODO: Make one

# -- Main game loop --
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            print("User pressed a key")
            if event.key == pygame.K_LEFT:
                chara.player.moveX(-1)
            elif event.key == pygame.K_RIGHT:
                chara.player.moveX(1)
            elif event.key == pygame.K_UP:
                chara.player.moveY(-1)
            elif event.key == pygame.K_DOWN:
                chara.player.moveY(1)

        elif event.type == pygame.KEYUP:
            print("User let go of a key")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                chara.player.moveX(0)
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                chara.player.moveY(0)

    # Game logic
    chara.player.recalcPos()
    bullet.test.recalcPos(1, 1)

    # TODO move the function inside recalcPos
    # TODO when collission is detected, the game should show gameover screen
    bullet.test.collide(chara.player)

    # Refresh screen
    constants.DISPLAYSURF.fill(constants.BGCOLOR)

    # Drawing code
    constants.DISPLAYSURF.blit(chara.player.image,(chara.player.x_pos, chara.player.y_pos))
    bullet.test.draw()

    bullet.test.drawHitbox()
    chara.player.drawHitbox()

    pygame.display.update()
    clock.tick(constants.FPS)

pygame.quit()