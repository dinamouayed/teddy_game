import pygame
from pouf import Pouf

class PoufFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 12
        self.all_poufs = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, 10):
            self.all_poufs.add(Pouf(self))

    def attempt_fall(self):
        # La jauge d'événement est totalement chargée + plus de guard/biere --> pluie de pouf
        if self.is_full_loaded() and len(self.game.all_beers) == 0:
            # Lancement de la musique de l'évènement
            pygame.mixer.music.load('assets/sounds/triviata.wav')
            pygame.mixer.music.play(-1, start=2.5) # -1 pour que ça soit une boucle infini + on commence le son à partir de la seconde 2.5

            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):
        # Ajout pourcentage à la barre
        self.add_percent()

        # Barre arrière plan
        pygame.draw.rect(surface, (0,0,0), [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            10
        ])

        # Barre premier plan
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10
        ])