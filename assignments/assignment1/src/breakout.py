import pygame
import sys
from pygame.math import Vector2 as vec 

# screen spesifications

(screen_width, screen_height) = (1645, 1200)
screen = pygame.display.set_mode((screen_width, screen_height))
screen_res = (screen_width, screen_height)

# initialize pygame stuff

pygame.init()
pygame.display.flip()
pygame.display.set_caption("EXTREME BREAKOUT")
background_image = pygame.image.load("pics/galaxy.png")
clock = pygame.time.Clock() 
game_over_image = pygame.image.load("pics/GAME OVER.png")
game_over_image = pygame.transform.scale(game_over_image, (1645, 1200))



# Some working colors 

purple_color = (106, 13, 173)
blue_color = (0, 30, 240)
white_color = (255, 255, 255)
red_color = (240, 0, 30)


# Class for purple bricks

class purple_brick(): 

    def __init__(self,screen,x,y):

        self.color = purple_color
        self.x = x
        self.y = y
        self.w = 200
        self.h = 65
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)


# Class for blue bricks

class blue_brick():

    def __init__(self, screen, x, y):

        self.color = blue_color
        self.x = x
        self.y = y
        self.w = 97.5
        self.h = 65
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)


# Class for the player, A.K.A the paddle

class Player(): 
    
    def __init__(self,screen,x,y):

        self.color = red_color
        self.x = x
        self.y = y
        self.w = 200
        self.h = 5
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    
    def control(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.move_ip(-25, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(25, 0)


# Creates class for the ball

class Ball():

    def __init__(self, screen, center):

        self.color = white_color
        self.x = 40
        self.y = 600
        self.center = (self.x, self.y)
        self.radius = 20
        self.speedx = 8
        self.speedy = 8
        
    def update_pos(self):

        self.x += self.speedx
        self.y += self.speedy
        self.center = (self.x, self.y)

        if self.x < self.radius or self.x > screen_width - self.radius:
            self.speedx *= -1
        if self.y < self.radius:
            self.speedy *= -1

        # If ball goes outside screen 

        if self.y > screen_width + self.radius:
            blue_bricks.clear()
            purple_bricks.clear()
            screen.blit(game_over_image, (0, 0))
            

    def collision(self):

        if self.x + self.radius >= player.rect.x and \
           self.x + self.radius <= player.rect.x + player.rect.width and \
           self.y + self.radius >= player.rect.y and \
           self.y + self.radius <= player.rect.y + player.rect.height: 
            self.speedy *= -1
        
        for blue_brick in blue_bricks: 
            if self.x + self.radius >= blue_brick.rect.x and \
               self.x - self.radius <= blue_brick.rect.x + blue_brick.rect.width and \
               self.y + self.radius >= blue_brick.rect.y and \
               self.y - self.radius <= blue_brick.rect.y + blue_brick.rect.height:
                blue_bricks.remove(blue_brick)
                self.speedy *= -1
        
        for purple_brick in purple_bricks: 
            if self.x + self.radius >= purple_brick.rect.x and \
               self.x - self.radius <= purple_brick.rect.x + purple_brick.rect.width and \
               self.y + self.radius >= purple_brick.rect.y and \
               self.y - self.radius <= purple_brick.rect.y + purple_brick.rect.height:
                purple_bricks.remove(purple_brick)
                self.speedy *= -1
        

# Creates a list for purple bricks

purple_bricks = []  
purple_brick_y_start = 5
purple_brick_x_avstand = 5

# Creats purple bricks for two different rows

for row in range(2):
    for x in range(0, 8):
        brick = purple_brick(screen, 5 + x * (200 + purple_brick_x_avstand), purple_brick_y_start)
        purple_bricks.append(brick)
    purple_brick_y_start += 65 * 2 + 10

# Creates a list for blue bricks

blue_bricks = []
blue_brick_y_start = 75
blue_brick_x_avstand = 5

# Creates blue bricks for two different rows

for row in range(2):
    for x in range(0, 16):
        brick = blue_brick(screen, 5 + x * (97.5 + blue_brick_x_avstand), blue_brick_y_start)
        blue_bricks.append(brick)
    blue_brick_y_start += 65 * 2 + 10

# Creates the player

player = Player(screen, 800, 1100)

# Creates the ball 

ball = Ball(screen, [40, 600])

# Opens window, closes when quit

running = True                

while running:          
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Draws background 

    screen.blit(background_image, [0, 0])  
    
    # Draws the player

    pygame.draw.rect(screen, player.color, player.rect)
    
    # Draws the ball

    pygame.draw.circle(screen, ball.color, ball.center, ball.radius)

    # Updates ball position

    ball.update_pos()

    # Checks for collision between ball and player

    ball.collision()

    # Enables player movement
        
    player.control()

    # Draws the bricks to the window

    for brick in purple_bricks: #draws all bricks in list
        pygame.draw.rect(screen, brick.color, brick.rect)
    for brick in blue_bricks:
        pygame.draw.rect(screen, brick.color, brick.rect)
    


    # Sets game to 30 ticks 
    clock.tick(60)  

    pygame.display.flip()

pygame.quit()
    

    


