# Alise Linda Viluma, av17098
# Requires Python and PyGame to run
# Avoid bullets and try to get the highest score

import sys
import pygame as pg
from constants import *
from gamestates import *

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((SCREEN_X, SCREEN_Y))
    pg.display.set_caption(TITLE)
    states = {"SPLASH": SplashScreen(),
              "GAMEPLAY": Gameplay(),
              "GAMEOVER": GameOver()}
    game = Game(screen, states, "SPLASH")
    game.run()
    pg.quit()
    sys.exit()