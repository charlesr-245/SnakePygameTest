import pygame
import time
import colors
from LevelManager import *
from EventHandler import *

class Display(object):
    def __init__(this, _eventHandler):
        this.DISPLAYWIDTH = 800
        this.DISPLAYHEIGHT = 600
        this.eventHandler = _eventHandler
        this.screen = pygame.display.set_mode((this.DISPLAYWIDTH,this.DISPLAYHEIGHT))
        this.levels = LevelManager(this.screen, this.eventHandler)
    def Update(this): #Renders objects to the screen
        this.levels.Update()
        pygame.display.update()
        this.screen.fill(color.BLACK)