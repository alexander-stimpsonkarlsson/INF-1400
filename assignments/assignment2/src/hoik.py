from parent import Basic
import pygame 
import math 
import param as P

screen = pygame.display.set_mode([P.SCREEN_WIDTH, P.SCREEN_WIDTH])

# Class for hoik

class Hoik(Basic):

    def __init__(self):

        self.size_x = 50
        self.size_y = 50

        super().__init__("reddit/upvote.png", self.size_x, self.size_y)

    def update(self, flock):

        edge = self.edge()
        separate = self.flock_separation(flock, P.HOIK_MAD)         

        self.speed = self.speed + (edge*2)                                      # Calculates hoik speed

        self.speed = self.speed.normalize() * P.MAX_SPEED                       # Limit for speed
        self.speed = self.speed - (separate*2)                                  # Hoiks will seek out boids

        self.pos += self.speed

        self.dir = math.degrees(math.atan2(self.speed[1], self.speed[0]))       # Gets direction of image
        self.image = pygame.transform.rotate(self.rotation_image, -self.dir)    # Rotates image in the right direction                                   
        self.rect = self.image.get_rect(center=(self.rect.center))              # Get new rect
        self.rect.center = self.pos                                             # New center

        screen.blit(self.image, self.pos)                                       # Blit image to screen
