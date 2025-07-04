import pygame
import math
from game import Game

pygame.init()
pygame.mixer.init()

# Fenêtre du jeu
pygame.display.set_caption("Pouf Fall Game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('assets/bg_picasso.png')

# Zoom fort : plus grand que l'écran à cause des bords blancs
zoomed_width = 1400
zoomed_height = 1100
background = pygame.transform.scale(background, (zoomed_width, zoomed_height))

# Centrage horizontal
offset_x = -(zoomed_width - 1080) // 2

# Décalage vertical vers le haut (plus négatif = plus haut)
offset_y = -200

# Bouton "Start"
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.2 )
play_button_rect.y = math.ceil(screen.get_height() / 1.5 )

# Logo du jeu --> teddy
banner = pygame.image.load('assets/teddy_bear.png')
banner = pygame.transform.scale(banner, (450, 450))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.5 )
banner_rect.y = math.ceil(screen.get_height() / 6 )

# Chargement du jeu
game = Game()

running = True

clock = pygame.time.Clock() # car les sprites bougent trop vite à cause du FPS

# Boucle du jeu
while running:
    # Arrière-plan
    screen.blit(background, (offset_x, offset_y))

    # Vérifier si le jeu à commencer
    if game.is_playing:
        game.update(screen)
    else:
        # Écran de bienvenu
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    # MAJ écran
    pygame.display.flip()

    # Limite le framerate
    clock.tick(60)

    # Événement de l'utilisateur
    for event in pygame.event.get():
        # Fermeture de la fenetre par le joueur
        if event.type == pygame.QUIT:
            running = False
            print("Fermeture de la fenêtre de jeu")
            pygame.quit()

        # Détecter si le joueur lâche une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Lancement de projectile vers la droite
            if event.key == pygame.K_d:
                game.teddy.launch_projectile_right()

            # Lancement de projectile vers la gauche
            if event.key == pygame.K_q:
                game.teddy.launch_projectile_left()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # Click Start
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()