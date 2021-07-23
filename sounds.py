import pygame  # Importer la bibliothèque Pygame

"""Définir la classe des sons"""


class SoundManager:  # Créer la classe des sons
    """Définir les attributs"""

    def __init__(self):  # Définir le constructeur
        self.sounds = {  # Importer les sons
            'click': pygame.mixer.Sound("assets/sounds/click.ogg"),  # Importer le son du clic
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),  # Importer le son du game over
            'meteorite': pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
            # Importer le son de la chute des météorites
            'tir': pygame.mixer.Sound("assets/sounds/tir.ogg"),  # Importer le son du tir

        }
        self.sound = True

    """Définir les méthodes"""

    def play_sound(self, name):  # Définir la méthode pour jouer les sons
        if self.sound:
            self.sounds[name].play()  # Jouer les sons