import pygame
import time
import math as M
import config as C 
from pygame         import Vector2 as V
from moveable_obj   import Moveable_Obj
from pygame.locals  import *
from blaster        import Blasters

# Parent class for players, inherits from moveable_obj

class Player(Moveable_Obj):

    """ Child class of moveable_obj. Adds arguments for how players are controlled and how they move on screen. 
        Takes in same arguments as moveable_obj but also takes in: 
        ctrl - what keys are used to control player object
        blaster - what type of appearance the blaster has
        sound - what sound the blaster makes when shot
    """

    def __init__(self, pics, x, y, pos, ctrl, blaster, sound):
        super().__init__(pics, x, y, pos)

        self.ctrl       = ctrl                      # Controls, keys are defined in the types of player class
        self.acc        = V(0, -C.PLAYER_ACC)       # Acceleration variable
        self.dir_speed  = 0                         # Used for calculatin how much object will rotate
        self.blast_list = []                        # List for blaster shot
        self.blaster    = blaster                   # Blaster picture 
        self.sound      = sound                     # Blaster sound
        self.health     = 5                         # Amount of health 
        self.fuel       = 1000                      # Amount of fuel
        self.re_fuel    = 0                         # Re fuel variable 

    def update(self):

        """ Updates speed and position of player object. Also adds blast object on player input and updates this. 
            Takes in arguments fps to set update frequence. Uses fuel attribute to determine wheter or not the player 
            can use its thrusters. If fuel is less that 0 it cannot thrust. Updates health if fuel reaches 0. 
        """
        
        self.edge()
    
        key = pygame.key.get_pressed()
    
        if key[self.ctrl[1]]:                                   # left, rotates
            self.dir_speed = -C.PLAYER_SPIN
            self.player_rotate() 
        if key[self.ctrl[2]]:                                   # right, rotate
            self.dir_speed = C.PLAYER_SPIN
            self.player_rotate() 
        
        if key[self.ctrl[0]] and self.fuel > 0:                 # Thrusts in the direction of the ship
            self.speed += self.acc
            self.fuel -= 2
            
        if self.fuel == 0:                                      # Stops thrusters when fuel is empty
            self.re_fuel += 1
            if self.re_fuel == 100:                             # Re fills after a certain amount of time
                self.health -= 1                                # Looses one health when it re fills
                self.fuel += 500
                self.re_fuel = 0

        if self.fuel > 1000:                                    # Fuel is capped at 1000
            self.fuel = 1000

        if len(self.blast_list) < 1:                            # Only allows one bullet to be shot at a time
            if key[self.ctrl[3]]:
                self.shoot()
        
        if self.speed.length() > C.PLAYER_MAX_THRUST:           # restricts max thrust
            self.speed.scale_to_length(C.PLAYER_MAX_THRUST)
        
        self.speed += C.GRAVITY                                 # Constant gravity pulling player down
        self.pos += self.speed                                  # updates position 
        self.rect.center = self.pos 

        for blast in self.blast_list:
            blast.update()
            C.SCREEN.blit(blast.image, blast.pos)
            if blast.rect.centerx > C.SCREEN_WIDTH or \
               blast.rect.centerx < 0 or \
               blast.rect.centery > C.SCREEN_HEIGHT or \
               blast.rect.centery < 0: 
                self.blast_list.remove(blast)

    def shoot(self):                                            # Creates a blast object and adds it to blast list
        
        """ Creates Blaster object and appends object to blast_list. Also plays sound when object is added to list 
        """

        self.blast = Blasters(V(self.rect.centerx-20, self.rect.centery-20), self.dir, (self.speed*C.BLASTER_SPEED), self.blaster) # Shoots
        self.blast_list.append(self.blast)
        self.sound.play()

    def player_rotate(self):                                    # Rotates left and right

        """ Rotates player depending on the player speed orientation. Updates player image so that, image is player is always 
            pointing in the direction for which it travels
        """
    
        self.acc.rotate_ip(self.dir_speed)
        self.dir += self.dir_speed

        if self.dir > 360:
            self.dir -= 360
        elif self.dir < 0:
            self.dir += 360 
        self.image = pygame.transform.rotate(self.rotation_img, -self.dir)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def edge(self):                                             # If player flies of the screen it re appears on the other side

        """ Checks if player position exceedes screen area. If so the player object is given a new position
            on screen to create the illusion of infinite screen area 
        """

        if self.rect.centerx < 0:
            self.pos[0] = C.SCREEN_WIDTH
        if self.rect.centerx > C.SCREEN_WIDTH:
            self.pos[0] = 0
        if self.rect.centery < 0:
            self.pos[1] = C.SCREEN_HEIGHT
        if self.rect.centery > C.SCREEN_HEIGHT:
            self.pos[1] = 0
    