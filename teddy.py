import pygame
from projectile import Projectile

class Teddy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/teddy_bear.png')
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 450
        self.all_projectiles_right = pygame.sprite.Group()
        self.all_projectiles_left = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else: # le joueur n'a plus de point de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 80, self.rect.y + 5, self.health, 7]
        back_bar_position = [self.rect.x + 80, self.rect.y + 5, self.max_health, 7]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile_right(self):
        self.all_projectiles_right.add(Projectile(self))

    def launch_projectile_left(self):
        self.all_projectiles_left.add(Projectile(self))

    def move_right(self):
        # Mouvement seulement si pas de collision avec un group de sprite (beer)
        if not self.game.check_collision(self, self.game.all_beers):
            self.rect.x += self.velocity

    def move_left(self):
        # Mouvement seulement si pas de collision avec un group de sprite (beer)
        if not self.game.check_collision(self, self.game.all_guards):
            self.rect.x -= self.velocity