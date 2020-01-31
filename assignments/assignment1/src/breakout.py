import pygame
from pygame.math import Vector2 as vec 

# screen spesifications
(width, height) = (1645, 1200)
screen = pygame.display.set_mode((width, height))
screen_res = (width, height)

pygame.init()
pygame.display.flip()
pygame.display.set_caption("EXTREME BREAKOUT")
background_image = pygame.image.load("pics/galaxy.png")
clock = pygame.time.Clock() 

#fra vector fil
#.
class purple_brick: #classe for purple objects
    def __init__(self,screen,x,y):
        self.color =(106,13,173)
        self.x = x
        self.y = y
        self.w = 200
        self.h = 65
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)

bricks = []                           #adds bricks to list 
brick1 = purple_brick(screen,5,5) 
bricks.append(brick1)           
brick2 = purple_brick(screen,210,5)   
bricks.append(brick2)
brick3 = purple_brick(screen,415,5)   
bricks.append(brick3)
brick4 = purple_brick(screen,620,5)  
bricks.append(brick4)
brick5 = purple_brick(screen,825,5) 
bricks.append(brick5)  
brick6 = purple_brick(screen,1030,5)  
bricks.append(brick6) 
brick7 = purple_brick(screen,1235,5)   
bricks.append(brick7)
brick8 = purple_brick(screen,1440,5)  
bricks.append(brick8)
    
class Player: 
    def __init__(self,screen,x,y):
        self.color = (240, 0, 0)
        self.x = x
        self.y = y
        self.w = 150
        self.h = 5
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    
    def control(self):
        key = pygame.key.get_pressed()
        dist = 1

        if key[pygame.K_LEFT]:
            self.rect.move_ip(-25, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(25, 0)
        
    
    
player = Player(screen, 800, 1100)



# opens window, closes when quit
running = True                   
while running:          
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # background 
    screen.blit(background_image, [0, 0])  

    # controls
    

    pygame.draw.rect(screen, player.color, player.rect)
    
    player.control()
    

    # bricks
    for brick in bricks: #draws all bricks in list
        pygame.draw.rect(screen, brick.color, brick.rect)
    


    # sets game to 30 ticks 
    clock.tick(30)  


    pygame.display.flip()
    

    


