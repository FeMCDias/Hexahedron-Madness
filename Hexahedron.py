import pygame, sys
from pygame.locals import *
import os

class TaxiGame():
    def __init__(self):
        pygame.init()

        # Set icon
        icon = pygame.image.load(os.path.join('assets','images','taxi_icon.png'))
        pygame.display.set_icon(icon)

        # Set music
        # pygame.mixer.init()
        # pygame.mixer.music.set_volume(0.08)
        # pygame.mixer.music.load(os.path.join('assets', 'sounds', 'song_name_here.mp3))
        # pygame.mixer.music.play(-1)

        # Set title
        pygame.display.set_caption('Hexahedron Madness!')

        # Colours
        self.BACKGROUND = (0, 0, 0)
        
        # Game Setup
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        self.window_width = 1152
        self.window_height = 768
        self.generic_font = pygame.font.Font(None, 30)
        # Identify Assets
        self.assets = {
        }
        
        # Identify state
        self.state = {
        }
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
                    
    def render_screen(self):
        self.fpsClock.tick(self.FPS)
        pygame.display.update()
            
    
    def run(self):
        looping = True
        # The main game loop
        while looping :
            for event in pygame.event.get() :
                if event.type == QUIT :
                    pygame.quit()
                    sys.exit()
            # Render elements of the game
            self.render_screen()
            pygame.display.update()
            self.fpsClock.tick(self.FPS)

game = TaxiGame()
game.run()