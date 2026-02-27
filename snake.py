import pygame
import sys

# --- Initialisation ---
pygame.init()

# --- Paramètres ---
WIDTH  = 600
HEIGHT = 600
CELL   = 20          # chaque case fait 20x20 pixels
COLS   = WIDTH  // CELL   # 30 colonnes
ROWS   = HEIGHT // CELL   # 30 lignes

# --- Couleurs ---
BLACK      = (0,   0,   0)
GREEN      = (0,   200, 0)
DARK_GREEN = (0,   150, 0)

# --- Fenêtre ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake 🐍")
clock  = pygame.time.Clock()
FPS    = 60

# =====================
#   SERPENT
# =====================
# Le serpent = liste de cases (colonne, ligne)
snake = [(10, 10), (9, 10), (8, 10)]  # 3 cases, tête en (10,10)

# Direction actuelle : (1,0) = droite, (-1,0) = gauche
#                      (0,1) = bas,    (0,-1) = haut
direction = (1, 0)  # part vers la droite

# Vitesse du serpent : il bouge toutes les X millisecondes
SNAKE_SPEED  = 150        # ms entre chaque mouvement
last_move_time = 0        # mémorise le dernier moment où il a bougé


def draw_snake(surface, snake):
    """Dessine chaque case du serpent."""
    for i, (col, row) in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN   # tête plus claire
        rect  = pygame.Rect(col * CELL, row * CELL, CELL, CELL)
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)  # contour noir (1px)


def move_snake(snake, direction):
    """Calcule la nouvelle position et déplace le serpent."""
    head_col, head_row = snake[0]           # position de la tête
    dc, dr = direction                      # delta colonne, delta ligne
    new_head = (head_col + dc, head_row + dr)  # nouvelle tête

    snake.insert(0, new_head)   # ajoute la nouvelle tête au début
    snake.pop()                 # supprime la dernière case (la queue)


# =====================
#   BOUCLE PRINCIPALE
# =====================
running = True
while running:

    now = pygame.time.get_ticks()  # temps actuel en millisecondes

    # 1. ÉVÉNEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Changer de direction avec les flèches
            # (on empêche de faire demi-tour)
            if event.key == pygame.K_UP    and direction != (0,  1):
                direction = (0, -1)
            if event.key == pygame.K_DOWN  and direction != (0, -1):
                direction = (0,  1)
            if event.key == pygame.K_LEFT  and direction != (1,  0):
                direction = (-1, 0)
            if event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1,  0)

    # 2. MISE À JOUR
    # Le serpent ne bouge pas à chaque frame, seulement toutes les SNAKE_SPEED ms
    if now - last_move_time >= SNAKE_SPEED:
        move_snake(snake, direction)
        last_move_time = now

    # 3. RENDU
    screen.fill(BLACK)
    draw_snake(screen, snake)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()