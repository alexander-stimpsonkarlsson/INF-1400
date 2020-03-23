import pygame
import parameter as P 
from player import Player
from pygame.locals import *

class Trump(Player):

    trump_pos = (300, 600)

    def __init__(self):
        super().__init__("pics/smoosh.png", 20, 20, (300, 600))

    def control(self):

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
                
            if (self.speed != 0):
                if self.speed > 0: 
                    self.speed -= 0.5
                elif self.speed < 0: 
                    self.speed += 0.5
