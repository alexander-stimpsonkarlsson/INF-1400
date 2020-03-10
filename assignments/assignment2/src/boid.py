import pygame
import random
import math
from pygame import Vector2 as V
import param as P
from parent import Common

screen = pygame.display.set_mode([P.SCREEN_WIDTH, P.SCREEN_WIDTH])

# Class for boids

class Boid(Common):

    def __init__(self):
        super().__init__("reddit/rotate1.png", 25, 25)

    def flock_steer(self, flock):                                   # Move towards center of the flock

        steer_twrd = V(0, 0)                                             
        average_dir = V(0, 0)
        pos = self.pos
        count = 0

        for boid in flock:                         
            if boid.pos != self.pos:          
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])  
                if length < P.GROUP_DISCTANCE: 
                    average_dir += boid.pos
                    count += 1

        if count > 0:
            average_dir /= count
            average_dir = V(*average_dir)

        steer_twrd = (average_dir - pos) * P.GROUP

        return steer_twrd
         
    def flock_alignment(self, flock):                               # Will try to allign with nearby boids

        alignment = V(0, 0)                             
        pos = self.pos
        count = 0
                       
        for boid in flock:
            if boid.pos != self.pos:
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])  
                if length <= P.ALIGN_DISTANCE:                                   
                    alignment += boid.speed
                    count += 1
        
        if count > 0:
            alignment /= count
            alignment = V(*alignment)

        alignment = (alignment + self.speed) * P.ALIGN
        
        return alignment
                 
    def update(self, flock, obstacles):
        
        steer = self.flock_steer(flock)
        align = self.flock_alignment(flock)
        separate = self.flock_separation(flock, P.SEPARATION_DISTANCE)
        edge = self.edge()  
        avoid = self.object_avoid(obstacles)                 

        self.speed = self.speed + (steer*2) + align + separate + (edge*2)   # Calculates speed depening on the three flock variables
        self.speed = self.speed + (avoid*4)                                 # Avoid objects asteroids
        self.speed = self.speed.normalize() * P.MAX_SPEED                   # Limit for speed
        self.pos += self.speed                                              # Moves boid

        self.dir = math.degrees(math.atan2(self.speed[1], self.speed[0]))    # Gets direction of image
        self.image = pygame.transform.rotate(self.rotation_image, -self.dir) # Rotates image in the right direction                                   
        self.rect = self.image.get_rect(center=(self.rect.center))           # Gets the new center of image
        self.rect.center = self.pos                                          # New center

        screen.blit(self.image, self.pos)                                    # Prints boid


