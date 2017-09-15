import pygame
import time
import color
from LevelManager import *

class Display(object):
    def __init__(this):
        this.DISPLAYWIDTH = 800
        this.DISPLAYHEIGHT = 600
        this.screen = pygame.display.set_mode((this.DISPLAYWIDTH,this.DISPLAYHEIGHT))
        this.levels = LevelManager(this.screen)
    def Update(this): #Renders objects to the screen
        this.levels.Update()
        pygame.display.update()
        this.screen.fill(color.BLACK)