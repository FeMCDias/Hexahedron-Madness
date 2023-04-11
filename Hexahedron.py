import pygame as pg 
import sys
from pygame.locals import *
import numpy as np
import math

from main import main

class Cube(object):
    def __init__(self,screen) -> None:
        self.angleX = np.deg2rad(1)
        self.angleY = np.deg2rad(1) 
        self.angleZ = np.deg2rad(1)
        self.d = 400  # ajustar o valor para alterar a distância da câmera
        self.screen = screen
        self.cube =  np.array([[-100, -100, -100, 1], [100, -100, -100, 1], [100, 100, -100, 1], [-100, 100, -100, 1], [-100, -100, 100, 1], [100, -100, 100, 1], [100, 100, 100, 1], [-100, 100, 100, 1]]).T
        self.P = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-self.d],[0,0,-(1/self.d),0]])
        self.directions = ['none']
        self.count_rotations = 0
        self.lines = [(0, 1), (1, 2), (2, 3), (3, 0),
                      (4, 5), (5, 6), (6, 7), (7, 4),
                      (0, 4), (1, 5), (2, 6), (3, 7)]
        self.update()

    def update(self):

        self.rx = np.array([[1, 0, 0, 0], [0, math.cos(self.angleX), -math.sin(self.angleX), 0],[0, math.sin(self.angleX), math.cos(self.angleX), 0],[0, 0, 0, 1]])
        self.ry = np.array([[math.cos(self.angleY), 0, math.sin(self.angleY), 0], [0, 1, 0, 0],[-math.sin(self.angleY), 0, math.cos(self.angleY), 0],[0, 0, 0, 1]])
        self.rz = np.array([[math.cos(self.angleZ), -math.sin(self.angleZ), 0, 0],[math.sin(self.angleZ), math.cos(self.angleZ), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
        self.rotation = self.rx @ self.ry @ self.rz # rotation matrix

        self.tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, self.d], [0, 0, 0, 1]]) #Matriz de translação - Eixo Z
        self.tc = np.array([[1, 0, 0, 400], [0, 1, 0, 300],[0, 0, 1, 0],[0, 0, 0, 1]]) #Matriz de translação - Centro da tela
        self.transformation = self.tc @ self.P @ self.tz @ self.rotation #Matriz de transformação total do cubo
        
        self.projected = self.transformation @ self.cube #Cubo - transformado - aplicar a matriz de transformação

    def change_direction(self):
        if 'none' not in self.directions:
            self.count_rotations += 1
            if self.count_rotations % 20 ==0:
                if 'right' in self.directions:
                    self.angleY += np.deg2rad(1)
                if 'left' in self.directions:
                    self.angleY -= np.deg2rad(1)
                if 'up' in self.directions:
                    self.angleX += np.deg2rad(1)
                if 'down' in self.directions:
                    self.angleX -= np.deg2rad(1)
                if 'z_down' in self.directions:
                    self.angleZ += np.deg2rad(1)
                if 'z_up' in self.directions:
                    self.angleZ -= np.deg2rad(1)
                print('OK')

    def draw_cube(self):
        for i in range(8):
            pg.draw.circle(self.screen, (255, 255, 255), ((self.projected[0][i] / self.projected[3][i]), (self.projected[1][i] / self.projected[3][i])), 5)
        for a, b in self.lines:
            p1 = (self.projected[0][a] / self.projected[3][a], self.projected[1][a] / self.projected[3][a])
            p2 = (self.projected[0][b] / self.projected[3][b], self.projected[1][b] / self.projected[3][b])
            pg.draw.line(self.screen, (255, 255, 255), p1, p2)

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_cube()
            # self.change_direction()
            
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if 'none' in self.directions:
                        self.directions.remove('none')
                    if event.key == K_d:
                        self.directions.append('right')
                    if event.key == K_a:
                        self.directions.append('left')
                    if event.key == K_w:
                        self.directions.append('up')
                    if event.key == K_s:
                        self.directions.append('down')
                    if event.key == K_z:
                        self.directions.append('z_down')
                    if event.key == K_x:
                        self.directions.append('z_up')
                if event.type == KEYUP:
                    if event.key == K_d:
                        self.directions.remove('right')
                    if event.key == K_a:
                        self.directions.remove('left')
                    if event.key == K_w:
                        self.directions.remove('up')
                    if event.key == K_s:
                        self.directions.remove('down')
                    if event.key == K_z:
                        self.directions.remove('z_down')
                    if event.key == K_x:
                        self.directions.remove('z_up')
                if event.type == pg.MOUSEBUTTONDOWN:
                    # Scroll to Zoom Function
                    if event.button == 4:
                        self.d += 5
                    if event.button == 5:
                        self.d -= 5
            self.change_direction()
            self.update()

            pg.display.update()


