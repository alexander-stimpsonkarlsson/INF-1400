import pygame
import math as M
import parameter as P 
from screen_objects import Screen_Obj
from moveable_obj import Moveable_Obj
from pygame.locals import *

class Player(Moveable_Obj):

    def __init__(self, pics, length, height, pos):

        self.up     = 0
        self.down   = 0
        self.right  = 0
        self.left   = 0

    def update(self):

        x = self.pos[0]
        y = self.pos[1]

        self.speed += (self.up + self.down)

        if self.speed > P.PLAYER_SPEED:
            self.speed = P.PLAYER_SPEED
        
        if self.speed < -P.PLAYER_FALL:
            self.speed = -P.PLAYER_FALL
        
        self.dir += (self.left + self.right)
        angle = self.dir * math.pi / 180

        x += -self.speed*math.sin(angle)
        y += -self.speed*math.cos(angle)

        self.pos[0] = x
        self.pos[1] = y

        self.image = pygame.transform.rotate(self.image, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def control(player1, player2):

        for event in pygame.event.get():

            pressed = event.type == KEYDOWN     # Checks if key is held down, returns true if its held down 
            if event.key == K_UP:
                player1.up = pressed * 2
            elif event.key == K_DOWN: 
                player1.down = pressed * -2
            if event.key == K_RIGHT:
                player1.right = pressed *-2
            if event.key == K_LEFT:
                player1.left = pressed *2
            
            if event.key == K_w:
                player2.up = pressed * 2
            elif event.key == K_s: 
                player2.down = pressed * -2
            if event.key == K_d:
                player2.right = pressed *-2
            if event.key == K_a:
                player2.left = pressed *2
            
        if (player1.speed != 0):
            if player1.speed > 0: 
                player1.speed -= 0.5
            elif player1.speed < 0: 
                player1.speed += 0.5

        if (player2.speed != 0):
            if player2.speed > 0:
                player2.speed -= 0.5
            elif player2.speed < 0: 
                player2.speed += 0.5






