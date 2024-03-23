# 1 - Import packages
import pygame
from pygame.locals import *
import sys

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECONDS = 30

# 3 - Initialize the worl
pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

# 4 - Loads assets: image(s), sound(s), etc.

# 5 - Initialize variables

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # if user click the QUIT button, then the program will be refrained immediately
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BLACK)
    
    # 10 - Draw all window elements
    
    # 11 - Update the window
    
    # 12 - Slows things down a bit
    clock.tick(FRAMES_PER_SECONDS)
