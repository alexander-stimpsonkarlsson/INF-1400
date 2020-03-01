import pygame
import random

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

MAX_SPEED = 5
MIN_SPEED = -5

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_WIDTH])

# Class for boids

class Boid(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()

        self.image = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])  # Where the image is to be
        self.image = pygame.image.load("Pics/boid.png")             # Loads boid image
        self.image = pygame.transform.scale(self.image, (20, 20))   # Transform image to given scale

        self.pos = pygame.mouse.get_pos()                                            # Boids position is mouse position
        self.rect = self.image.get_rect(center=(4, 13))          # Are of image defined
        
        self.speed = (random.uniform(MIN_SPEED, MAX_SPEED),
                      random.uniform(MIN_SPEED, MAX_SPEED))         # Boid is spawned with a random speed
        self.direction = random.randint(0, 359)                     # Boid is spawned with a random direction

    #def align(self):    

    #def separation(self):

    #def cohesion(self):

    def movement(self):

        self.pos = self.speed
        
        if abs(SCREEN_WIDTH / 2 - self.pos[0]) > SCREEN_WIDTH / 2 - 20:
            #if self.pos[0] < SCREEN_WIDTH / 2:
            #    avoid = 1
            avoid = 1 if self.pos[0] < SCREEN_WIDTH / 2 else -1
            avoid *= MAX_SPEED * 0.2
            #else:
            #    avoid = -1
            #avoid *= MAX_SPEED * 0.2
            self.speed = self.speed[0] + avoid, self.speed[1]

        if abs(SCREEN_HEIGHT / 2 - self.pos[1]) > SCREEN_HEIGHT / 2 - 20:
            #if self.pos[1] < SCREEN_HEIGHT / 2:
            #    avoid = 1
            avoid = 1 if self.pos[1] < SCREEN_HEIGHT / 2 else -1
            avoid *= MAX_SPEED * 0.2
            #else: 
            #    avoid = -1
            #avoid *= MAX_SPEED * 0.8
            self.speed = self.speed[0], self.speed[1] + avoid
        
        self.speed = tuple(max(min(x, MAX_SPEED), -MAX_SPEED) for x in self.speed)

    def update(self):

        screen.blit(self.image, self.pos)    
        print(self.pos)     



# Class for voids

#class Void():
