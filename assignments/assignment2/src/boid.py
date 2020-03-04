import pygame
import random
import math
from pygame import Vector2
import param as par

screen = pygame.display.set_mode([par.SCREEN_WIDTH, par.SCREEN_WIDTH])

# Class for boids

class Boid():

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([par.SCREEN_WIDTH, par.SCREEN_HEIGHT])  # Where the image is to be
        self.image = pygame.image.load("Pics/rotate1.png")          # Loads boid image
        self.image = pygame.transform.scale(self.image, (25, 25))   # Transform image to given scale
        self.org_img = self.image                                   # Used for rotating image 

        x = pygame.mouse.get_pos()[0]                               # x posistion of mouse
        y = pygame.mouse.get_pos()[1]                               # y posiition of mouse
        self.fov = 180                                              # Field of view                                            

        self.pos = Vector2(x, y)                                    # Boids position is mouse position

        self.rect = self.image.get_rect(center = self.pos)          # Are of image defined
        
        speed = (random.uniform(par.MIN_SPEED, par.MAX_SPEED),              # Random (x, y) 
                 random.uniform(par.MIN_SPEED, par.MAX_SPEED))
        self.speed = Vector2(*speed)        

        angle = (random.uniform(par.MIN_DIR, par.MAX_DIR),                  # Random (x, y)
                 random.uniform(par.MIN_DIR, par.MAX_DIR))
        self.dir = Vector2(*angle)                                  # Direction of bird when spawned 

    def flock_steer(self, flock):                                   # Move towards center of the flock

        steer_twrd = Vector2(0, 0)
        flock_size = 0                                              # Count of boids in flock
        average_dir = Vector2(0, 0)
        pos = self.pos

        for boid in flock:     
            if (boid.pos != pos):                                
                distance = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])    
                if distance <= par.GROUP_DISCTANCE:
                    average_dir[0] += boid.pos[0]
                    average_dir[1] += boid.pos[1]
                    flock_size += 1

        if flock_size > 0:
            average_dir[0] /= flock_size
            average_dir[1] /= flock_size

        steer_twrd = ((average_dir[0] - pos[0]) * par.GROUP,           # Boids will try and steer towards the average 
                 (average_dir[1] - pos[1]) * par.GROUP)                # direction of all boids in the area

        return steer_twrd

    def flock_separation(self, flock):                             # Boids will try and avoid each other

        separation = Vector2(0, 0)
        pos = self.pos

        for boid in flock:
            if (boid.pos != pos):
                distance = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])
                if distance <= par.SEPARATION_DISTANCE:
                    separation[0] -= (boid.pos[0] - pos[0]) * par.SEPARATION
                    separation[1] -= (boid.pos[1] - pos[1]) * par.SEPARATION
            
        return separation

    def flock_alignment(self, flock):                               # Will try to allign with nearby boids

        alignment = Vector2(0, 0)
        local_size = 0                                              # Count how many boids are in the boids area
        pos = self.pos

        for boid in flock:
            if (boid.pos != pos):
                distance = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])   # length of the vector from origin 
                if distance <= par.ALIGN_DISTANCE:                                  # to point
                    alignment[0] += boid.speed[0]                       
                    alignment[1] += boid.speed[1]
                    local_size += 1
        
        if local_size > 0:
            alignment[0] /= local_size
            alignment[1] /= local_size
        
        alignment = ((alignment[0] - self.speed[0]) * par.ALIGN,        # Boids will try and match speed with  
                     (alignment[1] - self.speed[1]) * par.ALIGN)        # other boids
        
        return alignment


    def edge(self):                                                 # Boids will re-appear on the other side
                                                                    # when they go out of the screen
        pos = self.pos
        if pos[0] > par.SCREEN_WIDTH:
            pos[0] = 0
        elif pos[0] < 0:
            pos[0] = par.SCREEN_WIDTH

        if pos[1] > par.SCREEN_HEIGHT:
            pos[1] = 0
        elif pos[1] < 0:
            pos[1] = par.SCREEN_HEIGHT

    def movement(self, flock):

        self.speed = tuple(sum(x)for x in zip(self.flock_steer(flock),      # Calculates speed depending on 
                                              self.flock_separation(flock), # the value of the three 
                                              self.flock_alignment(flock))) # movement functions

        self.pos += self.speed

        if self.speed[0] > par.MAX_SPEED and self.speed[1] > par.MAX_SPEED: # Restricts the speed a boid can have
            self.speed = self.speed.normalize_ip()
            self.pos[0] = self.speed[0] / (self.speed[0] * par.MAX_SPEED)
            self.pos[1] = self.speed[1] / (self.speed[1] * par.MAX_SPEED)

        self.dir = math.degrees(math.atan2(self.speed[0], self.speed[1]))   # Gets direction of iamge
        self.image = pygame.transform.rotate(self.org_img, -self.dir)       # Rotates image in the right direction                                     

    def draw(self, screen):

        screen.blit(self.image, self.pos)    


