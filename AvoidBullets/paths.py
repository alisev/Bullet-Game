import math

'''
    Functions that move entities in certain paths. 
'''

def explode(entity, x_origin, y_origin, speed):
    '''
        Makes entity move away from a center point.
        entity                  Entity or entity subclass object
        x_origin, y_origin      Center point
        speed                   Radius increase between center point and the entity
    '''
    entity.radius += speed
    calcCircular(entity, x_origin, y_origin)
    entity.updateHitbox()

def orbit(entity, x_origin, y_origin, speed):
    '''
        Makes entity orbit around a center point.
        entity                  Entity or entity subclass object
        x_origin, y_origin      Center point
        speed                   Angle in degrees
    '''
    entity.angle += speed
    calcCircular(entity, x_origin, y_origin)
    entity.updateHitbox()

def calcCircular(entity, x_origin, y_origin):
    '''
        Helper function for explode and orbit.
        entity                  Entity or entity subclass object
        x_origin, y_origin      Center point
    '''
    rad = degrees2rad(entity.angle)
    entity.rect.x = x_origin + math.cos(rad) * entity.radius
    entity.rect.y = y_origin + math.sin(rad) * entity.radius

def degrees2rad(angle):
    '''
        Helper function that converts given angle from degrees to radians.
    '''
    return math.radians(angle)