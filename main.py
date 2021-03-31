import pygame


from Jeu.Figure import Figure
from Jeu.Joueur import Joueur
from Jeu.Piece import Piece
from Jeu.Terrain import Terrain

pygame.init()

colors = [
    (0, 0, 0),
    (120, 37, 220),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")


done = False
clock = pygame.time.Clock()
fps = 25
Piece = Piece()
Joueur1 = Joueur()
TerrainDeJeu = Terrain()
FigurePiece = Figure(10,20)
counter = 0

pressing_down = False

while not done:
    if Piece.figure is None:
        Piece.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // Piece.level // 2) == 0 or pressing_down:
        if Piece.state == "start":
            Piece.deplac_bas()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Piece.rotation()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                Piece.deplac_horiz(-1)
            if event.key == pygame.K_RIGHT:
                Piece.deplac_horiz(1)
            if event.key == pygame.K_SPACE:
                Piece.descente_piece()
            if event.key == pygame.K_ESCAPE:
                Piece.__init__()

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(WHITE)

    for i in range(TerrainDeJeu.hauteur):
        for j in range(TerrainDeJeu.longueur):
            pygame.draw.rect(screen, GRAY, [TerrainDeJeu.hauteur + Piece.zoom * j, TerrainDeJeu.longueur + Piece.zoom * i, Piece.zoom, Piece.zoom], 1)
            if TerrainDeJeu.field[i][j] > 0:
                pygame.draw.rect(screen, colors[TerrainDeJeu.field[i][j]],
                                 [TerrainDeJeu.hauteur + Piece.zoom * j + 1, TerrainDeJeu.longueur + Piece.zoom * i + 1, Piece.zoom - 2, Piece.zoom - 1])

    if Piece.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in Piece.figure.image():
                    pygame.draw.rect(screen, colors[Piece.figure.color],
                                     [TerrainDeJeu.hauteur + Piece.zoom * (j + Piece.figure.x) + 1,
                                      TerrainDeJeu.longueur + Piece.zoom * (i + Piece.figure.y) + 1,
                                      Piece.zoom - 2, Piece.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(Joueur1.score), True, BLACK)
    text_PieceDeJeu_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if Piece.state == "gameover":
        screen.blit(text_game_over1, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

if __name__ == "__main__":
    pass