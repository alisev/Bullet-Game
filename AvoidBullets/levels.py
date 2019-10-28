import pygame
import constants
import level_1
import level_2

'''
    Contains functions for highscores and levels.
    TODO Test all these functions.
'''

highscore = 0
lvl = 0

def callLevel():
    '''
        Calls the required level.
        Each level calls certain functions that define what enemies appear and their behaviour.
        They contain a couple of if conditions to check how far player is in the level and when the next enemy needs to be brought in.

        More levels can be added later.
    '''
    global lvl

    if lvl == 0:
        lvl = level_1.update(lvl)
    if lvl == 1:
        lvl = level_2.update(lvl)

def draw():
    if lvl == 0:
        level_1.draw()
    elif lvl == 1:
        level_2.draw()

def highscoreCounter(pts):
    '''
        Increases the highscore counter.
        pts - points awarded
    '''
    global highscore
    highscore += pts
    if highscore > 99999999:
        highscore = 99999999 # Max score for now

def advanceLevel():
    '''
        Increases level counter.
    '''
    global lvl
    lvl += 1

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
    font = pygame.font.Font(None, 48)

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
    font = pygame.font.Font(None, 36)
    x_pos = 650
    y_pos = 20
    score = font.render(str(highscore), False, constants.YELLOW)
    constants.DISPLAYSURF.blit(score, [x_pos, y_pos])

def collissionAndBounds(obj, pts):
    hasCollided = obj.collide(player)
    if not hasCollided:
        highscoreCounter(pts)
    if obj.rect.y > constants.SCREEN_Y:
        obj.remove()