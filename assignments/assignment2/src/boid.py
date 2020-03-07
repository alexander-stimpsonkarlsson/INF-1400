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

        self.pos = V(x, y)                                    # Boids position is mouse position

        self.rect = self.image.get_rect(center =(10, 10))          # Are of image defined
        
        speed = (random.uniform(P.MIN_SPEED, P.MAX_SPEED),              # Random (x, y) 
                 random.uniform(P.MIN_SPEED, P.MAX_SPEED))
        self.speed = V(*speed)        

        self.dir = random.randint(P.MIN_DIR, P.MAX_DIR)
        self.angle = self.dir                                # Direction of bird when spawned 
 

    def flock_steer(self):                                   # Move towards center of the flock

        steer_twrd = V(0, 0)
        flock_size = 0                                              # Count of boids in flock
        average_dir = V(0, 0)
        pos = self.pos

        if len(self.box) != 0:                                         # Updates as long as list is not empty
            for boid in self.box:                                   
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])  
                if length <= P.GROUP_DISCTANCE: 
                    average_dir[0] += boid.pos[0]
                    average_dir[1] += boid.pos[1]
                    flock_size += 1

        if flock_size > 0:
            average_dir[0] /= flock_size
            average_dir[1] /= flock_size

        steer_twrd = ((average_dir[0] + pos[0]) * P.GROUP,           # Boids will try and steer towards the average 
                      (average_dir[1] + pos[1]) * P.GROUP)           # direction of all boids in the area

        return tuple(map(sum, zip(self.speed, steer_twrd)))

    def flock_separation(self):                             # Boids will try and avoid each other

        separation = V(0, 0)
        pos = self.pos

        if len(self.box) != 0:                                         # Updates as long as list is not empty
            for boid in self.box:
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])
                if length <= P.SEPARATION_DISTANCE:
                    separation[0] -= (boid.pos[0] - pos[0]) * P.SEPARATION
                    separation[1] -= (boid.pos[1] - pos[1]) * P.SEPARATION
                
        return tuple(map(sum, zip(self.speed, separation)))

    def flock_alignment(self):                               # Will try to allign with nearby boids

        alignment = V(0, 0)
        local_size = 0                                              # Count how many boids are in the boids area
        pos = self.pos

        if len(self.box) != 0:                                         # Updates as long as list is not empty, len is length
            for boid in self.box:
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])   # length of the vector from origin 
                if length <= P.ALIGN_DISTANCE:                                   # to point
                    alignment[0] += boid.speed[0]                       
                    alignment[1] += boid.speed[1]
                    local_size += 1
        
        if local_size > 0:
            alignment[0] /= local_size
            alignment[1] /= local_size
        
        alignment = ((alignment[0] - self.speed[0]) * P.ALIGN,        # Boids will try and match speed with  
                     (alignment[1] - self.speed[1]) * P.ALIGN)        # other boids
        
        return tuple(map(sum, zip(self.speed, alignment)))


    #def edge(self):                                                 # Boids will re-appear on the other side
                                                                    # when they go out of the screen
        #new_pos = list(self.pos)                                    # Since tuples are not changeable, i have to make 
                                                                    # a list from the tuple given, then change the variable
        #if new_pos[0] > P.SCREEN_WIDTH:                             # in the list and add that to the tuple
            #new_pos[0] = 0
            #self.pos = tuple(new_pos)
        #elif new_pos[0] < 0:
        #    new_pos[0] = P.SCREEN_WIDTH
        #    self.pos = tuple(new_pos)
        #if new_pos[1] > P.SCREEN_HEIGHT:
        #    new_pos[1] = 0
        #    self.pos = tuple(new_pos)
        #elif new_pos[1] < 0:
        #    new_pos[1] = P.SCREEN_HEIGHT
        #    self.pos = tuple(new_pos)
            
        #if new_pos[0] + P.WALL_DIST > P.SCREEN_WIDTH:                
        #    avoid = -1 
        #    avoid *= P.MAX_SPEED * P.AVOID_OBJECT
        #    new_speed[0] = avoid
        #    self.speed = tuple(new_speed)
        #elif new_pos[0] - P.WALL_DIST < 0:
        #    avoid = 1
        #    avoid *= P.MAX_SPEED * P.AVOID_OBJECT
        #    new_speed[0] = avoid
        #    self.speed = tuple(new_speed)
        #if new_pos[1] + P.WALL_DIST > P.SCREEN_HEIGHT:
        #    avoid = -1
        #    avoid *= P.MAX_SPEED * P.AVOID_OBJECT
        #    new_speed[1] = avoid
        #    self.speed = tuple(new_speed)
        #elif new_speed[1] - P.WALL_DIST < 0:
        #    avoid = 1
        #    avoid *= P.MAX_SPEED * P.AVOID_OBJECT
        #    new_speed[1] = avoid
        #    self.speed = tuple(new_speed)

    def update(self):

        #new_pos = list(self.pos)                                    # Since tuples are not changeable, i have to make 
                                                                    # a list from the tuple given, then change the variable
        #if new_pos[0] > P.SCREEN_WIDTH:                             # in the list and add that to the tuple
        #    new_pos[0] = 0
        #    self.pos = tuple(new_pos)
        #elif new_pos[0] < 0:
        #    new_pos[0] = P.SCREEN_WIDTH
        #    self.pos = tuple(new_pos)
        #if new_pos[1] > P.SCREEN_HEIGHT:
        #    new_pos[1] = 0
        #    self.pos = tuple(new_pos)
        #elif new_pos[1] < 0:
        #    new_pos[1] = P.SCREEN_HEIGHT
        #    self.pos = tuple(new_pos)
        #print(self.flock_steer(flock))
        #for boid in flock:
        #    if (boid.pos != self.pos):
                #self.speed = tuple(sum(x)for x in zip(self.flock_steer(flock),      # Calculates speed depending on 
                #self.flock_separation(flock), # the value of the three 
                #self.flock_alignment(flock))) # movement functions
        #if len(flock) != 0:
            #or boid in flock:
                #length = math.hypot(boid.pos[0] - self.pos[0], boid.pos[1] - self.pos[1])
                #if length <= P.ACTIVATION_DISTANCE:
        #if abs(P.SCREEN_WIDTH / 2 - self.pos[0]) > P.SCREEN_WIDTH / 2 - P.WALL_DIST:
        #    repel = 1 if self.pos[0] < P.SCREEN_WIDTH / 2 else -1
        #    repel *= P.MAX_SPEED * P.AVOID_OBJECT
        #    self.speed = self.speed[0] + repel, self.speed[1]
        #if abs(P.SCREEN_HEIGHT / 2 - self.pos[1]) > P.SCREEN_HEIGHT / 2 - P.WALL_DIST:
            #repel = 1 if self.pos[1] < P.SCREEN_HEIGHT / 2 else -1
            #repel *= P.MAX_SPEED * P.AVOID_OBJECT
            #self.speed = self.speed[0], self.speed[1] + repel

        self.speed = self.flock_steer()
        self.speed = self.flock_alignment()
        self.speed = self.flock_separation()

        self.speed = self.speed[0] + random.uniform(P.MIN_RANDOM, P.MAX_RANDOM), self.speed[1] + random.uniform(P.MIN_RANDOM, P.MAX_RANDOM)

        self.speed = tuple(max(min(x, P.MAX_SPEED), P.MIN_SPEED) for x in self.speed)
        print(self.speed)
    
        self.pos = tuple(sum(x) for x in zip(self.pos, self.speed))

        self.dir = math.degrees(math.atan2(self.speed[1], self.speed[0]))   # Gets direction of image
        self.image = pygame.transform.rotate(self.rotation_image, -self.dir)       # Rotates image in the right direction                                   
        self.rect = self.image.get_rect(center=(self.rect.center))
        self.rect.center = self.pos
  


