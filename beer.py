import pygame
import random

class Beer(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/filou.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 480
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # Bruitage quand le monstre meurt
            self.game.bell_sound.play()
            # Suppression du monstre actuel et apparition d'un nouveau
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health
            # Si la bar d'événement chargée au max --> on ne fait plus apparaitre de monstre
            if self.game.pouf_event.is_full_loaded():
                self.game.all_beers.remove(self)
                # Déclencher la pluie
                self.game.pouf_event.attempt_fall()

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 50, self.rect.y - 20, self.health, 5]
        back_bar_position = [self.rect.x + 50, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # Déplacement seulement si pas de collision avec le teddy
        if not self.game.check_collision(self, self.game.all_teddys):
            self.rect.x -= self.velocity
        # Monstre en collision avec le joueur --> Dégat pour le joueur
        else:
            self.game.teddy.damage(self.attack)
