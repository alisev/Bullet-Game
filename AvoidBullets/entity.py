import constants
import pygame

'''
    Entity class. Used as basis for both Bullet and Character class.
'''

class Entity(pygame.sprite.Sprite):
    '''
        Character data. Used for both the player and enemies. Has the following properties:
            name            Entity's name.
            x_pos, y_pos    Entity's position on screen
            width, height   Entity's width and height
            color           Entity's color if it's srawn as a basic shape.
            image           Entity's sprite.
            hitbox          Entity's hitbox
    '''
    def __init__(self, img):
        super().__init__()
        self.name = ""
        self.x_pos = 0
        self.y_pos = 0
        self.width = 0
        self.height = 0
        self.color = constants.WHITE
        self.image = img
        self.hitbox = (self.x_pos, self.y_pos, self.width, self.height)

    def draw(self):
        '''
            Draws the entity on screen.
        '''
        point_1 = [self.x_pos + self.width/2, self.y_pos]
        point_2 = [self.x_pos, self.y_pos + self.height]
        point_3 = [self.x_pos + self.width, self.y_pos + self.height]
        pygame.draw.polygon(constants.DISPLAYSURF, self.color, [point_1, point_2, point_3], 0)

    def drawHitbox(self):
        '''
            Draws character's hitbox border. For testing only.
        '''
        pygame.draw.rect(constants.DISPLAYSURF, (255,0,0), selif.hitbox, 2)