from SimpleButton import SimpleButton
from ..Window import Window
import pygame
from pygame.locals import * 
import random
import sys

# creating an folder path pointing to the Window class
# sys.path.append("../Window.py")
# from target_directory import Window

BLACK = (0, 0, 0)
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
FRAMES_PER_SECONDS = 30
N_PIXELS_PER_FRAMES = 3

myWindow = Window(WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, FRAMES_PER_SECONDS)
myWindow.initialize()

customWindow = myWindow.retrieve_window_from_main()

myButton = SimpleButton(customWindow, (150, 30), "../images/buttonUp.png", "../images/buttonDown.png")

myWindow.controllerForCustomButtons(myButton)
