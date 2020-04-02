import pygame
import config as C 
import random as R
from pygame import Vector2 as V
from screen_objects     import Screen_Obj
from Star_Destroyer     import Star_Destroyer
from Millennium_Falcon  import Millennium_Falcon
from moveable_obj       import Moveable_Obj
from player             import Player
from blaster            import Blasters
from explosion          import Explosion
from fuel               import Fuel

class Game(pygame.sprite.Sprite):

    def __init__(self):
        pygame.init()                           # Pygame initiazer       
        pygame.mixer.init()                     # Sound initiazer 
        pygame.font.init()                      # Font initiazer

        self.caption    = pygame.display.set_caption("Mayhem: Star Wars Edition") 
        self.font       = pygame.font.Font('freesansbold.ttf', 16) 
        self.icon       = pygame.image.load("pics/starwars1.png")
        pygame.display.set_icon(self.icon)
        self.time       = pygame.time.Clock()                           # Gets time, used for update frequenzy
        self.fps        = self.time.tick(60)                            # Set update frequency(fps) to 60

        self.background = Screen_Obj("pics/bg.png", C.SCREEN_WIDTH, 
        C.SCREEN_HEIGHT, (C.SCREEN_WIDTH/2, C.SCREEN_HEIGHT/2))
        self.restart_t  = Screen_Obj("pics/restart.png", 600, 100, (C.SCREEN_WIDTH/2, C.SCREEN_HEIGHT/2))
        self.player1    = Millennium_Falcon()
        self.player2    = Star_Destroyer()
        self.group      = pygame.sprite.Group(self.background, self.player1, self.player2)  # Sprite group
        self.fuel_count = 0
        self.count      = 0
        self.fuel       = None

    def update(self):

        running = True 

        pygame.mixer.music.load(C.THEME_MUSIC)                  # Initialize music
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                   # Exit by closing window
                    running = False

            player1_health = self.font.render("Health: " + str(self.player1.health) + "/5", running, C.WHITE, C.BLACK)
            text_area1 = player1_health.get_rect()
            text_area1.center = (100, 820)                      # Text for player1 health

            player2_health = self.font.render("Health: " + str(self.player2.health) + "/5", running, C.WHITE, C.BLACK)
            text_area2 = player2_health.get_rect()      
            text_area2.center = (1500, 820)                     # Text for player2 health

            player1_fuel = self.font.render("Fuel: " + str(self.player1.fuel) + "/1000", running, C.WHITE, C.BLACK)
            fuel_area1 = player1_fuel.get_rect()
            fuel_area1.center = (100, 850)                      # Text for player1 fuel 

            player2_fuel = self.font.render("Fuel: " + str(self.player2.fuel) + "/1000", running, C.WHITE, C.BLACK)
            fuel_area2 = player2_fuel.get_rect()
            fuel_area2.center = (1500, 850)                     # Text for player2 fuel
            
            key = pygame.key.get_pressed()                      # Check for key input

            if key[pygame.K_ESCAPE]:                            # Exit by pressing ESC
                running = False

            self.group.draw(C.SCREEN)                           # Draws all sprite group objects
            self.group.update(self.fps)                         # Updates all sprite group objects

            if self.fuel_count < 1:                             # Spawn new fuel after count has reached certain value and there are no
                self.count += 1                                 # more than one fuel on screen
                if self.count == 200:
                    self.fuel_spawn(self.random_pos())          # Spawns fuel at random location 
                    self.fuel_count += 1
                    self.count = 0

            if len(self.group) > 2:                             # If there are more objects than two in group then display text
                C.SCREEN.blit(player1_health, text_area1)
                C.SCREEN.blit(player2_health, text_area2)
                C.SCREEN.blit(player1_fuel, fuel_area1)
                C.SCREEN.blit(player2_fuel, fuel_area2)

            if self.player1 in self.group:                      # Player1 collision detection
                self.player1_collision()

            if self.player2 in self.group:                      # Player2 collision detection
                self.player2_collision()

            if self.player2 not in self.group or self.player1 not in self.group:    # Should one player object not be in the list
                self.group.empty()                                                  # the game is done and the player can choose
                self.group.add(self.background, self.restart_t)                     # to play again by pressing SPACE
                if key[pygame.K_SPACE]:
                    self.group.empty()                          
                    self.player1 = Millennium_Falcon()
                    self.player2 = Star_Destroyer()
                    self.group.add(self.background, self.player1, self.player2)

            pygame.display.flip()
    
        pygame.quit()
            
    def player1_collision(self):                                        
                                                                       
        temp = V(0, 0)                                                 

        for blast in self.player1.blast_list:
            if pygame.sprite.collide_rect(blast, self.player2):         # Collision detection between player1_blaster and player2   
                self.player1.blast_list.remove(blast)                   # Removes player1 blast on collision 
                boom = Explosion(self.player2.rect.center)              # Creates explosion object if they collide
                self.group.add(boom)
                if self.player2.health == 1:                            # 
                    self.group.remove(self.player2)
                else:
                    self.player2.health -= 1
        
        if pygame.sprite.collide_rect(self.player1, self.player2):      # If two player objects collide, they bounce of each other with the 
            temp = self.player2.speed                                   # corresponding vector from the other player
            self.player2.speed = self.player1.speed*C.PLAYER_COLLISION
            self.player1.speed = temp*C.PLAYER_COLLISION
        
        if self.fuel in self.group:
            if pygame.sprite.collide_rect(self.fuel, self.player1):
                self.player1.fuel += 500
                self.group.remove(self.fuel)
                self.fuel_count -= 1

    def player2_collision(self):

        for blast in self.player2.blast_list:
            if pygame.sprite.collide_rect(blast, self.player1):
                self.player2.blast_list.remove(blast)
                boom = Explosion(self.player1.rect.center)
                self.group.add(boom)
                if self.player1.health == 1:                            # 
                    self.group.remove(self.player1)
                else:
                    self.player1.health -= 1
        
        if self.fuel in self.group:
            if pygame.sprite.collide_rect(self.fuel, self.player2):
                self.player2.fuel += 500
                self.group.remove(self.fuel)
                self.fuel_count -= 1
        
    def fuel_spawn(self, pos):                                          # Creates fuel object and adds to sprite group

        self.fuel = Fuel(pos)
        self.group.add(self.fuel)

    def random_pos(self):                                               # returns random position on screen, used for fuel position

        return (R.uniform(100, C.SCREEN_WIDTH-100), R.uniform(100, C.SCREEN_HEIGHT-100))
    

