import pygame
import constants
import bullet
from chara import player
import levelUtil

rows = 3
countPerRow = 5
count = countPerRow * rows

speed = 10

isPrepared = False

def prepare(group, a):
    '''
        Prepares meteor groups, sprites and their start positions.
        group - sprite group that is being prepared.
        a - y position offset
    '''
    global isPrepared

    x = 0
    y = 0
    for i in range(countPerRow):
        l = constants.SCREEN_X/(countPerRow * 2) # if SCREEN_X = 800 and countPerRow = 4, then l = 100
        if a == 0:
            x = l * (i - 4) # if i = 2, then x = -200
            y = -l * i
        elif a == 1:
            x = constants.SCREEN_X + l * (i + 1) + l * countPerRow
            y = l * (i - countPerRow + 1) - l * countPerRow
        else:
            x = l + l * i * 2
            y = -800
        meteor = bullet.makeMeteor(x, y)
        group.add(meteor)
        levelUtil.allSprites.add(meteor)
    isPrepared = True

def update(lvl):
    '''
        Prepares level (if needed) and goes through bulletLists to update each sprite group's position.
        As soon as all meteors are gone, level is increased.
        lvl - current level
    '''
    if not isPrepared:
        levelUtil.bulletLists = levelUtil.createSpriteList(rows)
        for i in range(rows):
            prepare(levelUtil.bulletLists[i], i)
    
    for i in range(rows):
        for obj in levelUtil.bulletLists[i]:
            if i == 0:
                obj.move(speed, speed)
            elif i == 1:
                obj.move(-speed, speed)
            else:
                obj.move(0, speed)
            obj.collide(player)
            levelUtil.checkBounds_Y(obj)

    return levelUtil.isGroupEmpty(levelUtil.allSprites, lvl)
