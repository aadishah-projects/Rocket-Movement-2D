import pygame
import sys

class Rocket:
    def __init__(self,screen):
        self.screen = screen
        #load
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # co-ordinates
        self.rect.x = 600
        self.rect.y = 400
        print (self.screen_rect.center)
        self.moving_right = False
        self.moving_left  = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_right and self.rect.x<1150:
            self.rect.x += 1.5
        if self.moving_left and self.rect.x>0:
            self.rect.x -= 1.5
        if self.moving_up and self.rect.y>0:
            self.rect.y -= 1.5
        if self.moving_down and self.rect.y<700:
            self.rect.y += 1.5
    def blitme(self):
        self.screen.blit(self.image,self.rect)