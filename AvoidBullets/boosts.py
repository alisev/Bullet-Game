import pygame as pg
import os

class Boost(pg.sprite.Sprite):
    '''
        Handles boosts that give player certain benefits.
        name            Boost's name
        image           Sprite image
        modifier        Boost's "strength"
        frame_counter   Indicates for how many more frames the effect is active
        active          bool, indicates if boost is still active
    '''
    def __init__(self, img):
        super().__init__()
        full_path = os.path.join("sprites", img)
        sprite = pg.image.load(full_path).convert_alpha()
        self.name = ""
        self.image = sprite
        self.modifier = 0
        self.frame_counter = 0
        self.active = False

    def update(self):
        '''
            Upon colliding with player, calls their specific effect.
        '''
        pass

class BoostLife(Boost):
    def __init__(self, variant):
        sprites = ["boost_life_1.png"]
        names = [" +1"]
        modifier_vals = [1]
        super().__init__(sprites[variant])
        self.name = "Life boost" + names[variant]
        self.modifier = modifiers[variant]
    def update(self, entity):
        entity.lives += 1

class BoostSpeed(Boost):
    pass

class BoostPower(Boost):
    pass

class BoostInvincible(Boost):
    pass