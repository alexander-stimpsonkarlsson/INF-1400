import pygame
import random
import param

screen_width = 1400
screen_height = 1000
screen_size = [screen_width, screen_height]                     
screen = pygame.display.set_mode(screen_size)
white_color = (255, 255, 255)

# Class for boids

class Boid(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()

        self.image = pygame.Surface([screen_width, screen_height])
        self.image = pygame.image.load("Pics/boid.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
    
    def update(self):

        screen.blit(self.image, pygame.mouse.get_pos()) 
        self.x, self.y = pygame.mouse.get_pos()
        print(self.x, self.y)



# Class for voids

#class Void():
