import pygame, sys
from pygame.locals import *
import numpy as np
import os

class Hexahedron():
    def __init__(self):
        pygame.init()

        # Set icon
        icon = pygame.image.load(os.path.join('assets','images','cube_icon.jpg'))
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
            'd': 200,
            'cube': [],
            'rx': None,
            'ry': None,
            'rz': None,
            'theta_x': 1,
            'theta_y': 1,
            'theta_z': 1,
            'proj': None
        }
        self.create_cube()
        self.create_projection()
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

    def create_cube(self):
        self.state['cube'] = np.array([[1, 1, -1, -1, 1, 1, -1, -1], 
                                       [1, -1, -1, 1, 1, -1, -1, 1],
                                       [-1, -1, -1, -1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1, 1, 1]])
        self.state['cube'][2] += 5
        self.state['cube'][0] *= 200
        self.state['cube'][0] += self.window_width//2
        self.state['cube'][1] *= 200
        self.state['cube'][1] += self.window_height//2


    def update_rx_ry_rz(self):
        self.rx = np.array([[1, 0, 0, 0],
                            [0, np.cos(self.state['theta_x']), -np.sin(self.state['theta_x']), 0],
                            [0, np.sin(self.state['theta_x']), np.cos(self.state['theta_x']), 0],
                            [0, 0, 0, 1]])
        self.ry = np.array([[np.cos(self.state['theta_y']), 0, np.sin(self.state['theta_y']), 0],
                            [0, 1, 0, 0],
                            [-np.sin(self.state['theta_y']), 0, np.cos(self.state['theta_y']), 0],
                            [0, 0, 0, 1]])
        self.rz = np.array([[np.cos(self.state['theta_z']), -np.sin(self.state['theta_z']), 0, 0],
                            [np.sin(self.state['theta_z']), np.cos(self.state['theta_z']), 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])

    def create_projection(self):
        self.proj = np.array([[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 0, -self.state['d']],
                              [0, 0, -1/self.state['d'], 0]])

    def update_cube(self):
        self.state['cube'] = self.rx @ self.ry @ self.rz @ self.state['cube']
        self.state['cube'] = self.proj @ self.state['cube']
        self.state['cube'] = self.state['cube']/self.state['cube'][3]
        print(self.state['cube'])

    def draw_cube(self):
        self.window.fill(self.BACKGROUND)
        for i in range(8):
        # draw circle for vertices
            pygame.draw.circle(self.window, (255, 255, 255), (int(self.state['cube'][0][i]), int(self.state['cube'][1][i])), 7)
        pygame.display.flip()
    

    def render_screen(self):
        self.fpsClock.tick(self.FPS)
        self.draw_cube()
            
    
    def run(self):
        looping = True
        # The main game loop
        print(self.state['cube'])
        while looping :
            for event in pygame.event.get() :
                if event.type == QUIT :
                    pygame.quit()
                    sys.exit()
            self.update_rx_ry_rz()
            self.update_cube()
            self.render_screen()
            pygame.display.update()

game = Hexahedron()
game.run()