import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, teddy):
        super().__init__()
        self.velocity = 5
        self.teddy = teddy
        self.image = pygame.image.load('assets/ecocup.png')
        self.image= pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()
        self.rect.x = teddy.rect.x + 90
        self.rect.y = teddy.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove_right(self):
        self.teddy.all_projectiles_right.remove(self)

    def remove_left(self):
        self.teddy.all_projectiles_left.remove(self)

    def move_right(self):
        self.rect.x += self.velocity
        self.rotate()

        # Si collision avec un monstre --> Supression du projectile + dégâts
        for beer in self.teddy.game.check_collision(self, self.teddy.game.all_beers):
            self.remove_right()
            beer.damage(self.teddy.attack)

        # Suppression projectile s'il est hors de l'écran
        if self.rect.x > 1080:
            self.remove_right()

    def move_left(self):
        self.rect.x -= self.velocity
        self.rotate()

        # Si collision avec un monstre --> Supression du projectile + dégâts
        for guard in self.teddy.game.check_collision(self, self.teddy.game.all_guards):
            self.remove_left()
            guard.damage(self.teddy.attack)

        # Suppression projectile s'il est hors de l'écran
        if self.rect.x < -15 :
            self.remove_left()