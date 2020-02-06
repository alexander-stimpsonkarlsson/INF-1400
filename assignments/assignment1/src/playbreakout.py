import pygame 

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

    ball.player_collision()

    # Checks for collision between ball and brick

    ball.brick_collision()

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