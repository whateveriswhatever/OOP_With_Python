import pygame 
from pygame.locals import * 
import sys
import random

GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
TEAL = (0, 128, 128)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480 
FRAMES_PER_SECONDS = 30
N_PIXELS_PER_FRAMES = 3 

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # do any "per frame" actions
    
    # clear the window
    window.fill(GRAY)
    
    # draw all the window elements
    # draw a box
    # top
    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)
    # left
    pygame.draw.line(window, BLUE, (20, 20), (20,60), 4)
    # right
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)
    # bottom
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)
    
    # draw an filled circle and an empty circle
    # filled circle
    pygame.draw.circle(window, GREEN, (250, 50), 30, 0)
    # 2 pixels edge
    pygame.draw.circle(window, GREEN, (400, 50), 30, 2)
    
    # draw a filled rectangle and an empty rectangle
    # filled
    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0)
    # 1 pixel edge
    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1)
    
    # draw a filled ellipse and an empty ellipse
    # filled
    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40), 0)
    # 2 pixel edge
    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40), 2)
    
    # draw a six-sided polygon
    # pygame.draw.polygon(window, TEAL, ((240, 350), (350, (410, 410, (350, 470), (240, 470), (170, 410)))))
    pygame.draw.polygon(window, TEAL, ( (240, 350), (350, 350), (410, 410), (350, 470), (240, 470), (170, 410) ))
    # draw an arc
    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2, 5)
    
    # draw anti-aliased lines: a single line, then a list of points
    pygame.draw.aaline(window, RED, (500, 400), (540, 470), 1)
    pygame.draw.aalines(window, BLUE, True, ((580, 400), (587, 450), (595, 460), (600, 444)), 1)
    
    # update the window
    pygame.display.update()
    
    # slowing things down a bit
    clock.tick(FRAMES_PER_SECONDS)