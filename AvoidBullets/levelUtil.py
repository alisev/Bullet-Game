import constants
import math

def draw(group):
    '''
        Draws all bullets.
    '''
    group.draw(constants.DISPLAYSURF)

def isGroupEmpty(group, lvl):
    if len(group)==0:
        return lvl + 1
    return lvl

def calcCircular(obj, center_x, center_y):
    obj.rect.x = center_x + math.cos(obj.angle) * obj.radius
    obj.rect.y = center_y + math.sin(obj.angle) * obj.radius

def orbit(obj, center_x, center_y, a, b):
    '''
        Moves sprite in a circular path.
        obj - sprite to move
        origin_x, origin_y - path's center coordinates
    '''
    obj.angle = obj.angle + a * (b + 1)
    calcCircular(obj, center_x, center_y)

def explode(obj, center_x, center_y, a):
    '''
        Moves sprites away from a certain center position
    '''
    obj.radius = obj.radius + a
    calcCircular(obj, center_x, center_y)