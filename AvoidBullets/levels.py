import pygame as pg
import bullet
import chara
from constants import *
import paths

'''
    Contains functions that handles all level logic and rendering.
'''

class Level():
    '''
        Contains functions that handles all level logic and rendering.
        level_num   Current level number
        levels      A dict containing all levels
        level       Current level
    '''
    def __init__(self, levelList):
        self.level_num = 0
        self.levels = levelList
        self.level = self.levels[self.level_num]
    
    def call(self):
        '''
            Calls current level's game logic, updates level_num when level is completed and returns True or False value to indicate if the game has been beaten.
        '''
        levelCount = len(self.levels)
        if self.level_num < levelCount:
            self.level_num = self.level.update(self.level_num)
            if self.level_num == levelCount:
                return True
            else:
                self.level = self.levels[self.level_num]
                return False
        return True

    def draw(self):
        '''
            Draws current level.
        '''
        screen = pg.display.get_surface()
        if self.level_num < len(self.levels):
            self.level.allSprites.draw(screen)

    def entityCollission(self, entity):
        '''
            Checks for collissions between passed entity (player) and each group in BulletLists.
            entity  Passed entity object
        '''
        for group in self.level.bulletLists:
            list = pg.sprite.spritecollide(entity, group, True)
            if len(list) > 0:
                entity.gotHit()

    def groupCollission(self, group):
        '''
            Checks for collissions between the passed group and each group in EnemyLists.
            group   Passed group object
        '''
        for enemyGroup in self.level.enemyLists:
            hitEnemies = pg.sprite.groupcollide(enemyGroup, group, False, True)
            for enemy in hitEnemies:
                enemy.gotHit()

class LevelBlueprint():
    '''
        A blueprint class for level creation.
        bullet_rows     Amount of rows with bullets
        bullets_perRow  Amount of bullets per row
        bullet_count    Total amount of bullets
        allSprites      All sprites in current level
        bulletLists     Array of bullet sprite groups
        enemyLists      Array of enemy sprite groups
        isPrepared      Indicates if level has been prepared for gameplay
    '''
    def __init__(self, a, b, c = 1, d = 0):
        self.bullet_rows = a
        self.bullets_perRow = b
        self.bullet_count = self.bullet_rows * self.bullets_perRow

        self.enemyGroupCount = c
        self.enemy_perGroup = d

        self.allSprites = pg.sprite.Group()
        self.bulletLists = []
        self.enemyLists = []

        self.isPrepared = False

    def createSpriteList(self, n):
        '''
            Creates sprite group arrays. Used for bulletLists and enemyLists.
            Function is called by populateBulletLists and populateEnemyLists
        '''
        array = []
        for i in range(n):
            array.append(pg.sprite.Group())
        return array

    def populateBulletLists(self):
        self.bulletLists = self.createSpriteList(self.bullet_rows)

    def populateEnemyLists(self):
        self.enemyLists = self.createSpriteList(self.enemyGroupCount)

    def clearSpriteLists(self):
        '''
            Clears all sprite lists.
        '''
        self.allSprites.empty()
        self.bulletLists.clear()
        self.enemyLists.clear()

    def update(self, lvl):
        '''
            Updates game logic in current level.
            lvl     Current level
        '''
        self.prepare()
        self.updateLevel()
        return self.isGroupEmpty(self.allSprites, lvl)

    def updateLevel(self):
        '''
            Empty function for updating level to avoid errors in prepare() function.
            This function is properly defined and used in each level's class.
        '''
        pass

    def prepare(self):
        '''
            Prepares level for the gameplay.
        '''
        if not self.isPrepared:
            self.populateBulletLists()
            self.populateEnemyLists()
            self.prepareLevel()
            self.isPrepared = True

    def prepareLevel(self, row):
        '''
            Empty function for level preparation to avoid errors in prepare() function.
            This function is properly defined and used in each level's class.
        '''
        pass

    def isGroupEmpty(self, group, lvl):
        '''
            Checks if given sprite group is empty.
            group   Sprite group to be checked
            lvl     Current level
        '''
        if len(group) == 0:
            return lvl + 1
        return lvl

class Level_1(LevelBlueprint):
    def __init__(self):
        super().__init__(3, 5)
    
    def prepareLevel(self):
        for row in range(self.bullet_rows):
            x = 0
            y = 0
            for i in range(self.bullets_perRow):
                l = SCREEN_X/(self.bullets_perRow * 2)
                if row == 0:
                    x = l * (i - 4)
                    y = -l * i
                elif row == 1:
                    x = SCREEN_X + l * (i + self.bullets_perRow + 1)
                    y = l * (i - 2 * self.bullets_perRow + 1)
                else:
                    x = l * (1 + i * 2)
                    y = -800
                meteor = bullet.makeMeteor(x, y)
                self.allSprites.add(meteor)
                self.bulletLists[row].add(meteor)

    def updateLevel(self):
        '''
            Prepares enemies and bullets at the start of the level and handles game logic.
        '''
        for i in range(self.bullet_rows):
            for obj in self.bulletLists[i]:
                if i == 0:
                    obj.move(obj.speed, obj.speed)
                elif i == 1:
                    obj.move(-obj.speed, obj.speed)
                else:
                    obj.move(0, obj.speed)
                obj.checkBounds(False, False, True, False)

class Level_2(LevelBlueprint):
    def __init__(self):
        super().__init__(10, 12, 1, 1)

    def prepareLevel(self):
        self.bug = chara.makeBug((SCREEN_X / 2) - 25, -50)

        for i in range(self.bullet_rows):
            angle = 0
            offset = 360/self.bullets_perRow
            for j in range(self.bullets_perRow):
                angle += offset
                ball = bullet.makeSmallBall(self.bug.rect.x + 36, self.bug.rect.y + 36, angle, 1)
                self.bug.children.add(ball)
                self.bulletLists[i].add(ball)
                self.allSprites.add(ball)
        self.allSprites.add(self.bug)
        self.enemyLists[0].add(self.bug)

    def updateLevel(self):
        if self.bug.rect.y < 150:
            self.bug.move(0, self.bug.speed)
        else:
            threshold = 10
            th_reached = False
            speed_r = 2
            speed_a = 1

            for ring in self.bulletLists:
                for ball in ring:
                    if ring == self.bulletLists[0] or ball.radius > 0 or (ball.radius == 0 and th_reached == True):
                        paths.explode(ball, self.bug.rect.x + 36, self.bug.rect.y + 36, speed_r)
                        paths.orbit(ball, self.bug.rect.x + 36, self.bug.rect.y + 36, speed_a)
                        if ball.radius == threshold:
                            th_reached = True
                        else:
                            th_reached = False

levelList = [Level_1(), Level_2()]