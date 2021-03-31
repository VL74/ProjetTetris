import pygame
import random

from Jeu.Joueur import Joueur
from Jeu.Tetris import Tetris

colors = [
    (0,255,255),
    (255,0,0),
    (0,255,0),
    (0,0,255),
    (255,168,0),
    (255,0,255),
    (255,255,0),
]

pygame.init()

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")

done = False
clock = pygame.time.Clock()
fps = 25
PieceTetris = Tetris(20, 10)
compteur = 0

pressing_down = False

print('Veuillez renseignes votre nom : ')
nom = input()
print(nom)

while not done:
    if PieceTetris.figure is None:
        PieceTetris.new_figure()
    compteur += 1
    if compteur > 100000:
        compteur = 0

    if compteur % (fps // PieceTetris.level // 2) == 0 or pressing_down:
        if PieceTetris.state == "start":
            PieceTetris.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PieceTetris.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                PieceTetris.go_side(-1)
            if event.key == pygame.K_RIGHT:
                PieceTetris.go_side(1)
            if event.key == pygame.K_SPACE:
                PieceTetris.go_space()
            if event.key == pygame.K_ESCAPE:
                PieceTetris.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(BLANC)

    for i in range(PieceTetris.hauteur):
        for j in range(PieceTetris.longueur):
            pygame.draw.rect(screen, NOIR, [PieceTetris.x + PieceTetris.zoom * j, PieceTetris.y + PieceTetris.zoom * i, PieceTetris.zoom, PieceTetris.zoom], 1)
            if PieceTetris.field[i][j] > 0:
                pygame.draw.rect(screen, colors[PieceTetris.field[i][j]],
                                 [PieceTetris.x + PieceTetris.zoom * j + 1, PieceTetris.y + PieceTetris.zoom * i + 1, PieceTetris.zoom - 2, PieceTetris.zoom - 1])

    if PieceTetris.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in PieceTetris.figure.image():
                    pygame.draw.rect(screen, colors[PieceTetris.figure.color],
                                     [PieceTetris.x + PieceTetris.zoom * (j + PieceTetris.figure.x) + 1,
                                      PieceTetris.y + PieceTetris.zoom * (i + PieceTetris.figure.y) + 1,
                                      PieceTetris.zoom - 2, PieceTetris.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    font3 = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render("Score: " + str(PieceTetris.Joueur1.score), True, NOIR)
    text2 = font2.render("level: " + str(PieceTetris.grab), True, GRIS)
    text3 = font3.render(str(nom),True,NOIR)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))
    text_game_over2 = font1.render("Score final " + str(PieceTetris.Joueur1.score_max), True, GRIS)

    screen.blit(text, [0, 100])
    screen.blit(text2, [0, 50])
    screen.blit(text3, [280,20])
    if PieceTetris.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])
        screen.blit(text_game_over2, [25, 330])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

