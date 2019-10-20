'''
    Game assets, that aren't characters
'''

import pygame

class Asset():
    '''
        Asset object data. Has the following properties:
        name            Asset's name
        sprite          Image file that represents the asset
        width, height   Asset's width and height
        position        Asset's position on screen
    '''
    def __init__(self):
        name = ""
        sprite = ""
        width = 0
        height = 0
        position = [0, 0]
    def draw(screen):
        '''
            Draws asset's sprite on screen
        '''

title_logo = Asset()
title_logo.name = "Game's title"
title_logo.sprite = ""
title_logo.width = 564
title_logo.height = 176
title_logo.position = [118, 100]
