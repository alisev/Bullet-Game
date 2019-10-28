import constants
import pygame

'''
    Entity class. Used as basis for both Bullet and Character class.
'''

class Entity(pygame.sprite.Sprite):
    '''
        Entity data. Used to create both Bullet and Character class.
        Has the following properties:
            name            Entity's name.
            width, height   Entity's hitbox width and height
            color           Entity's color if it's srawn as a basic shape.
            image           Entity's sprite.
            rect            Necessary for drawing sprite
            hitbox          Entity's hitbox
            isActive        Indicates if entity is being used at the moment.
    '''
    def __init__(self, img):
        super().__init__()
        self.name = ""
        self.width = 0
        self.height = 0
        self.color = constants.WHITE # TODO not needed
        self.image = img
        self.rect = self.image.get_rect()
        self.hb_offset_x = 0
        self.hb_offset_y = 0
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)
        self.isActive = True

    def drawShape(self):
        # TODO not needed
        '''
            Draws the entity on screen as a triangle shape.
            Used only for testing, when entity does not have a drawn sprite.
        '''
        point_1 = [self.rect.x + self.width/2, self.rect.y]
        point_2 = [self.rect.x, self.rect.y + self.height]
        point_3 = [self.rect.x + self.width, self.rect.y + self.height]
        pygame.draw.polygon(constants.DISPLAYSURF, self.color, [point_1, point_2, point_3], 0)

    def drawSprite(self):
        # TODO not needed, pygame.sprite.group takes care of this
        '''
            Draws entity's sprite.
        '''
        constants.DISPLAYSURF.blit(self.image,(self.rect.x, self.rect.y))

    def drawHitbox(self):
        '''
            Draws character's hitbox border. For testing only.
        '''
        pygame.draw.rect(constants.DISPLAYSURF, (255,0,0), self.hitbox, 2)

    def move(self, move_x, move_y):
        # TODO Probably only used by player
        '''
            Recalculates entity's position on screen.
            move_x, move_y - Variables, which define how much the entity has moved.
        '''
        self.rect.x = self.rect.x + move_x
        self.rect.y = self.rect.y + move_y

    def bounds(self):
        # TODO Probably not needed anymore
        if self.rect.x < constants.BOUND_L:
            self.rect.x = constants.BOUND_L
            return True
        elif self.rect.x - self.width > constants.BOUND_R:
            self.rect.x = self.rect.x - self.width
            return True
        return False

    def updateHitbox(self):
        '''
            Updates entity's hitbox.
        '''
        self.hitbox = (self.rect.x + self.hb_offset_x, self.rect.y + self.hb_offset_y, self.width, self.height)

    def remove(self):
        '''
            Removes entity from screen.
        '''
        self.kill()
        self.hitbox = (0,0,0,0)
        self.isActive = False