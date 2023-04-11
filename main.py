import pygame as pg
import Hexahedron

def main():
    pg.init()
    screen = pg.display.set_mode((720, 600))
    pg.display.set_caption("3D Cube")
    cube = Hexahedron.Cube(screen)
    cube.run()

if __name__ == "__main__":
    main()


