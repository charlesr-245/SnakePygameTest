import pygame
from pygame.locals import *
import colors
from Levels import *

class LevelManager(object):
    def __init__(this, _screen, _eventHandler):
        this.screen = _screen
        this.currentLevel = 0
        this.eventHandler = _eventHandler
        this.levelList = Levels(this.screen,this.eventHandler)

    def Level0(this):
        this.levelList.MainMenu()
    def Update(this):
        if (this.currentLevel == 0):
            this.Level0()

