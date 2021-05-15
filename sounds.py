"""Importer les bibliothèques/modules"""
import pygame #Importer la bibliothèque Pygame

"""Définir la classe des sons"""
class SoundManager: #Créer la classe des sons
    def __init__(self): #Créer le constructeur de la classe
        self.sounds = { #Définir le dictionnaire stockant les sons
            "click": pygame.mixer.Sound("assets/sounds/click.ogg"), #Importer le sons du Clic
            "game_over": pygame.mixer.Sound("assets/sounds/game_over.ogg"), #Importer le sons du Game Over
            "meteorite": pygame.mixer.Sound("assets/sounds/meteorite.ogg"), #Importer le sons des météorites
            "tir": pygame.mixer.Sound("assets/sounds/tir.ogg"), #Importer le sons du tir
        }

    def play(self, name): #Définir la méthode pour jouer des sons
        self.sounds[name].play() #Jouer les sons