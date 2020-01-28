import pygame
from pygame.math import Vector2 as vec 


(width, height) = (1700, 1200)
screen = pygame.display.set_mode((width, height))
screen_res = (1700, 1200)
pygame.init()
pygame.display.flip()
pygame.display.set_caption("EXTREME BREAKOUT")
background_image = pygame.image.load("pics/galaxy.png")
clock = pygame.time.Clock() 

#fra vector fil
#.
class purple_brick: #classe for purple objects
    def __init__(self,screen,x,y):
        self.color=(106,13,173)
        self.x = x
        self.y = y
        self.w = 200
        self.h = 75
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)

bricks = []                           #adds bricks to list 
brick1 = purple_brick(screen,5,5)            
brick2 = purple_brick(screen,210,5)   
brick3 = purple_brick(screen,415,5)   
brick4 = purple_brick(screen,620,5)  
brick5 = purple_brick(screen,825,5)   
brick6 = purple_brick(screen,1030,5)   
brick7 = purple_brick(screen,1235,5)   
brick8 = purple_brick(screen,1440,5)  
brick9 = purple_brick(screen,1645,5)    


#bricks.extend((brick1, brick2, brick3, brick4))



running = True  #keeps window open until we close it                  
while running:          
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.blit(background_image, [0, 0])  #background

    for brick in bricks: #draws all bricks in list
        pygame.draw.rect(screen, brick.color, brick.rect)


    clock.tick(30)  #sets game to 30 ticks 


    pygame.display.flip()
    

    


