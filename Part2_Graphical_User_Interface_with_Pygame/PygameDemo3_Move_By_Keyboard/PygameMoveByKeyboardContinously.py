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

TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH = 120
TARGET_HEIGHT = 120
N_PIXELS_TO_MOVE = 69


# 3 - Initialize the game
pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

# 4 - Loads assets: image(s), sound(s), etc.
ballImage = pygame.image.load("images/ball.png")
targetImage = pygame.image.load("images/target.jpg")

# 5 - Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH, TARGET_HEIGHT)


# ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH, BALL_HEIGHT)

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # if user click the QUIT button, then the program will be refrained immediately
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # # check for user pressing keys
        # elif event.type == pygame.KEYDOWN:
            
        #     if event.key == pygame.K_LEFT:
        #         ballX -= N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_RIGHT:
        #         ballX += N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_UP:
        #         ballY -= N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_DOWN:
        #         ballY += N_PIXELS_TO_MOVE
            
    
    # 8 - Do any "per frame" actions
    # check for user pressing keys
    if keyPressedTuple[pygame.K_LEFT]:
        ballX -= N_PIXELS_TO_MOVE
    elif keyPressedTuple[pygame.K_RIGHT]:
        ballX += N_PIXELS_TO_MOVE
    elif keyPressedTuple[pygame.K_UP]:
        ballY -= N_PIXELS_TO_MOVE
    elif keyPressedTuple[pygame.K_DOWN]:
        ballY += N_PIXELS_TO_MOVE 
    elif keyPressedTuple[pygame.K_q]:
        print("Press 'q' to cancel the program !!!")
        pygame.quit()
        sys.exit()
    
    # check if the ball is colliding with the target
    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH, BALL_HEIGHT)
    keyPressedTuple = pygame.key.get_pressed()
    
    
    if ballRect.colliderect(targetRect):
        print("Ball is touching the target")
    
    # 9 - Clear the window
    window.fill(BLACK)
    
    # 10 - Draw all window elements
        # draw ball at position 100 across (x) and 200 down (y)
    # window.blit(ballImage, (100, 200))
    window.blit(ballImage, (ballX, ballY)) # draw the ball)
    window.blit(targetImage, (TARGET_X, TARGET_Y)) # draw the target
    
        
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slows things down a bit
    clock.tick(FRAMES_PER_SECONDS) # make pygame waiting
