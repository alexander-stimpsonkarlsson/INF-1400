import pygame
import math as M
import config as P 
from pygame import Vector2 as V
from moveable_obj import Moveable_Obj
from pygame.locals import *
from blaster import Blasters

screen_size = [P.SCREEN_WIDTH, P.SCREEN_HEIGHT]
screen = pygame.display.set_mode(screen_size) 

# Parent class for players, inherits from moveable_obj

class Player(Moveable_Obj):

    def __init__(self, pics, x, y, pos, ctrl):
        super().__init__(pics, x, y, pos)

        self.ctrl = ctrl
        self.acc = V(0, -P.PLAYER_ACC)
        self.dir_speed = 0
        self.blast_list = []

    def update(self, fps):
        
        self.edge()
        key = pygame.key.get_pressed()
    
        if key[self.ctrl[1]]:                           # left, rotates
            self.dir_speed = -P.PLAYER_SPIN
            self.player_rotate() 
        if key[self.ctrl[2]]:                           # right, rotate
            self.dir_speed = P.PLAYER_SPIN
            self.player_rotate() 
        
        if key[self.ctrl[0]]:                           # thrust upwards
            self.speed += self.acc
        
        if key[self.ctrl[3]]:
            self.shoot()
        
        if self.speed.length() > P.PLAYER_MAX_THRUST:          # restricts max thrust
            self.speed.scale_to_length(P.PLAYER_MAX_THRUST)
        
        self.speed += P.GRAVITY
        self.pos += self.speed                          # updates position 
        self.rect.center = self.pos 

        for blast in self.blast_list:
            blast.update()
            screen.blit(blast.image, self.pos)
    
    def shoot(self):

        blast = Blasters(self.pos, self.dir, self.speed)    # Shoots
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
            self.pos[0] = P.SCREEN_WIDTH
        if self.rect.centerx > P.SCREEN_WIDTH:
            self.pos[0] = 0
        if self.rect.centery < 0:
            self.pos[1] = P.SCREEN_HEIGHT
        if self.rect.centery > P.SCREEN_HEIGHT:
            self.pos[1] = 0


   
   