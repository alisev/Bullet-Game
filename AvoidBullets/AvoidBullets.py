# Alise Linda Viluma, av17098
# Requires Python and PyGame to run
# Avoid bullets and try to get the highest score

import sys
import pygame as pg
import constants
import gamestates

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((constants.SCREEN_X, constants.SCREEN_Y))
    pg.display.set_caption(constants.TITLE)
    states = {"SPLASH": gamestates.SplashScreen(),
              "GAMEPLAY": gamestates.Gameplay(),
              "GAMEOVER": gamestates.GameOver()}
    game = gamestates.Game(screen, states, "SPLASH")
    game.run()
    pg.quit()
    sys.exit()