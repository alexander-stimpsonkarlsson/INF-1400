import pygame
from pygame import Vector2 as V
import os
from os import path
pygame.mixer.init()

# Global 

SCREEN_WIDTH        = 1600
SCREEN_HEIGHT       = 900
GRAVITY             = V(0, 0.1)
SCREEN_SIZE         = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN              = pygame.display.set_mode(SCREEN_SIZE) 
THEME_MUSIC         = ("sounds/music.wav")
EXPLOSION_ANIMATION = ["animation/e0.png", "animation/e1.png", "animation/e2.png", "animation/e3.png", "animation/e4.png",
                       "animation/e5.png", "animation/e6.png", "animation/e7.png", "animation/e8.png", "animation/e9.png",
                       "animation/e10.png", "animation/e11.png", "animation/e12.png", "animation/e13.png", "animation/e14.png",
                       "animation/e15.png"]
#[pygame.image.load(os.path.join("animation", img)).convert_alpha()
#for img in os.listdir("animation")]
WHITE               = (255, 255, 255)
BLACK               = (0, 0, 0)

# Player 

PLAYER_SPEED        = 10
PLAYER_ACC          = 0.6
PLAYER_SPIN         = 4
PLAYER_MAX_THRUST   = 10
PLAYER_COLLISION    = 4

# Millennium falcon

MILLENNIUM_POS      = (300, 800)
MILLENIUM_CTRL      = [pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_q]
MILLENIUM_H         = 90
MILLENIUM_W         = 80
MILLENIUM_SOUND     = pygame.mixer.Sound("sounds/millenium_sound.wav")
MILLENIUM_SOUND.set_volume(0.1)

# Star destroyer

STAR_POS            = (1400, 800)
STAR_CTRL           = [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_PERIOD]
STAR_H              = 100
STAR_W              = 70
STAR_SOUND          = pygame.mixer.Sound("sounds/star_sound.wav")
STAR_SOUND.set_volume(0.04)

# Blaster

BLASTER_H           = 60
BLASTER_W           = 40
BLASTER_SPEED       = 3
