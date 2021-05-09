"""Importer les bibliothèques/modules"""
import pygame #Importer la bibliothèque Pygame
from projectile import Projectile #Importer la classe du projectile

"""Définir la classe du joueur"""
class Player(pygame.sprite.Sprite): #Créer la classe du joueur
    """Définir les attributs"""
    def __init__(self, game): #Créer le constructeur de la classe
        super().__init__() #Dire à pygame que le joueur est un élément graphique du jeu
        self.game = game
        self.health = 100 #Définir le nombre de vies initial du joueur
        self.max_health = 100 #Définir le nombre maximum de vies du joueur
        self.attack = 10 #Définir les points d'attaque du joueur
        self.velocity = 5 #Définir la vitesse du joueur
        self.image = pygame.image.load("assets/player.png") #Charger l'image du joueur
        self.rect = self.image.get_rect() #Avoir la position du joueur
        self.rect.x = 400 #Définir l'abcisse du joueur
        self.rect.y = 500 #Définir l'ordonnée du joueur
        self.all_projectiles = pygame.sprite.Group()

    """Définir les méthodes"""
    def updade_health_bar(self, surface): #Méthode pour définir la barre de vies
        """Dessiner la barre de vie"""
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])  # Dessiner l'arrière-plan de la barre de vies
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7]) #Dessiner la barre de vies

    def damage(self, amount): #Méthode pour infliger des dégâts au joueur
        """Infliger des dégâts au joueur"""
        if self.health > amount: #Vérifier le nombre de vies
            self.health -= amount #Infliger des dégâts au joueur

        else: #Si le monstre n'a plus de vies
            self.game.game_over() #Afficher l'écran du Game Over

    def move_right(self): #Méthode pour déplacer le joueur à droite
        """Vérifier les collisions"""
        if not self.game.check_collision(self, self.game.all_monsters): #Vérifier les collisions
            """Fazire déplacer le joueur vers la droite"""
            self.rect.x += self.velocity #Déplacer le joueur à droite

    def move_left(self): #Méthode pour déplacer le joueur à gauche
        """Faire déplacer le joueur vers la gauche"""
        self.rect.x -= self.velocity #Déplacer le joueur à gauche

    def launch_projectile(self): #Méthode pour lancer des projectiles
        """Envoyer les projectiles"""
        self.all_projectiles.add(Projectile(self)) #Créer un nouveau projectile
