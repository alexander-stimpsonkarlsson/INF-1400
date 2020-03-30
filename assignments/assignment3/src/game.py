import pygame
import config as C 
from screen_objects import Screen_Obj
from Star_Destroyer import Star_Destroyer
from Millennium_Falcon import Millennium_Falcon
from moveable_obj import Moveable_Obj
from player import Player
from blaster import Blasters

class Game(pygame.sprite.Sprite):

    def __init__(self):

        self.caption    = pygame.display.set_caption("Mayhem: Star Wars Edition") 
        self.font       = pygame.font.Font('freesansbold.ttf', 32) 
        self.icon       = pygame.image.load("pics/starwars1.png")
        pygame.display.set_icon(self.icon)

        self.background = Screen_Obj("pics/bg.png", C.SCREEN_WIDTH, C.SCREEN_HEIGHT, (C.SCREEN_WIDTH/2, C.SCREEN_HEIGHT/2))
        self.player1    = Millennium_Falcon()
        self.player2    = Star_Destroyer()
        self.group      = pygame.sprite.Group(self.background, self.player1, self.player2)

    def update(self, fps):

        self.group.draw(C.SCREEN) 
        self.player1.update()
        self.player2.update()
        self.player1_collision()
        self.player2_collision()
    
    def player1_collision(self):

        for blast in self.player1.blast_list:
            collision = pygame.sprite.collide_rect(blast, self.player2)
            if collision == True:
                self.player2.explosion()

    def player2_collision(self):

        for blast in self.player2.blast_list:
            collision = pygame.sprite.collide_rect(blast, self.player1)
            if collision == True:
                self.player1.explosion()
    

