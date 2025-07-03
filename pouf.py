import pygame
import random

class Pouf(pygame.sprite.Sprite):
    def __init__(self, pouf_event):
        super().__init__()
        self.image = pygame.image.load('assets/pouf.png')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 5)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.pouf_event = pouf_event

    def remove(self):
        self.pouf_event.all_poufs.remove(self)

        # Si plus de poufs --> Reset la barre d'évènement + Réapparition des bieres
        if len(self.pouf_event.all_poufs) == 0:
            print("Fin de la pluie de pouf.")
            self.pouf_event.reset_percent()
            self.pouf_event.game.spawn_beer()
            self.pouf_event.game.spawn_beer()
            self.pouf_event.game.spawn_guard()

    def fall(self):
        self.rect.y += self.velocity

        # Tombe sur le sol
        if self.rect.y >= 550:
            self.remove()

            # Si plus de pouf
            if len(self.pouf_event.all_poufs) == 0:
                print("Fin de la pluie de pouf.")
                self.pouf_event.reset_percent()
                self.pouf_event.fall_mode = False

        # Collision avec le joueur
        if self.pouf_event.game.check_collision(self, self.pouf_event.game.all_teddys):
            self.remove()
            self.pouf_event.game.teddy.damage(10)