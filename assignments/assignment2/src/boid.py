import pygame
import random
import math
from pygame import Vector2

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

MAX_SPEED = 5
MIN_SPEED = -5
MAX_DIR = 1
MIN_DIR = -1

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_WIDTH])

# Class for boids

class Boid(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])  # Where the image is to be
        self.image = pygame.image.load("Pics/rotate1.png")             # Loads boid image
        self.image = pygame.transform.scale(self.image, (25, 25))   # Transform image to given scale
        self.org_img = self.image

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        self.pos = Vector2(x, y)                                    # Boids position is mouse position
        self.rect = self.image.get_rect(center = self.pos)          # Are of image defined
        
        angle = (random.uniform(MIN_SPEED, MAX_SPEED),              # Random (x, y) 
                 random.uniform(MIN_SPEED, MAX_SPEED))
        self.speed = Vector2(*angle)        

        angle = (random.uniform(MIN_DIR, MAX_DIR),                  # Random (x, y)
                 random.uniform(MIN_DIR, MAX_DIR))
        self.acc = Vector2(*angle)

    #def align(self):    

    #def separation(self):

    #def cohesion(self):

    def avoid_edge(self):

        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH

        if self.pos.y > SCREEN_HEIGHT:
            self.pos.y = 0
        elif self.pos.y < 0:
            self.pos.y = SCREEN_HEIGHT

    def movement(self):

        self.pos += self.speed
        self.speed += self.acc

        if self.speed[0] > MAX_SPEED and self.speed[1] > MAX_SPEED:
            self.speed[0] = self.speed[0] / (self.speed[0] * MAX_SPEED)
            self.speed[1] = self.speed[1] / (self.speed[1] * MAX_SPEED)
        self.acc = Vector2()

        self.dir = math.degrees(math.atan2(self.speed[1], self.speed[0]))   # Gets direction of iamge
        self.image = pygame.transform.rotate(self.org_img, -self.dir)       # Rotates image in the right direction                                     


    def draw(self, screen):

        screen.blit(self.image, self.pos)    

# Class for voids

#class Void():
