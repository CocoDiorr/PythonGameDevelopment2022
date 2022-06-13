from game.Game import Game
import os
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('VMiK')
    pygame.display.set_icon(pygame.image.load(os.path.join("pics", "menu", "vmik_logo.png")))
    game = Game()
    game.run()
    pygame.quit()
