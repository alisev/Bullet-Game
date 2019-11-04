import constants
import math
from chara import player

def draw(group):
    '''
        Draws all bullets.
    '''
    group.draw(constants.DISPLAYSURF)

def isGroupEmpty(group, lvl):
    '''
        Checks if sprite group is empty.
    '''
    if len(group)==0:
        return lvl + 1
    return lvl

def calcCircular(obj, center_x, center_y):
    '''
        Converts degrees to radians and recalculates sprite's position
    '''
    rad = math.radians(obj.angle)
    obj.rect.x = center_x + math.cos(rad) * obj.radius
    obj.rect.y = center_y + math.sin(rad) * obj.radius

def orbit(obj, center_x, center_y, speed):
    '''
        Moves sprite in a circular path.
    '''
    obj.angle += speed
    calcCircular(obj, center_x, center_y)
    obj.updateHitbox()

def explode(obj, center_x, center_y, speed):
    '''
        Moves sprites away from a certain center position
    '''
    obj.radius += speed
    calcCircular(obj, center_x, center_y)
    obj.updateHitbox()

def moveDown(obj, speed):
    '''
        Moves sprite straight down
    '''
    obj.rect.y += speed
    obj.updateHitbox()

def getPlayerPos(obj):
    '''
        Returns the angle of the vector, that connects bullet and the player
        obj - entity that is targeting the player
    '''
    x_dif = player.rect.x - obj.rect.x
    y_dif = player.rect.y - obj.rect.y
    angle = math.atan2(y_dif, x_dif)
    angle = math.degrees(angle)
    return angle

def checkBounds(obj, min):
    '''
        Checks if sprite has gone out of bounds
        min - sprite's width. Ensures that sprite isn't visible onscreen
    '''
    if obj.rect.x > constants.SCREEN_X or obj.rect.x < -min or obj.rect.y > constants.SCREEN_Y or obj.rect.y < -min:
        obj.remove()

