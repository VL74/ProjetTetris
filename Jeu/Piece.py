
from pygame.math import Vector3, Vector2

from Jeu.Figure import Figure
from Jeu.Terrain import Terrain


class Piece :
    level = 2
    state = "start"
    x = 100
    y = 60
    zoom = 20
    Terrain1 = Terrain()
    figure = None

    def __init__(self):
        self.state = "start"

    def new_figure(self):
        self.figure = Figure(3, 0)

    def descente_piece(self):
        while not self.Terrain.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def deplac_bas(self):
        self.figure.y += 1
        if self.Terrain1.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                pass
                #if i * 4 + j in self.figure.image():
                #    self.Terrain1.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.Terrain1.break_lines()
        self.new_figure()
        if self.Terrain1.intersects():
            self.state = "gameover"

    def deplac_horiz(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.Terrain1.intersects():
            self.figure.x = old_x

    def rotation(self):
        old_rotation = self.figure.rotation
        self.figure.rotation()
        if self.Terrain1.intersects():
            self.figure.rotation = old_rotation
