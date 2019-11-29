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

def displayBest():
    '''
        Displays 10 best scores on screen from the ones saved in a file.
    '''
    pass

def increaseScore(score, points):
    '''
        Rewards player with points.
    '''
    score += points
    return score

def saveScore(score):
    '''
        Saves player's score and name.
    '''
    pass

