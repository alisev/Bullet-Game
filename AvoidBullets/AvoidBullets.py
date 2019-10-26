# Alise Linda Viļuma, av17098
# Requires Python and PyGame to run
# Avoid bullets and try to get the highest score

import pygame
import constants
import chara
import bullet
import levels

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
gameEnd = False

# Fonts
font = pygame.font.SysFont('Consolas', 28)

# -- Splash screen --
while not done and display_splash:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                display_splash = False
    
    # Game logic

    # Refresh screen
    constants.DISPLAYSURF.fill(constants.BGCOLOR)

    # Drawing code
    # Text formating
    LINE_SPACING = 40
    ITEM_X_POS = 100
    FIRST_ITEM_Y_POS = 350

    constants.DISPLAYSURF.blit(TITLE_LOGO,(121,100))

    text = font.render('Instructions:', True, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [ITEM_X_POS, FIRST_ITEM_Y_POS])

    text = font.render(' - Use arrow keys to avoid projectiles', True, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [ITEM_X_POS, FIRST_ITEM_Y_POS + LINE_SPACING])

    text = font.render(' - Survive for as long as you can', True, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [ITEM_X_POS, FIRST_ITEM_Y_POS + LINE_SPACING * 2])

    text = font.render('Press Enter key to start the game', True, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [ITEM_X_POS, FIRST_ITEM_Y_POS + LINE_SPACING * 3 + 20])

    pygame.display.update()
    clock.tick(constants.FPS)

# -- Main game loop --
while not done and gameEnd == False:
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
    levels.callLevel()
    # recalc pos for all sprites
    # test for collissions

    # Refresh screen
    constants.DISPLAYSURF.fill(constants.BGCOLOR)

    # Drawing code
    chara.spriteList.draw(constants.DISPLAYSURF)
    levels.bulletList.draw(constants.DISPLAYSURF)

    chara.player.drawHitbox()

    levels.displayHighscoreCounter()
    chara.displayLives()

    pygame.display.update()
    clock.tick(constants.FPS)

# -- Gameover loop --
while not done and gameEnd:
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print('TODO: Return to menu')

    #Game Logic

    # Refresh screen
    constants.DISPLAYSURF.fill(constants.BGCOLOR)

    #Drawing code


pygame.quit()