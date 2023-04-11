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
        self.cube =  np.array([[-50, -50, -50, 1], [50, -50, -50, 1], [50, 50, -50, 1], [-50, 50, -50, 1], [-50, -50, 50, 1], [50, -50, 50, 1], [50, 50, 50, 1], [-50, 50, 50, 1]]).T
        self.P = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-self.d],[0,0,-(1/self.d),0]])
        self.direction = 'right'
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

    def change_direction(self,direction = ''):
        self.direction = direction
        if self.direction == 'right' or self.direction == '':
            self.rotation = self.rotation @ self.rx
        elif self.direction == 'left':
            self.rotation = self.rotation @ self.ry
        elif self.direction == 'up':
            self.rotation = self.rotation @ self.rz
        elif self.direction == 'down':
            self.rotation = self.rotation @ self.rx @ self.ry @ self.rz            

    def draw_cube(self):
        for i in range(8):
            pg.draw.circle(self.screen, (255, 255, 255), ((self.projected[0][i] / self.projected[3][i]), (self.projected[1][i] / self.projected[3][i])), 5)
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][i] / self.projected[3][i]), (self.projected[1][i] / self.projected[3][i])), ((self.projected[0][(i + 1) % 4] / self.projected[3][(i + 1) % 4]), (self.projected[1][(i + 1) % 4] / self.projected[3][(i + 1) % 4])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][i] / self.projected[3][i]), (self.projected[1][i] / self.projected[3][i])), ((self.projected[0][(i + 4) % 8] / self.projected[3][(i + 4) % 8]), (self.projected[1][(i + 4) % 8] / self.projected[3][(i + 4) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 4) % 8] / self.projected[3][(i + 4) % 8]), (self.projected[1][(i + 4) % 8] / self.projected[3][(i + 4) % 8])), ((self.projected[0][(i + 5) % 8] / self.projected[3][(i + 5) % 8]), (self.projected[1][(i + 5) % 8] / self.projected[3][(i + 5) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 4) % 8] / self.projected[3][(i + 4) % 8]), (self.projected[1][(i + 4) % 8] / self.projected[3][(i + 4) % 8])), ((self.projected[0][(i + 7) % 8] / self.projected[3][(i + 7) % 8]), (self.projected[1][(i + 7) % 8] / self.projected[3][(i + 7) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 7) % 8] / self.projected[3][(i + 7) % 8]), (self.projected[1][(i + 7) % 8] / self.projected[3][(i + 7) % 8])), ((self.projected[0][(i + 6) % 8] / self.projected[3][(i + 6) % 8]), (self.projected[1][(i + 6) % 8] / self.projected[3][(i + 6) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 7) % 8] / self.projected[3][(i + 7) % 8]), (self.projected[1][(i + 7) % 8] / self.projected[3][(i + 7) % 8])), ((self.projected[0][(i + 3) % 8] / self.projected[3][(i + 3) % 8]), (self.projected[1][(i + 3) % 8] / self.projected[3][(i + 3) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 3) % 8] / self.projected[3][(i + 3) % 8]), (self.projected[1][(i + 3) % 8] / self.projected[3][(i + 3) % 8])), ((self.projected[0][(i + 2) % 8] / self.projected[3][(i + 2) % 8]), (self.projected[1][(i + 2) % 8] / self.projected[3][(i + 2) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 3) % 8] / self.projected[3][(i + 3) % 8]), (self.projected[1][(i + 3) % 8] / self.projected[3][(i + 3) % 8])), ((self.projected[0][(i + 0) % 8] / self.projected[3][(i + 0) % 8]), (self.projected[1][(i + 0) % 8] / self.projected[3][(i + 0) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 0) % 8] / self.projected[3][(i + 0) % 8]), (self.projected[1][(i + 0) % 8] / self.projected[3][(i + 0) % 8])), ((self.projected[0][(i + 1) % 8] / self.projected[3][(i + 1) % 8]), (self.projected[1][(i + 1) % 8] / self.projected[3][(i + 1) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 0) % 8] / self.projected[3][(i + 0) % 8]), (self.projected[1][(i + 0) % 8] / self.projected[3][(i + 0) % 8])), ((self.projected[0][(i + 4) % 8] / self.projected[3][(i + 4) % 8]), (self.projected[1][(i + 4) % 8] / self.projected[3][(i + 4) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 1) % 8] / self.projected[3][(i + 1) % 8]), (self.projected[1][(i + 1) % 8] / self.projected[3][(i + 1) % 8])), ((self.projected[0][(i + 5) % 8] / self.projected[3][(i + 5) % 8]), (self.projected[1][(i + 5) % 8] / self.projected[3][(i + 5) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 2) % 8] / self.projected[3][(i + 2) % 8]), (self.projected[1][(i + 2) % 8] / self.projected[3][(i + 2) % 8])), ((self.projected[0][(i + 6) % 8] / self.projected[3][(i + 6) % 8]), (self.projected[1][(i + 6) % 8] / self.projected[3][(i + 6) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 5) % 8] / self.projected[3][(i + 5) % 8]), (self.projected[1][(i + 5) % 8] / self.projected[3][(i + 5) % 8])), ((self.projected[0][(i + 4) % 8] / self.projected[3][(i + 4) % 8]), (self.projected[1][(i + 4) % 8] / self.projected[3][(i + 4) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 4) % 8] / self.projected[3][(i + 4) % 8]), (self.projected[1][(i + 4) % 8] / self.projected[3][(i + 4) % 8])), ((self.projected[0][(i + 6) % 8] / self.projected[3][(i + 6) % 8]), (self.projected[1][(i + 6) % 8] / self.projected[3][(i + 6) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 6) % 8] / self.projected[3][(i + 6) % 8]), (self.projected[1][(i + 6) % 8] / self.projected[3][(i + 6) % 8])), ((self.projected[0][(i + 7) % 8] / self.projected[3][(i + 7) % 8]), (self.projected[1][(i + 7) % 8] / self.projected[3][(i + 7) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 7) % 8] / self.projected[3][(i + 7) % 8]), (self.projected[1][(i + 7) % 8] / self.projected[3][(i + 7) % 8])), ((self.projected[0][(i + 5) % 8] / self.projected[3][(i + 5) % 8]), (self.projected[1][(i + 5) % 8] / self.projected[3][(i + 5) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 7) % 8] / self.projected[3][(i + 7) % 8]), (self.projected[1][(i + 7) % 8] / self.projected[3][(i + 7) % 8])), ((self.projected[0][(i + 3) % 8] / self.projected[3][(i + 3) % 8]), (self.projected[1][(i + 3) % 8] / self.projected[3][(i + 3) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 3) % 8] / self.projected[3][(i + 3) % 8]), (self.projected[1][(i + 3) % 8] / self.projected[3][(i + 3) % 8])), ((self.projected[0][(i + 2) % 8] / self.projected[3][(i + 2) % 8]), (self.projected[1][(i + 2) % 8] / self.projected[3][(i + 2) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 2) % 8] / self.projected[3][(i + 2) % 8]), (self.projected[1][(i + 2) % 8] / self.projected[3][(i + 2) % 8])), ((self.projected[0][(i + 0) % 8] / self.projected[3][(i + 0) % 8]), (self.projected[1][(i + 0) % 8] / self.projected[3][(i + 0) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 0) % 8] / self.projected[3][(i + 0) % 8]), (self.projected[1][(i + 0) % 8] / self.projected[3][(i + 0) % 8])), ((self.projected[0][(i + 1) % 8] / self.projected[3][(i + 1) % 8]), (self.projected[1][(i + 1) % 8] / self.projected[3][(i + 1) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 1) % 8] / self.projected[3][(i + 1) % 8]), (self.projected[1][(i + 1) % 8] / self.projected[3][(i + 1) % 8])), ((self.projected[0][(i + 3) % 8] / self.projected[3][(i + 3) % 8]), (self.projected[1][(i + 3) % 8] / self.projected[3][(i + 3) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 1) % 8] / self.projected[3][(i + 1) % 8]), (self.projected[1][(i + 1) % 8] / self.projected[3][(i + 1) % 8])), ((self.projected[0][(i + 5) % 8] / self.projected[3][(i + 5) % 8]), (self.projected[1][(i + 5) % 8] / self.projected[3][(i + 5) % 8])))
            pg.draw.line(self.screen, (255, 255, 255), ((self.projected[0][(i + 5) % 8] / self.projected[3][(i + 5) % 8]), (self.projected[1][(i + 5) % 8] / self.projected[3][(i + 5) % 8])), ((self.projected[0][(i + 4) % 8] / self.projected[3][(i + 4) % 8]), (self.projected[1][(i + 4) % 8] / self.projected[3][(i + 4) % 8])))


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
                    if event.key == K_d:
                        self.change_direction('right')
                    if event.key == K_a:
                        self.change_direction('left')
                    if event.key == K_w:
                        self.change_direction('up')
                    if event.key == K_s:
                        self.change_direction('down')

            pg.display.update()


