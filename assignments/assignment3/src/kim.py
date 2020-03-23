import pygame
import parameter as P 
from player import Player
from pygame.locals import *

class Kim(Player):

    kim_pos = (500, 500)

    def __init__(self):
        super().__init__("pics/kimgethit.png", 20, 20, (500, 500))

    def control(player1, player2):

        for event in pygame.event.get():

            pressed = event.type == KEYDOWN     # Checks if key is held down, returns true if its held down 
            if event.key == K_w:
                self.up = pressed * 2
            elif event.key == K_s: 
                self.down = pressed * -2
            if event.key == K_d:
                self.right = pressed *-2
            if event.key == K_a:
                self.left = pressed *2

        if (self.speed != 0):
            if self.speed > 0:
                self.speed -= 0.5
            elif self.speed < 0: 
                self.speed += 0.5
