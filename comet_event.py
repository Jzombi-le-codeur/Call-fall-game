"""Importer les bibliothèques/modules"""
import pygame #Importer la bibliothèque Pygame
from comet import Comet #Importer la classe des comètes

"""Définir la classe de la barre des comètes"""
class CometFallEvent: #Créer la classe de la barre des comètes
    """Définir les attributs"""
    def __init__(self, game): #Créer le constructeur
        self.percent = 0 #Définir le pourcentage initial
        self.percent_speed = 33 #DDéfinir l'augmentation de la vitesse pourcentage de la barre
        self.all_comets = pygame.sprite.Group() #Créer le groupe des comètes
        self.game = game #Stocker la classe Game
        self.fall_mode = False #Ne pas mettre les météorites au départ

    """Définir les méthodes"""
    def add_percent(self): #Définir la méthode pour ajouter du pourcentage à la barre
        self.percent += self.percent_speed / 100 #Ajouter du pourcentage à la barre

    def is_full_loaded(self): #Définir la méthode pour signaler que la barre est remplie
        return self.percent >= 100 #Signaler que la barre est remplie

    def reset_percent(self): #Définir la méthode pour réinitialiser la barre
        self.percent = 0 #Réinitialiser la barre

    def meteor_fall(self): #Définir la méthode pour faire tomber la pluie de comètes
        """Faire tomber la pluie de 10 comètes"""
        if self.game.paused is False:
            if self.game.level == 1:  # Action s'exécutant si le niveau est à 1
                for i in range(1, 11):  # Répéter 10 fois l'action suivante
                    self.all_comets.add(Comet(self))  # Ajouter une comète au groupe

            elif self.game.level == 2:  # Action s'exécutant si le niveau est à 2
                for i in range(1, 13):  # Répéter 12 fois l'action suivante
                    self.all_comets.add(Comet(self))  # Ajouter une comète au groupe

            elif self.game.level == 3:  # Action s'exécutant si le niveau est à 3
                for i in range(1, 16):  # Répéter 15 fois l'action suivante
                    self.all_comets.add(Comet(self))  # Ajouter une comète au groupe

            elif self.game.level == 10:
                for i in range(1, 10):
                    self.all_comets.add(Comet(self))

            else:  # Action s'exécutant si le niveau est au moins à 4 mais n'atteint pas le niveau 10
                for i in range(1, 21):  # Répéter 20 fois l'action suivante
                    self.all_comets.add(Comet(self))  # Ajouter une comète au groupe

    def attempt_fall(self): #Définir la méthode pour activer la pluie de comètes
        """Activer la pluie de comètes"""
        if self.is_full_loaded() and len(self.game.all_monsters) == 0: #Action s'exécutant si la barre est remplie et qu'il n'y a plus de monstres
            self.meteor_fall() #Appeler la méthode pour faire tomber la pluie de comètes
            self.fall_mode = True #Activer la pluie de comètes

    def update_bar(self, surface): #Définir la méthode pour mettre à jour la barre
        if self.game.paused is False:
            self.add_percent() #Appeler la méthode pour ajouter du pourcentage

        """Définir la barre"""
        """Créer la barre d'arrière-plan"""
        pygame.draw.rect(surface, (0, 0, 0), [ #Définir la couleur de l'arrière-plan de la barre
            0, #Définir l'abcisse de l'arrière-plan de la barre
            surface.get_height() - 20, #Définir l'ordonnée de l'arrière-plan de la barre
            surface.get_width(), #Définir la longueur de l'arrière-plan de la barre
            10 #Définir l'épaisseur de l'arrière-plan de la barre
        ])

        """Créer la barre"""
        pygame.draw.rect(surface, (187, 11, 11), [ #Définir la couleur  de la barre
            0, #Définir l'abcisse de la barre
            surface.get_height() - 20, #Définir l'ordonnée de la barre
            (surface.get_width() / 100) * self.percent, #Définir la longueur de la barre
            10 #Définir l'épaisseur de la barre
        ])