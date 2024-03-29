# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
from pygame.locals import *
import sys
import random
from Ball import Ball
from Window import Window

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    BLACK = (0, 0, 0)
    WINDOW_WIDTH = 900
    WINDOW_HEIGTH = 800
    FRAMES_PER_SECONDS = 30
    N_PIXELS_PER_FRAMES = 3
    
    # # initialize the world
    # pygame.init()
    # window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
    
    # clock = pygame.time.Clock()
    # pygame.mixer.music.load("./sounds/background.mp3")
    # # -1 means the pygame will start playing the music right after
    # # user open the game and 0 to set the music playing intervally
    # pygame.mixer.music.play(-1, 0)
    
    # ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGTH)
    
    # while True:
    #     for event in pygame.event.get():
    #         # click the close button ? Quit game and end the program
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
         
    #      # do any 'per frames' actions
    #      # instruct the ball to update by itself       
    #     ball.update()
        
    #     window.fill(BLACK)
        
    #     # draw the window elements
    #     ball.draw()
        
    #     # update the window
    #     pygame.display.update()
        
    #     # slow things down a bit
    #     clock.tick(FRAMES_PER_SECONDS)
    
    # ballsOnTheBench = []
    
    # for i in range(4):
    #     ball = Ball(mainWindow, WINDOW_WIDTH, WINDOW_HEIGTH)
    #     ballsOnTheBench.append(ball)
    
    myWindow = Window(WINDOW_WIDTH, WINDOW_HEIGTH, BLACK, FRAMES_PER_SECONDS)
    myWindow.initialize()
    
    # customWindow = myWindow.retrieve_window_from_initializer()
    mainWindow = myWindow.retrieve_window_from_main()
    
    
    myBall = Ball(mainWindow, WINDOW_WIDTH, WINDOW_HEIGTH)
    # myWindow.initialize()
    
    ballsOnTheBench = []
    
    for i in range(20):
        ball = Ball(mainWindow, WINDOW_WIDTH, WINDOW_HEIGTH)
        ballsOnTheBench.append(ball)
    
    # myWindow.controller(myBall)
    myWindow.controllerForMultipleBalls(ballsOnTheBench)    
        
    
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
