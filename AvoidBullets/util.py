import pygame as pg
import pygame.freetype
import os
from constants import *

'''
    Other useful functions.
'''

def renderText(screen, text, position, size):
    '''
        Renders text on screen.
    '''
    fontdir = os.path.dirname(os.path.abspath (__file__))
    font = pygame.freetype.Font(os.path.join (fontdir, "fonts", "retro gaming.ttf"), 22)
    render_text = font.render_to(screen, position, text, YELLOW, None)

def loadSprite(file_name):
    '''
        Loads sprite from folder 'sprites'.
    '''
    full_path = os.path.join("sprites", file_name)
    return pg.image.load(full_path)
