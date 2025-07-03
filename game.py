import pygame
from teddy import Teddy
from beer import Beer
from pouf_event import PoufFallEvent
from guard import Guard

class Game :
    def __init__(self):
        self.is_playing = False

        # Générer le joueur
        self.all_teddys = pygame.sprite.Group()
        self.teddy = Teddy(self)
        self.all_teddys.add(self.teddy)

        # Générer le groupe de monstre
        self.all_beers = pygame.sprite.Group()

        # Générer le groupe de guard
        self.all_guards = pygame.sprite.Group()

        # Générer l'évenement pluie de pouf
        self.pouf_event = PoufFallEvent(self)

        # Touches actionnées
        self.pressed = {}

        # Effets sonores
        self.bell_sound = pygame.mixer.Sound('assets/sounds/bell.wav')

    def start(self):
        self.is_playing = True
        self.spawn_beer()
        self.spawn_beer()
        self.spawn_guard()

    def game_over(self):
        # MAJ des variables du jeu
        self.all_beers = pygame.sprite.Group()
        self.all_guards = pygame.sprite.Group()
        self.teddy.health = self.teddy.max_health
        self.teddy.rect.x = 420
        self.pouf_event.all_poufs = pygame.sprite.Group()
        self.pouf_event.reset_percent()
        self.is_playing = False
        pygame.mixer.music.stop()

    def update(self, screen):
        # Affichage du joueur
        screen.blit(self.teddy.image, self.teddy.rect)

        # Affichage de la bare de vie du joueur
        self.teddy.update_health_bar(screen)

        # Affichage bare d'évènement
        self.pouf_event.update_bar(screen)

        # Affichage projectiles droits
        for projectile in self.teddy.all_projectiles_right:
            projectile.move_right()
        self.teddy.all_projectiles_right.draw(screen)

        # Affichage projectiles gauche
        for projectile in self.teddy.all_projectiles_left:
            projectile.move_left()
        self.teddy.all_projectiles_left.draw(screen)

        # Affichage des bieres
        for beer in self.all_beers:
            beer.forward()
            beer.update_health_bar(screen)
        self.all_beers.draw(screen)

        # Affichage des guards
        for guard in self.all_guards:
            guard.forward()
            guard.update_health_bar(screen)
        self.all_guards.draw(screen)

        # Affichage de la pluie de poufs
        for pouf in self.pouf_event.all_poufs:
            pouf.fall()
        self.pouf_event.all_poufs.draw(screen)

        # Déplacement du joueur
        if self.pressed.get(pygame.K_LEFT) and self.teddy.rect.x > 0:
            self.teddy.move_left()
        elif self.pressed.get(
                pygame.K_RIGHT) and self.teddy.rect.x + self.teddy.image.get_width() < screen.get_width():
            self.teddy.move_right()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_beer(self):
        beer = Beer(self)
        self.all_beers.add(beer)

    def spawn_guard(self):
        guard = Guard(self)
        self.all_guards.add(guard)