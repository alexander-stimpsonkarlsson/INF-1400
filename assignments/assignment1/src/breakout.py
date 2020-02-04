import pygame
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

# Some working colors 

purple_color = (106, 13, 173)
blue_color = (0, 30, 240)
white_color = (255, 255, 255)
red_color = (240, 0, 30)

# Class for purple bricks

class purple_brick(pygame.sprite.Sprite): 

    def __init__(self,screen,x,y):

        super().__init__()

        self.color = purple_color
        self.x = x
        self.y = y
        self.w = 200
        self.h = 65
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)

# Class for blue bricks

class blue_brick(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        
        super().__init__()

        self.color = blue_color
        self.x = x
        self.y = y
        self.w = 97.5
        self.h = 65
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)

# Class for the player, A.K.A the paddle

class Player(pygame.sprite.Sprite): 
    
    def __init__(self,screen,x,y):

        super().__init__()

        self.color = red_color
        self.x = x
        self.y = y
        self.w = 150
        self.h = 5
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    
    def control(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.move_ip(-25, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(25, 0)

# Creates class for the ball

class Ball(pygame.sprite.Sprite):

    def __init__(self, screen, center):

        super().__init__()

        self.color = white_color
        self.x = 40
        self.y = 600
        self.center = (self.x, self.y)
        self.radius = 20
        self.speedx = 10
        self.speedy = 10
        
        
    def update_pos(self):

        self.x += self.speedx
        self.y += self.speedy
        self.center = (self.x, self.y)

        if self.x < self.radius or self.x > screen_width - self.radius:
            self.speedx *= -1
        if self.y < self.radius or self.y > screen_height - self.radius:
            self.speedy *= -1
        #om ball.x >= player.x and ball.x <= player.x + player.w
        #om ball
            #self.speedx *= -1
            #self.speedy *= -1

    def collision(self):

        if self.x > plar.x and self.xye < player.x + player.w:
            self.speedx *= -1
        if self.y > player.y and self.y < player.y + player.w:
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
    clock.tick(30)  


    pygame.display.flip()
    

    


