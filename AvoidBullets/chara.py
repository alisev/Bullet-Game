import pygame as pg
import constants
import entity
import bullet

'''
    Defines character class and objects.
'''

class Character(entity.Entity):
    '''
        Character data. Used for both the player and enemies.
        Has the following properties. The rest are defined in Entity class.
            move_x, move_y  Character's movement "vectors". Value usually switches between -1, 0 and 1. When value is -1 or 1 the character is moving across the screen, when 0 - it is still
            lives           Number of lives a character has. Each character has 1 life by default.
            isPlayer        Defines if character is the player
            children        Bullet sprite group
    '''
    def __init__(self, img):
        super().__init__(img)
        self.move_x = 0
        self.move_y = 0
        self.lives = 1
        self.children = pg.sprite.Group()

    def remove(self):
        '''
            Removes entity from screen.
        '''
        self.kill()
        for child in self.children:
            child.kill()
        self.hitbox = (0,0,0,0)

    def removeLifePoint():
        self.lives -= 1


# Player specific function
def displayLives():
    '''
        Displays how many lives player has left.
    '''
    font = pg.font.Font(None, 36)
    lives = font.render('Lives: ' + str(player.lives), False, constants.YELLOW)
    constants.DISPLAYSURF.blit(lives, [20, 20])

def makeBallUFO(pos_x, pos_y):
    image = pg.image.load("sprites\\ballUFO.png").convert_alpha()
    enemy = Character(image)
    enemy.name = "Ball UFO"
    enemy.rect.x = pos_x
    enemy.rect.y = pos_y
    enemy.width = 34
    enemy.height = 34
    enemy.hb_offset_x = 8
    enemy.hb_offset_y = 8
    enemy.children = pg.sprite.Group()
    return enemy

def makeBug(pos_x, pos_y):
    image = pg.image.load("sprites\\bug.png").convert_alpha()
    enemy = Character(image)
    enemy.name = "Bug alien"
    enemy.rect.x = pos_x
    enemy.rect.y = pos_y
    enemy.width = 52
    enemy.height = 52
    enemy.hb_offset_x = 10
    enemy.hb_offset_y = 10
    enemy.lives = 25
    enemy.children = pg.sprite.Group()
    return enemy
