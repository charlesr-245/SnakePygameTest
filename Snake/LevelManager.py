import pygame
from pygame.locals import *
import colors
from Levels import *
import random

class LevelManager(object):
    def __init__(this, _screen, _eventHandler):
        this.screen = _screen
        this.currentLevel = 0
        this.eventHandler = _eventHandler
        this.levelList = Levels(this.screen,this.eventHandler)
        this.Level1 = Level1(this.screen, this.eventHandler, False)
        this.ID = random.random()
    def Level0(this):
        this.levelList.MainMenu(this)
    def Level1(this):
        this.levelList.EnableLevel1()
        
    def Update(this):
        #print(this.currentLevel)
        #print(this.ID)
        if (this.currentLevel == 0):
            this.Level0()
        elif (this.currentLevel == 1):
            this.Level1.Update()

