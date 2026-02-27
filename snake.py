import pygame
import sys

# --- Initialisation ---
pygame.init()  # Démarre tous les modules pygame

# --- Paramètres de la fenêtre ---
WIDTH  = 600   # largeur en pixels
HEIGHT = 600   # hauteur en pixels
CELL   = 20    # taille d'une case (le serpent se déplace case par case)

# --- Couleurs (Rouge, Vert, Bleu) ---
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

# --- Création de la fenêtre ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake 🐍")

# --- Horloge (pour contrôler la vitesse) ---
clock = pygame.time.Clock()
FPS = 60  # images par seconde

# =====================
#   BOUCLE PRINCIPALE
# =====================
running = True
while running:

    # 1. ÉVÉNEMENTS — ce que l'utilisateur fait
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # clic sur la croix
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # touche Échap
                running = False

    # 2. MISE À JOUR — la logique du jeu (vide pour l'instant)

    # 3. RENDU — ce qu'on affiche
    screen.fill(BLACK)           # efface l'écran avec du noir
    pygame.display.flip()        # envoie l'image à l'écran

    clock.tick(FPS)              # limite à 60 FPS

# --- Nettoyage ---
pygame.quit()
sys.exit()