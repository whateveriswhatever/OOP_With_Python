import pygame
from pygame.locals import * 
import sys
import random

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECONDS = 30
N_PIXELS_PER_FRAMES = 3

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

ballImage = pygame.image.load("./images/ball.png")

ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAMES
ySpeed = N_PIXELS_PER_FRAMES

while True:
    for event in pygame.event.get():
        # click the close button ? Quit game and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed # reverse the speed X if the ball is out of bound in the window on X diagnose
    
    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed # reverse the speed Y if the ball is out of bound in the window on Y diagnose
    
    # update the ball's rectangle using the speed in two directions
    ballRect.left += xSpeed
    ballRect.top += ySpeed
    
    
    # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    window.blit(ballImage, ballRect)
    
     # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECONDS)
     