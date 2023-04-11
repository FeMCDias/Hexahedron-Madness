import pygame as pg
import Hexahedron
import os

def main():
    pg.init()
    screen = pg.display.set_mode((720, 600))
    pg.display.set_caption("Hexahedron Madness!")
    icon = pg.image.load(os.path.join('assets','images','cube_icon.jpg'))
    pg.display.set_icon(icon)
    music = pg.mixer.music.load(os.path.join('assets','music','Shape Da Future.mp3'))
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1)
    cube = Hexahedron.Cube(screen)
    cube.run()

if __name__ == "__main__":
    main()


