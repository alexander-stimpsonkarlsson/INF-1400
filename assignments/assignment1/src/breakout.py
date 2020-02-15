import pygame
import sys


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
font = pygame.font.Font('freesansbold.ttf', 32)

# Music 

pygame.mixer.music.load('sound/Push it to the Limit (Scarface).wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(2)

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
        self.w = 250
        self.h = 5
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    
    def control(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.move_ip(-18, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(18, 0)

        if self.rect.x < 0:                       # keeps player within screen  
            self.rect.x = 0
        if self.rect.x + self.w > screen_width:
            self.rect.x = screen_width - self.w

# Creates class for the ball

class Ball():

    def __init__(self, screen, center):

        self.color = white_color
        self.x = 40
        self.y = 600
        self.center = (self.x, self.y)
        self.radius = 15
        self.speedx = 8
        self.speedy = 6
        self.Highscore = 0
        
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
            

    def player_collision(self):

        self_posx = self.x + self.radius
        self_posy = self.y + self.radius

        # 6 different positions on the player paddle

        paddle_pos1 = player.rect.x + player.rect.width / 6
        paddle_pos2 = paddle_pos1 + player.rect.width / 6
        paddle_pos3 = paddle_pos2 + player.rect.width / 6
        paddle_pos4 = paddle_pos3 + player.rect.width / 6
        paddle_pos5 = paddle_pos4 + player.rect.width / 6
        paddle_pos6 = paddle_pos5 + player.rect.width / 6
        
        paddle_y = player.rect.y + player.rect.height

        # Player collisions
                                                # Postion 1
        if self_posx >= player.rect.x and \
           self_posx <= paddle_pos1 and \
           self_posy >=player.rect.y and \
           self_posy <= paddle_y:
            self.speedy = 7
            self.speedy *= -1
            if self.speedx < 0:
                self.speedx = -11
            else: 
                self.speedx = 11
                                                # Position 2
        if self_posx >= paddle_pos1 and \
           self_posx <= paddle_pos2 and \
           self_posy >=player.rect.y and \
           self_posy <= paddle_y:
            self.speedy = 9
            self.speedy *= -1
            if self.speedx < 0:
                self.speedx = -7
            else: 
                self.speedx = 7
                                                # Position 3
        if self_posx >= paddle_pos2 and \
           self_posx <= paddle_pos3 and \
           self_posy >=player.rect.y and \
           self_posy <= paddle_y:
            self.speedy = 10
            self.speedy *= -1
            if self.speedx < 0: 
                self.speedx = -3
            else: 
                self.speedx = 3
                                                # Postion 4
        if self_posx >= paddle_pos3 and \
           self_posx <= paddle_pos4 and \
           self_posy >=player.rect.y and \
           self_posy <= paddle_y:
            self.speedy = 10
            self.speedy *= -1
            if self.speedx > 0:
                self.speedx = 3
            else: 
                self.speedx = -3
                                                # Position 5
        if self_posx >= paddle_pos4 and \
           self_posx <= paddle_pos5 and \
           self_posy >=player.rect.y and \
           self_posy <= paddle_y:
            self.speedy = 9
            self.speedy *= -1
            if self.speedx > 0:
                self.speedx = 7
            else: 
                self.speedx = -7
                                                # Postion 6
        if self_posx >= paddle_pos5 and \
           self_posx <= paddle_pos6 and \
           self_posy >=player.rect.y and \
           self_posy <= paddle_y:
            self.speedy = 7
            self.speedy *= -1
            if self.speedx > 0:
                self.speedx = 11
            else: 
                self.speedx = -11
        
    def brick_collision(self):

        # Brick collisions

        for blue_brick in blue_bricks: 
            if self.x + self.radius > blue_brick.rect.x and \
               self.x - self.radius < blue_brick.rect.x + blue_brick.rect.width and \
               self.y + self.radius > blue_brick.rect.y and \
               self.y - self.radius < blue_brick.rect.y + blue_brick.rect.height:
                self.speedy *= -1
                blue_bricks.remove(blue_brick)
                self.Highscore += 1
                print (self.Highscore, "/ 48")
        
        for purple_brick in purple_bricks: 
            if self.x + self.radius > purple_brick.rect.x and \
               self.x - self.radius < purple_brick.rect.x + purple_brick.rect.width and \
               self.y + self.radius > purple_brick.rect.y and \
               self.y - self.radius < purple_brick.rect.y + purple_brick.rect.height:
                self.speedy *= -1
                purple_bricks.remove(purple_brick)
                self.Highscore += 1
                print (self.Highscore, "/ 48")
                
# Creates a list for purple bricks

purple_bricks = []  
purple_brick_y_start = 5
purple_brick_x_avstand = 5

# Creates purple bricks for two different rows

for row in range(2):
    for x in range(8):
        brick = purple_brick(screen, 5 + x * (200 + purple_brick_x_avstand), purple_brick_y_start)
        purple_bricks.append(brick)
    purple_brick_y_start += 65 * 2 + 10

# Creates a list for blue bricks

blue_bricks = []
blue_brick_y_start = 75
blue_brick_x_avstand = 5

# Creates blue bricks for two different rows

for row in range(2):
    for x in range(16):
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
    
    # Draws higscore
    highscore = font.render("Score: " + str(ball.Highscore) + "/ 48", running, purple_color, blue_color)
    textHighscore = highscore.get_rect()
    textHighscore.center = (1500, 1000)
    screen.blit(highscore, textHighscore)

    # Draws the player

    pygame.draw.rect(screen, player.color, player.rect)
    
    # Draws the ball

    pygame.draw.circle(screen, ball.color, ball.center, ball.radius)

    # Updates ball position

    ball.update_pos()

    # Checks for collision between ball and player

    ball.player_collision()

    # Checks for collision between ball and brick

    ball.brick_collision()

    # Enables player movement
        
    player.control()

    # Draws the bricks to the window

    for brick in purple_bricks: 
        pygame.draw.rect(screen, brick.color, brick.rect)
    for brick in blue_bricks:
        pygame.draw.rect(screen, brick.color, brick.rect)
    
    # Sets game to 30 ticks 
    clock.tick(60)  

    pygame.display.flip()

pygame.quit()
    

    


