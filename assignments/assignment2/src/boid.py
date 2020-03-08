import pygame
import random
import math
from pygame import Vector2 as V
import param as P

screen = pygame.display.set_mode([P.SCREEN_WIDTH, P.SCREEN_WIDTH])

# Class for boids

class Boid(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.box)

        self.image = pygame.Surface([P.SCREEN_WIDTH, P.SCREEN_HEIGHT])  # Where the image is to be
        self.image = pygame.image.load("Pics/rotate1.png")          # Loads boid image
        self.image = pygame.transform.scale(self.image, (25, 25))   # Transform image to given scale
        self.rotation_image = self.image                            # Used for rotating image 

        x = pygame.mouse.get_pos()[0]                               # x posistion of mouse
        y = pygame.mouse.get_pos()[1]                               # y posiition of mouse

        self.pos = x, y                                    # Boids position is mouse position

        self.rect = self.image.get_rect(center =(5, 10))          # Are of image defined
        
        speed = (random.uniform(P.MIN_SPEED, P.MAX_SPEED),              # Random (x, y) 
                 random.uniform(P.MIN_SPEED, P.MAX_SPEED))
        self.speed = V(*speed)   
        self.dir = self.speed     

    def flock_steer(self):                                   # Move towards center of the flock

        steer_twrd = V(0, 0)
        flock_size = 0                                              # Count of boids in flock
        average_dir = V(0, 0)
        pos = self.pos

        if len(self.box) != 1:                                         # Updates as long as list is not empty
            for boid in self.box:                                   
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])  
                if boid.pos != self.pos:
                    if length < P.GROUP_DISCTANCE: 
                        average_dir += boid.pos
                        flock_size += 1

        if flock_size > 0:
            average_dir /= flock_size

        steer_twrd = (average_dir + pos) / P.GROUP

        return steer_twrd

    def flock_separation(self):                             # Boids will try and avoid each other

        separation = V(0, 0)
        pos = self.pos

        if len(self.box) != 1:                                         # Updates as long as list is not empty
            for boid in self.box:
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])  
                if boid.pos != self.pos:
                    if length < P.SEPARATION_DISTANCE:
                        separation -= (boid.pos - pos) * P.SEPARATION
                
        return separation
         
    def flock_alignment(self):                               # Will try to allign with nearby boids

        alignment = V(0, 0)
        local_size = 0                                              # Count how many boids are in the boids area
        pos = self.pos

        if len(self.box) != 1:                                         # Updates as long as list is not empty, len is length
            for boid in self.box:
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])  
                if boid.pos != self.pos:
                    if length <= P.ALIGN_DISTANCE:                                   # to point
                        alignment += boid.speed
                        local_size += 1
        
        if local_size > 0:
            alignment /= local_size

        alignment = (alignment - self.speed) * P.ALIGN
        
        return alignment

    #def place(self):

        #place_pref = V(200, 100)

        #return (place_pref - self.pos) / 100

    def update(self):

        if self.pos[0] < 0 + P.WALL_DIST: 
            self.speed[0] = 10
        if self.pos[0] > P.SCREEN_WIDTH - P.WALL_DIST:
            self.speed[0] = -10
        if self.pos[1] < 0 + P.WALL_DIST: 
            self.speed[1] = 10
        if self.pos[1] > P.SCREEN_HEIGHT - P.WALL_DIST:
            self.speed[1] = -10

        steer = self.flock_steer()
        align = self.flock_alignment()
        separate = self.flock_separation()

        self.speed = self.speed + steer + align + separate                  # Calculates speed depening on the three flock variables

        
        #if abs(P.SCREEN_WIDTH / 2 - self.pos[0]) > P.SCREEN_WIDTH / 2 - P.WALL_DIST:
        #    avoid = 1 if self.pos[0] < P.SCREEN_WIDTH / 2 else -1
        #    avoid = avoid * P.MAX_SPEED * P.AVOID_OBJECT
        #    self.speed = self.speed[0] + avoid, self.speed[1]
        #if abs(P.SCREEN_HEIGHT / 2 - self.pos[1]) > P.SCREEN_HEIGHT / 2 - P.WALL_DIST:
            #avoid = 1 if self.pos[1] < P.SCREEN_HEIGHT / 2 else -1
            #avoid = avoid * P.MAX_SPEED * P.AVOID_OBJECT
            #self.speed = self.speed[0], self.speed[1] + avoid

        if self.speed.length() > P.MAX_SPEED:                               # Limit for speed
            self.speed = (self.speed / self.speed.length()) * P.MAX_SPEED

        self.pos += self.speed
        #self.pos += self.place()

        self.dir = math.degrees(math.atan2(self.speed[1], self.speed[0]))   # Gets direction of image
        self.image = pygame.transform.rotate(self.rotation_image, -self.dir)       # Rotates image in the right direction                                   
        self.rect = self.image.get_rect(center=(self.rect.center))
        self.rect.center = self.pos
  


