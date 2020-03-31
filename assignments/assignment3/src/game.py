import pygame
import config as C 
from screen_objects     import Screen_Obj
from Star_Destroyer     import Star_Destroyer
from Millennium_Falcon  import Millennium_Falcon
from moveable_obj       import Moveable_Obj
from player             import Player
from blaster            import Blasters
from explosion          import Explosion

class Game(pygame.sprite.Sprite):

    def __init__(self):
        pygame.init()                           # Pygame initiazer       
        pygame.mixer.init()
        pygame.font.init()

        self.caption    = pygame.display.set_caption("Mayhem: Star Wars Edition") 
        self.font       = pygame.font.Font('freesansbold.ttf', 32) 
        self.icon       = pygame.image.load("pics/starwars1.png")
        pygame.display.set_icon(self.icon)
        self.time       = pygame.time.Clock()                           # Gets time, used for update frequenzy
        self.fps        = self.time.tick(60)                            # Set update frequency(fps) to 60

        self.background = Screen_Obj("pics/bg.png", C.SCREEN_WIDTH, 
        C.SCREEN_HEIGHT, (C.SCREEN_WIDTH/2, C.SCREEN_HEIGHT/2))
        self.restart_t  = Screen_Obj("pics/restart.png", 600, 100, (C.SCREEN_WIDTH/2, C.SCREEN_HEIGHT/2))
        self.player1    = Millennium_Falcon()
        self.player2    = Star_Destroyer()
        self.group      = pygame.sprite.Group(self.background, self.player1, self.player2)

    def update(self):

        running = True 

        pygame.mixer.music.load(C.THEME_MUSIC)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # Exit by closing window
                    running = False
            
            key = pygame.key.get_pressed()

            if key[pygame.K_ESCAPE]:            # Exit by pressing ESC
                running = False

            self.group.draw(C.SCREEN) 

            if self.player1 in self.group:
                self.player1.update(self.fps)
                self.player2_collision()

            if self.player2 in self.group:
                self.player2.update(self.fps)            
                self.player1_collision()
            
            if self.player2 not in self.group or self.player1 not in self.group:
                self.group.empty()
                self.group.add(self.background, self.restart_t)
                if key[pygame.K_SPACE]:
                    self.group.empty()
                    self.player1 = Millennium_Falcon()
                    self.player2 = Star_Destroyer()
                    self.group.add(self.background, self.player1, self.player2)
                
            pygame.display.flip()
    
        pygame.quit()
            
    def player1_collision(self):

        for blast in self.player1.blast_list:
            if pygame.sprite.collide_rect(blast, self.player2):
                boom = Explosion(self.player2.rect.center)
                boom.update()
                self.group.add(boom)
                self.group.remove(self.player2)
        
        if pygame.sprite.collide_rect(self.player1, self.player2):
            self.group.remove(self.player1, self.player2)

    def player2_collision(self):

        for blast in self.player2.blast_list:
            if pygame.sprite.collide_rect(blast, self.player1):
                boom = Explosion(self.player1.rect.center)
                boom.update()
                self.group.add(boom)
                self.group.remove(self.player1)
    

