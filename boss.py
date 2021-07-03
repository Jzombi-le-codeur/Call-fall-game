"""Importer les bibliothèques/modules"""
import random
import pygame #Importer la bibliothèque Pygame
import math #Importer la bibliothèque Math

"""Définir la classe du boss"""
class Boss(pygame.sprite.Sprite): #Créer la classe du boss
    """Définir le constructeur"""
    def __init__(self, game): #Créer le constructeur de la classe
        """Définir les attributs"""
        super().__init__() #Dire que cette classe sera un élément graphique du jeu
        self.game = game #Avoir la classe game dans cette classe
        self.health = 350 #Définir le nombre de vies initial du boss
        self.max_health = 350 #Définir le nombre de vies maximal du boss
        self.attack = 0.8 #Définir les points d'attaque du boss
        self.velocity = 200 #Définir la vitesse initiale du boss
        self.speed_move = 2.5 #Définir la vitesse de mouvement
        self.event = 0
        self.image = pygame.image.load("assets/boss.png")
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()  # Avoir la position du boss
        self.rect.x = 600  # Définir l'abcisse du boss
        self.init_x = 600 #Définir l'abcisse initiale du boss
        self.rect.y = 225  # Définir l'ordonnée du boss
        self.init_y = 225  # Définir l'abcisse initiale du boss
        self.moving_x = 0
        self.speed_moving_x = 2.5
        self.moving_y = 0
        self.speed_moving_y = 2.5

    """Définir les fonctions"""
    def damage(self, amount): #Définir la fonction pour infliger des dégâts au boss
        self.health -= amount #Enlever les points de vies du boss
        if self.health == 0: #Action s'exécutant si le boss n'a plus de vies
            self.game.end() #Dire que le jeu est terminé

    def go_and_back(self): #Définir la fonction pour faire bouger le boss
        if not self.game.check_collision(self, self.game.all_players): #Vérifier les collisions
            """Faire bouger le boss"""
            self.rect.x = self.init_x + self.velocity * math.sin(math.radians(self.moving_x))  # Définir le mouvement du boss
            self.moving_x += self.speed_moving_x  # Faire bouger le boss

        else: #Vérifier les collisions
            self.game.player.damage(self.attack) #Infliger des dégâts aux monstres

    def fly(self):  # Définir la fonction pour faire bouger le boss
        if not self.game.check_collision(self, self.game.all_players):  # Vérifier les collisions
            """"""
            self.rect.y = self.init_y + self.velocity * math.cos(math.radians(self.moving_y))  # Définir le mouvement du boss
            self.moving_y += self.speed_moving_y  # Faire bouger le boss

        else:  # Vérifier les collisions
            self.game.player.damage(self.attack)  # Infliger des dégâts aux monstres

    def update_health_bar(self, surface): #Créer la fonction pour actualiser la barre de vies
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 5]) #Créer l'arrière-plan de la barre de vies
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 20, self.health, 5]) #Créer la barre de vies