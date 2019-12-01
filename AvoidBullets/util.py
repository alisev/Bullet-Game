import pygame as pg
import os
from constants import *

'''
    Other useful functions.
'''

def renderText(screen, text, position, size):
    '''
        Renders text on screen.
    '''
    type_face = None
    font = pg.font.Font(type_face, size)
    render_text = font.render(text, True, YELLOW)
    screen.blit(render_text, position)

def loadSprite(file_name):
    '''
        Loads sprite from folder 'sprites'.
    '''
    full_path = os.path.join("sprites", file_name)
    return pg.image.load(full_path)
