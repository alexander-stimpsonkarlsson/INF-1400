import pygame
import time
import math as M
import config as C 
from pygame import Vector2 as V
from moveable_obj import Moveable_Obj
from pygame.locals import *
from blaster import Blasters

# Parent class for players, inherits from moveable_obj

class Player(Moveable_Obj):

    def __init__(self, pics, x, y, pos, ctrl, blaster):
        super().__init__(pics, x, y, pos)

        self.ctrl = ctrl
        self.acc = V(0, -C.PLAYER_ACC)
        self.dir_speed = 0
        self.blast_list = []
        self.blaster = blaster

    def update(self, fps):
        
        self.edge()
        key = pygame.key.get_pressed()
    
        if key[self.ctrl[1]]:                           # left, rotates
            self.dir_speed = -C.PLAYER_SPIN
            self.player_rotate() 
        if key[self.ctrl[2]]:                           # right, rotate
            self.dir_speed = C.PLAYER_SPIN
            self.player_rotate() 
        
        if key[self.ctrl[0]]:                           # thrust upwards
            self.speed += self.acc
        
        if len(self.blast_list) < 1: 
            if key[self.ctrl[3]]:
                self.shoot()
        
        if self.speed.length() > C.PLAYER_MAX_THRUST:          # restricts max thrust
            self.speed.scale_to_length(C.PLAYER_MAX_THRUST)
        
        self.speed += C.GRAVITY
        self.pos += self.speed                          # updates position 
        self.rect.center = self.pos 

        for blast in self.blast_list:
            blast.update()
            C.SCREEN.blit(blast.image, blast.pos)
            if blast.rect.centerx > C.SCREEN_WIDTH or \
               blast.rect.centerx < 0 or \
               blast.rect.centery > C.SCREEN_HEIGHT or \
               blast.rect.centery < 0: 
                self.blast_list.remove(blast)
    
    def shoot(self):

        blast = Blasters(V(self.rect.centerx-20, self.rect.centery-20), self.dir, (self.speed*C.BLASTER_SPEED), self.blaster)    # Shoots
        self.blast_list.append(blast)

    def player_rotate(self):                            # rotates player 
    
        self.acc.rotate_ip(self.dir_speed)
        self.dir += self.dir_speed

        if self.dir > 360:
            self.dir -= 360
        elif self.dir < 0:
            self.dir += 360 
        self.image = pygame.transform.rotate(self.rotation_img, -self.dir)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def edge(self):

        if self.rect.centerx < 0:
            self.pos[0] = C.SCREEN_WIDTH
        if self.rect.centerx > C.SCREEN_WIDTH:
            self.pos[0] = 0
        if self.rect.centery < 0:
            self.pos[1] = C.SCREEN_HEIGHT
        if self.rect.centery > C.SCREEN_HEIGHT:
            self.pos[1] = 0


   
   