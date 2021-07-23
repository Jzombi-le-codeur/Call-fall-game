"""Importer les bibliothèques/modules"""
import pygame #Importer la bibliothèque Pygame
import random #Importer la bibliothèque Random
import time #Importer la bibliothèque Time

"""Définir la classe des comètes"""
class Comet(pygame.sprite.Sprite): #Créer la classe des comètes
    """Définir les attributs"""
    def __init__(self, comet_event): #Créer le constructeur
        super().__init__() #Dire à pygame que les comètes sont des éléments graphiques du jeu
        self.image = pygame.image.load("assets/comet.png") #Importer l'image des comètes
        self.rect = self.image.get_rect() #Demander la position des comètes
        self.velocity = random.randint(1, 3) #Définir la vitesse des comètes
        self.rect.x = random.randint(20, 1000)
        self.rect.y = - random.randint(0, 800) #Définir l'ordonnée des comètes
        self.comet_event = comet_event #Stocker le module de la barre des comètes

    """Définir les méthodes"""
    def remove(self): #Définir la méthode pour supprimer une comète
        self.comet_event.all_comets.remove(self) #Supprimer une comète
        self.comet_event.game.sound_manager.play_sound("meteorite")  # Jouer le son des météorites
        if len(self.comet_event.all_comets) == 0: #Action s'exécutant si il n'y a plus de comètes
            self.comet_event.reset_percent() #Réinitialiser la barre des comètes
            self.comet_event.game.start() #Faire apparaître les monstres
            if self.comet_event.game.infinite is False:
                if self.comet_event.game.level != 10:
                    self.comet_event.game.add_level()
                    self.comet_event.game.register()

    def fall(self): #Définir la méthode pour faire tomber les comètes
        if self.comet_event.game.paused is False:
            self.rect.y += self.velocity #Faire tomber les comètes
        """Supprimer une comète"""
        if self.rect.y >= 500: #Action s'exécutant si une comète touche le sol
            self.remove() #Appeler la méthode pour supprimer une comète
            """Faire apparaître les monstres"""
            if len(self.comet_event.all_comets) == 0: #Action s'exécutant si il n'y a plus de comètes
                self.comet_event.reset_percent() #Réinitialiser la barre des comètes
                self.comet_event.fall_mode = False #Désactiver la pluie de comètes
                self.comet_event.game.block_projectile()

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players): #Action s'exécutant si une comète touche le joueur
            self.remove() #Appeler la méthode pour supprimer une comète
            self.comet_event.game.player.damage(20) #Faire perdre au joueur 20 points de vies