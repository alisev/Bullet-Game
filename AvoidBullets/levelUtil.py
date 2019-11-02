import constants

def draw(group):
    '''
        Draws all bullets.
    '''
    group.draw(constants.DISPLAYSURF)

def isGroupEmpty(group, lvl):
    if len(group)==0:
        return lvl + 1
    return lvl
