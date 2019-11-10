import pygame as pg
import bullet
import constants

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
        if self.level_num < len(self.levels):
            self.level_num = self.level.update(self.level_num)
            return False
        return True

    def draw(self):
        '''
            Draws current level.
        '''
        screen = pg.display.get_surface()
        self.level.allSprites.draw(screen)

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
    def __init__(self, a, b):
        self.bullet_rows = a
        self.bullets_perRow = b
        self.bullet_count = self.bullet_rows * self.bullets_perRow

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

    def populateEnemyLists(self, a):
        self.enemyList = self.createSpriteList(a)

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

    def prepare(self, a=1):
        '''
            Prepares level for the gameplay.
            a   Number of enemy sprite groups.
        '''
        if not self.isPrepared:
            self.populateBulletLists()
            self.populateEnemyLists(a)
            for i in range(self.bullet_rows):
                self.prepareLevel(i)
            self.isPrepared = True

    def prepareLevel(self, a):
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
    
    def prepareLevel(self, a):
        x = 0
        y = 0
        for i in range(self.bullets_perRow):
            l = constants.SCREEN_X/(self.bullets_perRow * 2)
            if a == 0:
                x = l * (i - 4)
                y = -l * i
            elif a == 1:
                x = constants.SCREEN_X + l * (i + self.bullets_perRow + 1)
                y = l * (i - 2 * self.bullets_perRow + 1)
            else:
                x = l * (1 + i * 2)
                y = -800
            meteor = bullet.Meteor(x, y)
            self.allSprites.add(meteor)
            self.bulletLists[a].add(meteor)
            self.isPrepared = True

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
                # obj.collide(player) # TODO check collission between bulletLists and player by using pygames native functions
                obj.checkBounds(False, False, True, False)

class Level_2(LevelBlueprint):
    def __init__(self):
        super().__init__(2, 5)

    def prepareLevel(self):
        pass

    def updateLevel(self):
        pass

levelList = [Level_1(), Level_2()]