import pygame
import sys
from Display import *
from EventHandler import *

def __init__():
    global display
    display = Display() #Initializes display
    while True:
        Update()

def Update():
    EventHandler.Update() #Checks for user input
    display.Update()

__init__()
