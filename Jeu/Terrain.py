from pygame.math import Vector2

from Jeu.Figure import Figure
from Jeu.Joueur import Joueur


class Terrain :
    field = []
    Figure1 =Figure(10,20)
    Joueur1 = Joueur()
    def __init__(self):
        self.hauteur = 0
        self.longueur = 0
        self.field = []
        for i in range(self.hauteur):
            new_line = []
            for j in range(self.longueur):
                new_line.append(0)
            self.field.append(new_line)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.Figure1.image():
                    if i + self.Figure1.y > self.hauteur - 1 or \
                            j + self.Figure1.x > self.longueur - 1 or \
                            j + self.Figure1.x < 0 or \
                            self.field[i + self.Figure1.y][j + self.Figure1.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.hauteur):
            zeros = 0
            for j in range(self.longueur):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.longueur):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.Joueur1.score += lines ** 2