import pygame as pg
import pygame.freetype
import os
import constants

'''
    Other useful functions.
'''

def renderText(screen, text, position, size, color = "yellow"):
    '''
        Renders text on screen.
    '''
    fontdir = os.path.dirname(os.path.abspath (__file__))
    font = pygame.freetype.Font(os.path.join (fontdir, "fonts", "retro gaming.ttf"), 22)
    font_color = ()
    try:
        font_color = constants.COLOR[color]
    except:
        print("A color with this name doesn't exist within COLOR dictionary in file 'constants.py'.")
        font_color = constants.COLOR["yellow"]
    render_text = font.render_to(screen, position, text, font_color, None)

def loadSprite(file_name):
    '''
        Loads sprite from folder 'sprites'.
    '''
    full_path = os.path.join("sprites", file_name)
    return pg.image.load(full_path)

def calcVector(start, end):
    '''
        Returns a vector between 2 coordinates.
    '''
    return [end[0] - start[0], end[1] - start[1]]
