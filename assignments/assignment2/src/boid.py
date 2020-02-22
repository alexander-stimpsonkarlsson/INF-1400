import pygame
import random
from param import param1
screen_width = 1400
screen_height = 1000
# Class for boids

class Boid(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super().__init__()

        self.x = pygame.mouse.get_pos(x)
        self.y = pygame.mouse.get_pos(y)
        self.image = pygame.Surface([screen_width, screen_height])
        self.image.load("Pics/void.png")
        self.rect = self.image.get_rect()
    
    def update(self):

        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, boid.rect) 
