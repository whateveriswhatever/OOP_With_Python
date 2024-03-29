import pygame
from pygame.locals import *
import sys
import random

class Window:
    def __init__(self, width, height, backgroundColor, framesPerSecs):
        self._width = width
        self._height = height
        self._backgroundColor = backgroundColor
        self._framesPerSecs = framesPerSecs
        self._window = pygame.display.set_mode((self._width, self._height))
    
    def initialize(self):
        pygame.init()
        # window = pygame.display.set_mode((self._width, self._height))
        
        # clock = pygame.time.Clock()
        # # pygame.mixer.music.load("./sounds/background.mp3")
        
        # # -1 means the pygame will start playing the music right after
        # # user open the game and 0 to set the music playing intervally
        # # pygame.mixer.music.play(-1, 0)
        
        # return {
        #     "window": window,
        #     "clock": clock
        # }
    
    # def retrieve_window_from_initializer(self):
    #     res = self.initialize()
    #     window = res["window"]
    #     return window

    def retrieve_window_from_main(self):
        return self._window
    
    def retrieve_clock(self):
        clock = pygame.time.Clock()
        return clock
    
    def controller(self, ball):
        while True:
            for event in pygame.event.get():
            # click the close button ? Quit game and end the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
         
            # do any 'per frames' actions
            # instruct the ball to update by itself       
            ball.update()
            
            # windowAndClock = self.initialize()
            
            # window = windowAndClock["window"]
            # clock = windowAndClock["clock"]
            
            window = self.retrieve_window_from_main()
            clock = self.retrieve_clock()            
            window.fill(self._backgroundColor)
            
            # draw the window elements
            ball.draw()
            
            # update the window
            pygame.display.update()
        
            # slow things down a bit
            clock.tick(self._framesPerSecs)
    
    def controllerForMultipleBalls(self, ballStorage):
        while True:
            for event in pygame.event.get():
            # click the close button ? Quit game and end the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
         
            # do any 'per frames' actions
            # instruct the ball to update by itself       
            for ball in ballStorage:
                ball.update()
            
            # windowAndClock = self.initialize()
            
            # window = windowAndClock["window"]
            # clock = windowAndClock["clock"]
            
            window = self.retrieve_window_from_main()
            clock = self.retrieve_clock()            
            window.fill(self._backgroundColor)
            
            # draw the window elements
            for ball in ballStorage:
                ball.draw()
            
            # update the window
            pygame.display.update()
        
            # slow things down a bit
            clock.tick(self._framesPerSecs)
        
    def controllerForCustomButtons(self, button):
        while True:
            # check for event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # pass the event to the button, see if it has been clicked
            if button.handleEvent(event):
                print("Clicked !")
        
            window = self.retrieve_window_from_main()
            window.fill((255, 255, 255)) # Gray color
        
            button.draw() # draw the button
            
            pygame.display.update() # update the window
            
            # slow thing down for a bit
            clock = self.retrieve_clock()
            clock.tick(self._framesPerSecs)
            
        
        
        
        