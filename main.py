import pygame as pg
import Hexahedron
import os

def main():
    pg.init()
    screen = pg.display.set_mode((720, 600))
    pg.display.set_caption("Hexahedron Madness!")
    icon = pg.image.load(os.path.join('assets','images','cube_icon.jpg'))
    pg.display.set_icon(icon)
    cube = Hexahedron.Cube(screen)
    cube.run()

if __name__ == "__main__":
    main()


