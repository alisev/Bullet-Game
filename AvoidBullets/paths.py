import math
import util

'''
    Functions that moves entity's in a path. 
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

def followEntity(entity_target, entity_move, enable_rotation):
    '''
        An individual entity flies moves towards another.
        entity_target       A target entity
        entity_move         An entity that moves towards entity_target
        enable_rotation     Enable rotation of entity_move sprite
    '''
    start_pos = entity_move.getEntityPos()
    target_pos = entity_target.getEntityPos()
    vector = util.calcVector(start_pos, target_pos)
    entity_move.angle = calcAngle(vector)
    entity_move.radius = entity_move.speed
    calcCircular(entity_move, entity_move.rect.x, entity_move.rect.y)

def aimAtEntity(entity_target, entity_aim, entity_rotation = False):
    '''
        Aims a group of sprites at an entity
        entity_target       A target entity
        entity_aim          An entity that is aimed at entity_target
        enable_rotation     Enable rotation of entity_aim sprite
    '''
    start_pos = entity_aim.getEntityPos()
    target_pos = entity_target.getEntityPos()
    vector = util.calcVector(start_pos, target_pos)
    #TODO if entity_rotation==True, calculate angle, how far the sprite needs to be rotated
    return vector

def calcAngle(vec):
    '''
        Calculates angle from vector.
        vec Vector
    '''
    angle = math.atan2(vec[1], vec[0])
    return math.degrees(angle)

def calcDistance(entity1, entity2):
    '''
        Calculates distance between two entities.
    '''
    pos1 = entity1.getEntityPos()
    pos2 = entity2.getEntityPos()
    vector = util.calcVector(pos1, pos2)
    distance = math.sqrt(vector[0]**2 + vector[1]**2)
    return distance
    
