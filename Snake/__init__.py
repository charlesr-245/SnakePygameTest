import pygame
import sys
from Display import *
from EventHandler import *

def __init__():
    global display
    global eventHandler
    eventHandler = EventHandler()
    display = Display(eventHandler) #Initializes display
    while True:
        Update()

def Update():
    eventHandler.Update() #Checks for user input
    display.Update()

__init__()
