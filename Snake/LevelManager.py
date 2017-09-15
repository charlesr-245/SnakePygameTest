import pygame
from pygame.locals import *
import color
from Levels import *

class LevelManager(object):
    def __init__(this, _screen):
        this.screen = _screen
        this.currentLevel = 0
        this.levelList = Levels(this.screen)

    def Level0(this):
        this.levelList.MainMenu()
    def Update(this):
        if (this.currentLevel == 0):
            this.Level0()

