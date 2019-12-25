import math

'''
    Calculates entity start positions and returns them as list
'''

def distributeEven(count, width, height, offset_x, offset_y):
    '''
        Calculates positions for sprites.
        count               Number of sprites
        width, height       Distance between first and last sprite
        offset_x, offset_y  Distance from screen's (0,0) coordinate and the first sprite
        sprite_width        Sprite's width
        moveUp              Indicates if every next sprite is going to be moved up.
    '''
    position_list = []
    if count <= 1:
        raise Exception("Error: Function distributeEven() cannot be used, when number of sprites is 1 or less.")
    increment_w = width/(count - 1)
    increment_h = height/(count - 1)
    for i in range(count):
        x = offset_x + i * increment_w
        y = offset_y + i * increment_h
        position_list.append((x, y))
    return position_list

def distributeAngle(count):
    '''
        Creates a list of angle values that are evenly distributed within a circle.
        count   A number of sprites
    '''
    position_list = []
    if count == 0:
        raise Exception("Error: Function distributeAngle() cannot be used, when number of sprites is 0.")
    angle = 0
    offset = 360/count
    for i in range(count):
        position_list.append(angle)
        angle += offset
    return position_list

def triangleFormation(count, pos, distance, angle = 0):
    '''
        Creates a list of positions, that are formated within a triangle.
        count       Entity count
        pos         Position for the first entity
        distance    Distance between entities
        angle       Triangle's angle
    '''
    position_list = []
    perRow = 1
    counter = 0
    row = 1
    for i in range(count):
        position_list.append(pos[:])
        row += 1
        if counter == perRow - 1: # sākas jauna rinda
            pos[0] -= int(distance/2) * (row - 1)
            pos[1] -= int((distance * math.sqrt(2))/2)
            perRow += 1
            counter = 0
        else:
            pos[0] += distance
            counter += 1
    return position_list