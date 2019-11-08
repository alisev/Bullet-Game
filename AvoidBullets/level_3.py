import pygame
import math
import constants
import bullet
import chara
import levelUtil

rings = 10
count = 12
total = rings * count

speed_r = 2
speed_a = 1

threshold = 10 # radius of a ring, that triggers movement of the next ring

bug = chara.makeBug((constants.SCREEN_X / 2) - 25, -50)

isPrepared = False

def prepare():
    global isPrepared

    levelUtil.clearSpriteLists()
    levelUtil.enemyLists = levelUtil.createSpriteList(1)
    levelUtil.bulletLists = levelUtil.createSpriteList(rings)

    for i in range(rings):
        angle = 0
        offset = 360/12
        for j in range(count):
            angle = angle + offset
            ball = bullet.makeSmallBall(bug.rect.x + 36, bug.rect.y + 36, angle, 1)
            levelUtil.bulletLists[i].add(ball)
            bug.children.add(ball)
            levelUtil.allSprites.add(ball)

    levelUtil.allSprites.add(bug)
    levelUtil.enemyLists[0].add(bug)
    isPrepared = True

def update(lvl):
    if not isPrepared:
        prepare()

    if bug.rect.y < 150:
        speed = 3
        bug.move(0, speed)
    else:
        th_reached = False

        for ring in levelUtil.bulletLists:
            for ball in ring:
                if ring == levelUtil.bulletLists[0] or ball.radius > 0 or (ball.radius == 0 and th_reached == True):
                    levelUtil.explode(ball, bug.rect.x + 36, bug.rect.y + 36, speed_r)
                    levelUtil.orbit(ball, bug.rect.x + 36, bug.rect.y + 36, speed_a)
                    if ball.radius == threshold:
                        th_reached = True
                    else:
                        th_reached = False
                ball.collide(chara.player)

                levelUtil.checkBounds(ball, 14)

    if len(levelUtil.allSprites) == 1:
        # At the end of the level the Bug Alien exits the screen
        bug.move(0, -5)
        levelUtil.checkBounds(bug, 72)
    # needs a check, when all bulletlIsts are empty
    return levelUtil.isGroupEmpty(levelUtil.allSprites, lvl)
