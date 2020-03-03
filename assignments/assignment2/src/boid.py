import pygame
import random
import math
from pygame import Vector2

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

MAX_SPEED = 5
MIN_SPEED = -5
MAX_DIR = 360
MIN_DIR = 0
GROUP_DISCTANCE = 100
SEPARATION_DISTANCE = 20
ALIGN_DISTANCE = 60
GROUP = 0.0001

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_WIDTH])

# Class for boids

class Boid():

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])  # Where the image is to be
        self.image = pygame.image.load("Pics/rotate1.png")          # Loads boid image
        self.image = pygame.transform.scale(self.image, (25, 25))   # Transform image to given scale
        self.org_img = self.image                                   # Used for rotating image 

        x = pygame.mouse.get_pos()[0]                               # x posistion of mouse
        y = pygame.mouse.get_pos()[1]                               # y posiition of mouse
        self.fov = 180                                              # Field of view                                            

        self.pos = Vector2(x, y)                                    # Boids position is mouse position
        self.rect = self.image.get_rect(center = self.pos)          # Are of image defined
        
        angle = (random.uniform(MIN_SPEED, MAX_SPEED),              # Random (x, y) 
                 random.uniform(MIN_SPEED, MAX_SPEED))
        self.speed = Vector2(*angle)        

        angle = (random.uniform(MIN_DIR, MAX_DIR),                  # Random (x, y)
                 random.uniform(MIN_DIR, MAX_DIR))
        self.dir = Vector2(*angle)                                  # Acceleration 

    def flock_steer(self, boids):                                   # Move towards center of the flock

        steer_twrd = Vector2(0, 0)
        flock_size = 0                                              # Count of boids in flock
        average_dir = Vector2(0, 0)
        pos = self.pos

        for boid in boids:     
            distance = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])   
            print(pos[0])                                  
            if distance <= GROUP_DISCTANCE:
                average_dir[0] += boid.pos[0]
                average_dir[1] += boid.pos[1]
                flock_size += 1
            #if (boid.pos[1] - self.pos[1]) > self.fov:
            #    average_dir[1] += boid.speed[1]
            #    flock_size += 1

        if flock_size > 0:
            average_dir[0] /= flock_size
            average_dir[1] /= flock_size

        steer_twrd = ((average_dir[0] - pos[0]) * GROUP, 
                 (average_dir[1] - pos[1]) * GROUP)
            #average_dir = Vector2(*average_dir)

            #average_dir[0] = (average_dir[0] / (average_dir[0] * MAX_SPEED))
            #average_dir[1] = (average_dir[1] / (average_dir[1] * MAX_SPEED))

            #steer_twrd[0] = average_dir[0] - self.speed[0]
            #steer_twrd[1] = average_dir[1] - self.speed[1]

        return steer_twrd

    def flock_separation(self, boids):

        separation = Vector2(0, 0)
        pos = self.pos

        for boid in boids:
            distance = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])
            if distance <= SEPARATION_DISTANCE:
                separation[0] -= (boid.pos[0] - pos[0]) * 0.02
                separation[1] -= (boid.pos[1] - pos[1]) * 0.02
        
        return separation

    def alignment(self, boids):                                        # Will try to allign with nearby boids

        alignment = Vector2(0, 0)
        local_size = 0                                                 # Count how many boids are in the boids area
        pos = self.pos

        for boid in boids:
            distance = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])
            if distance <= ALIGN_DISTANCE:
                alignment[0] += boid.speed[0]
                alignment[1] += boid.speed[1]
                local_size += 1
        
        if local_size > 0:
            alignment[0] /= local_size
            alignment[1] /= local_size
        
        alignment = ((alignment[0] - self.speed[0]) * 0.125, 
                     (alignment[1] - self.speed[1]) * 0.125)
        
        return alignment


    def edge(self):

        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH

        if self.pos.y > SCREEN_HEIGHT:
            self.pos.y = 0
        elif self.pos.y < 0:
            self.pos.y = SCREEN_HEIGHT

    def movement(self, boids):

        #self.pos += self.speed
        #self.speed += self.acc
        self.speed = tuple(sum(x) for x in zip(self.flock_steer(boids), self.flock_separation(boids), self.alignment(boids)))

        if self.speed[0] > MAX_SPEED and self.speed[1] > MAX_SPEED:
            self.speed[0] = self.speed[0] / (self.speed[0] * MAX_SPEED)
            self.speed[1] = self.speed[1] / (self.speed[1] * MAX_SPEED)
        #self.acc = Vector2(0, 0)

        self.dir = math.degrees(math.atan2(self.speed[1], self.speed[0]))   # Gets direction of iamge
        self.image = pygame.transform.rotate(self.org_img, -self.dir)       # Rotates image in the right direction                                     

    #def behaviour(self, boids):
        
        #self.speed = tuple(sum(x) for x in zip(self.))
        #align = self.flock_steer(boids)


    def draw(self, screen):

        screen.blit(self.image, self.pos)    

# Class for voids

#class Void():
