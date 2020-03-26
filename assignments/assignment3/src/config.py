import pygame
from pygame import Vector2 as V

# Global 

SCREEN_WIDTH        = 1600
SCREEN_HEIGHT       = 900
GRAVITY             = V(0, 0.1)

# Player 

PLAYER_SPEED        = 10
PLAYER_ACC          = 0.6
PLAYER_SPIN         = 4
PLAYER_MAX_THRUST   = 10

# Millennium falcon

MILLENNIUM_POS      = (300, 800)
MILLENIUM_CTRL      = [pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_q]
MILLENIUM_H         = 90
MILLENIUM_W         = 80

# Star destroyer

STAR_POS            = (1400, 800)
STAR_CTRL           = [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_l]
STAR_H              = 100
STAR_W              = 70

# Green blaster

G_H                 = 60
G_W                 = 40
BLAST_SPEED         = 20

# Red blaster       

R_H                 = 20
R_W                 = 10