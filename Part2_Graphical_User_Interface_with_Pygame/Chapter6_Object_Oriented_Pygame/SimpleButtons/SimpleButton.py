import pygame
from pygame.locals import * 

class SimpleButton:
    # Used to track the state of the button
    STATE_IDLE = "idle" # button is up, mouse not over button
    STATE_ARMED = "armed" # button is down, mouse over button
    STATE_DISARMED = "disarmed"
         
    def __init__(self, window, loc, up, down):
        self._window = window
        self._loc = loc
        self._surfaceUp = pygame.image.load(up)
        self._surfaceDown = pygame.image.load(down)
    
        # Get the rectangle of the button (used to see if the mouse is over the button)
        self._rect = self._surfaceUp.get_rect()
        self._rect[0] = loc[0]
        self._rect[1] = loc[1]
        
        self._state = SimpleButton.STATE_IDLE
    
    def handleEvent(self, eventObj):
        # This button will return True if user clicks on the button
        # Normally returns False
        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # The button only cares about mouse-related events
            return False
        
        eventPointInButtonRect = self._rect.collidepoint(eventObj.pos)
        
        if self._state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self._state = SimpleButton.STATE_ARMED
        elif self._state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self._state = SimpleButton.STATE_IDLE
                return True # clicked

            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self._state = SimpleButton.STATE_DISARMED
        elif self._state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self._state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self._state = SimpleButton.STATE_IDLE
        
        return False
    
    def draw(self):
        # Draw the button's current appearance to the window
        if self._state == SimpleButton.STATE_ARMED:
            self._window.blit(self._surfaceDown, self._loc)
        else: # IDLE or DISARMED
            self._window.blit(self._surfaceUp, self._loc)
            
        
        
        