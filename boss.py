"""Importer les bibliothèques/modules"""
import pygame #Importer la bibliothèque Pygame
import animation #Importer le module de l'animation

"""Définir la classe du boss"""
class Boss(pygame.sprite.Sprite): #Créer la classe du boss
    """Définir le constructeur"""
    def __init__(self, game): #Créer le constructeur de la classe
        """Définir les attributs"""
        super().__init__() #Dire que cette classe sera un élément graphique du jeu
        self.game = game #Avoir la classe game dans cette classe
        self.health = 350 #Définir le nombre de vies initial du boss
        self.max_health = 350 #Définir le nombre de vies maximal du boss
        self.attack = 1 #Définir les points d'attaque du boss
        self.velocity = 3 #Définir la vitesse du boss
        self.image = pygame.image.load("assets/boss/boss1.png") #Importer l'image du boss
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()  # Avoir la position du boss
        self.rect.x = 700  # Définir l'abcisse du boss
        self.rect.y = 400  # Définir l'ordonnée du boss

    """Définir les fonctions"""
    def move_right(self): #Créer la fonction pour bouger à droite
        self.rect.x += self.velocity #Faire bouger le boss à droite

    def move_left(self):  # Créer la fonction pour bouger à gauche
        self.rect.x -= self.velocity  # Faire bouger le boss à gauche

    def damage(self, amount): #Créer la fonction pour infliger des dégâts au boss
        self.health -= amount
        if self.health == 0:
            self.game.end()


    def update_health_bar(self, surface): #Créer la fonction pour actualiser la barre de vies
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 5]) #Créer l'arrière-plan de la barre de vies
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 20, self.health, 5]) #Créer la barre de vies