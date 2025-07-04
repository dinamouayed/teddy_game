import pygame
import random

class Guard(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/keep_the_beers.png')
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = - random.randint(-200, 300)
        self.rect.y = 425
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # Suppression des guards actuel et apparition d'un nouveau
            self.rect.x = - random.randint(0, 300)
            self.velocity = random.randint(1, 4)
            self.health = self.max_health
            # Si la bar d'événement chargée au max --> on ne fait plus apparaitre de guard
            if self.game.pouf_event.is_full_loaded():
                self.game.all_guards.remove(self)
                # Déclencher la pluie
                self.game.pouf_event.attempt_fall()

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 90, self.rect.y - 20, self.health, 5]
        back_bar_position = [self.rect.x + 90, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # Déplacement seulement si pas de collision avec le teddy
        if not self.game.check_collision(self, self.game.all_teddys):
            self.rect.x += self.velocity
        # Guard en collision avec le joueur --> Dégat pour le joueur
        else:
            self.game.teddy.damage(self.attack)
