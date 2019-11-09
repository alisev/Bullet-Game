import pygame as pg
import constants
import level_1
import level_2
import level_3
import chara
import levelUtil

'''
    Contains game logic that isn't specific to any level
'''

highscore = 0
lvl = 0
levelList = [level_1, level_2, level_3]

def callLevel():
    '''
        Calls the required level function. If player has beaten all levels, then a game win screen is shown.
    '''
    global lvl

    if lvl < len(levelList):
        lvl = levelList[lvl].update(lvl)
    else:
        # TODO switch to gamewin loop
        pass

def draw():
    if lvl < len(levelList):
        levelUtil.draw(levelUtil.allSprites)
    else:
        # TODO call gamewin draw function
        pass

def highscoreCounter(pts):
    '''
        Increases the highscore counter.
        pts - points awarded
    '''
    global highscore
    highscore += pts
    if highscore > 99999999:
        highscore = 99999999 # Max score for now

def saveHighscore():
    '''
        Saves score when game is finished.
    '''
    file = open("highscore.txt", "a")
    file.write(highscore, '\n')
    file.close()

def prepareHighscoreList():
    '''
        Makes a list of 10 best scores.
    '''
    file = open("highscore.txt", "r")
    scoreList = []
    for line in file:
        scoreList.append(line)
    file.close()
    scoreList.sort(True)
    return scoreList

def showHighscore(scoreList):
    '''
        Shows a list of 10 best highscores in highscore 
    '''
    font = pg.font.Font(None, 48)

    text_y_pos = 100

    text = font.render('Highscores', False, constants.YELLOW)
    constants.DISPLAYSURF.blit(text, [10, text_y_pos])

    for i in range(10):
        text = font.render(scoreList[i], False, constants.YELLOW)
        constants.DISPLAYSURF.blit(text, [10, text_y_pos+(i+1)*50])

def displayHighscoreCounter():
    '''
        Displays player's current score.
    '''
    font = pg.font.Font(None, 36)
    x_pos = 650
    y_pos = 20
    score = font.render(str(highscore), False, constants.YELLOW)
    constants.DISPLAYSURF.blit(score, [x_pos, y_pos])

def playerBulletsMove():
    for blt in chara.player.children:
        blt.move(0, -5)
        if lvl < len(levelList):
            for list in levelUtil.enemyLists:
                for enemy in list:
                    blt.collide(enemy)
        levelUtil.checkBounds(blt, 10)