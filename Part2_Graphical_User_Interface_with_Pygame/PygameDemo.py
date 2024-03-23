import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECONDS = 30

BALL_WIDTH = 100
BALL_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH
MAX_HEIGHT = WINDOW_HEIGHT - BALL_HEIGHT

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

# 4 - Loads assets: image(s), sound(s), etc.
ballImage = pygame.image.load("./images/ball.png")

# 5 - Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)

ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH, BALL_HEIGHT)

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # if user click the QUIT button, then the program will be refrained immediately
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # see if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos
            # could do this, if we needed it
            # check if the click was in the rect of the ball
            # if so, choose a random new location
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH, BALL_HEIGHT)
            
    
    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BLACK)
    
    # 10 - Draw all window elements
        # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (100, 200))
        
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slows things down a bit
    clock.tick(FRAMES_PER_SECONDS)
