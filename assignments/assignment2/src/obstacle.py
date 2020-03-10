import pygame 
import math 
import param as P

screen = pygame.display.set_mode([P.SCREEN_WIDTH, P.SCREEN_WIDTH])

class Obstacle():

    def __init__(self):

        self.image = pygame.Surface([P.SCREEN_WIDTH, P.SCREEN_WIDTH])
        self.image = pygame.image.load("reddit/asteroid.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        self.pos = x-50, y-70

        self.rect = self.image.get_rect(center =(50, 50))

    def place(self):

        screen.blit(self.image, self.pos)