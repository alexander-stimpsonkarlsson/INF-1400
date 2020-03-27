import pygame
import config as P 
from screen_objects import Screen_Obj
from Star_Destroyer import Star_Destroyer
from Millennium_Falcon import Millennium_Falcon
from moveable_obj import Moveable_Obj
from player import Player
from blaster import Blasters

def main():

    pygame.init()

    screen_size = [P.SCREEN_WIDTH, P.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(screen_size)                   

    pygame.display.set_caption("Mayhem: Star Wars Edition")
    font = pygame.font.Font('freesansbold.ttf', 32) 
    icon = pygame.image.load("pics/starwars1.png")
    pygame.display.set_icon(icon)

    running = True 
    time = pygame.time.Clock()

    background = Screen_Obj("pics/bg.png", P.SCREEN_WIDTH, P.SCREEN_HEIGHT, (P.SCREEN_WIDTH/2, P.SCREEN_HEIGHT/2))
    millennium_falcon = Millennium_Falcon()
    star_destroyer = Star_Destroyer()
    player_list = pygame.sprite.Group(background, millennium_falcon, star_destroyer)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:
            running = False

        fps = time.tick(60)

        player_list.draw(screen)                                       

        star_destroyer.update(fps)

        millennium_falcon.update(fps)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()