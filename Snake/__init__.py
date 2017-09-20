'''
Made by Charles Reverand
2017
'''

import pygame
import sys
from Display import *
from EventHandler import *

def __init__():
    global clock
    clock = pygame.time.Clock()
    clock.tick(60)
    global display
    global eventHandler
    eventHandler = EventHandler()
    display = Display(eventHandler) #Initializes display
    while True:
        Update()

def Update():
    clock.tick(60)
    eventHandler.Update() #Checks for user input
    display.Update()

__init__()
