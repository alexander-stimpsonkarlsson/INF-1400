import pygame 
import math 
import parameter as P

screen = pygame.display.set_mode([P.SCREEN_WIDTH, P.SCREEN_WIDTH])

# Class for obstacles

class Obstacle():

    def __init__(self):

        self.image = pygame.Surface([P.SCREEN_WIDTH, P.SCREEN_WIDTH])
        self.image = pygame.image.load("pics/asteroid.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rotation_image = self.image 

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        self.angle = 0
        self.pos = x, y
        
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):                                                           # Rotates and prints asteroid obstacles
        
        self.rotate()
        screen.blit(self.image, self.pos)
    
    def rotate(self):

        self.new_angle()
        self.image = pygame.transform.rotate(self.rotation_image, self.angle)
        self.rect = self.image.get_rect(center =(self.rect.center))
        

    def new_angle(self):
        
        self.angle += 1

        