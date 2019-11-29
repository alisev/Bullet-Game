import pygame as pg
from constants import *
import os # TODO for loading/writing highscore file

'''
    Functions related to highscore display, calculation and saving.
'''

def displayScore(screen, score):
    '''
        Formats player's score and displays it on screen.
        screen      Gameplay surface
        score       Player's score
    '''
    digit_count = 8
    score_digits = len(str(score))
    zero_count = digit_count - score_digits
    player_score = "0" * zero_count + str(score) if (zero_count > 0) else str(score)
    
    pos = [650, 25]
    font = pg.font.Font(None, 36)
    score_display = font.render(player_score, True, YELLOW)
    screen.blit(score_display, pos)

def displayBest(screen, highscores):
    '''
        Displays 10 best scores on screen from the ones saved in a file.
    '''
    counter = 0
    text_y = 300
    font = pg.font.Font(None, 16)
    for score in highscores:
        if counter == 10:
            break
        render_score = font.render(str(score[0]), True, YELLOW)
        screen.blit(render_score, [100, text_y])
        render_name = font.render(score[1], True, YELLOW)
        screen.blit(render_name, [400, text_y])
        text_y += 24
        counter += 1

def increaseScore(score, points):
    '''
        Rewards player with points.
    '''
    score += points
    return score

def saveScore(score, name):
    '''
        Saves player's score and name.
    '''
    file_name = "high.score"
    f = open(file_name, "a")
    record = str(score) + ' ' + name
    f.write(record)
    f.close()

def loadFromFile():
    '''
        Opens the specified file and loads its contents in a list.
    '''
    file_name = "high.score"
    highscore_list = []
    f = open(file_name)
    for line in f:
        if line[0] == '#':
            pass
        else:
            line = line.rstrip()
            score_name = line.split(" ", 1)
            highscore_list.append(score_name)
    f.close()
    highscore_list = sortScores(highscore_list)
    return highscore_list

def sortScores(score_list):
    '''
        Sorts a nested list by first attribute.
    '''
    for record in score_list:
        record[0] = int(record[0])
    score_list.sort(reverse=True)
    return score_list

def comparePlayerScore(highscore_list, player_score):
    '''
        Does a comparision between 10 best scores and player's. If player has a higher score than any of the listed ones, then it is added to the list.
    '''
    for score in highscore_list:
        if score[0] < player_score:
            player_name = nameInput()
            saveScore(player_score, player_name)
            highscore_list.append([player_score, player_name])
            highscore_list = sortScores(highscore_list)
            break
    print(highscore_list)
    return highscore_list

def nameInput():
    '''
        Allows player to input their name.
    '''
    name = "TODO"
    return name