import pygame
from pygame.locals import *
import sys
import random

class Ball:
    def __init__(self, window, windowWidth, windowHeight):
        self._window = window
        self._img = pygame.image.load("./images/ball.png")
        self._sound = pygame.mixer.Sound("./sounds/boing.wav")
        self._windowWidth = windowWidth
        self._windowHeight = windowHeight
        
        # a rectangle is made up of [x, y, width, height]
        ballRect = self._img.get_rect()
        self._width = ballRect.width
        self._height = ballRect.height
        self._maxWidth = self._windowWidth - self._width
        self._maxHeight = self._windowHeight - self._height
        
        # pick a random starting position
        self._x = random.randrange(0, self._maxWidth)
        self._y = random.randrange(0, self._maxHeight)
        
        self._speedList = [_ for _ in range(-4, 5, 1)]
        self._xSpeed = random.choice(self._speedList)
        self._ySpeed = random.choice(self._speedList)
    
    def update(self):
        # check if the ball hits the walls, the ball will be bounce
        # or change directions
        if (self._x < 0) or (self._x >= self._maxWidth):
            self._xSpeed = -self._xSpeed
        
        if (self._y < 0) or (self._y >= self._maxHeight):
            self._ySpeed = -self._ySpeed
        
        # update the current position of the ball in X and Y directions
        self._x += self._xSpeed
        self._y += self._ySpeed
    
    def draw(self):
        self._window.blit(self._img, (self._x, self._y))
        
        