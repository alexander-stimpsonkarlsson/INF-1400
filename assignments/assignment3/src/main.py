from game import Game
import pygame
import cProfile
import re
cProfile.run('re.compile("foo|bar")')
# Main loop

def main():

    game = Game()       # Create game object
    game.run()       # Updates game 

if __name__ == "__main__":
    main()