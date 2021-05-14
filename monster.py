"""Importer les bibiliothèques/modules"""
import pygame #Importer la bibliothèque Pygame
import random #Importer la bibliothèque Random
import animation #Importer le module animation

"""Définir la classe des monstres"""
class Monster(animation.AnimateSprite): #Créer la classe des monstres
    """Définir les attributs"""
    def __init__(self, game): #Créer le constructeur de la classe
        super().__init__("mummy") #Dire à pygame que les monstres sont des éléments graphiques du jeu
        self.game = game #Stocker la classe Game
        self.health = 100 #Définir le nombre de vies des monstres
        self.max_health = 100 #Définir le nombre de vies maximal des monstres
        self.attack = 0.3 #Définir les points d'attaque des joueurs
        self.velocity = random.randint(1, 3) #Définir la vitesse des monstres
        self.rect = self.image.get_rect() #Demander les positions des joueurs
        self.rect.x = 1000 + random.randint(0, 300) #Définir l'abcisse des monstres
        self.rect.y = 540 #Définir l'ordonée des monstres
        self.start_animation()

    """Définir les méthodes"""

    def update_animation(self):
        self.animate(loop=True)

    def updade_health_bar(self, surface): #Méthode pour définir la barre de vies
        """Dessiner la barre de vie"""
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])  # Dessiner l'arrière-plan de la barre de vies
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5]) #Dessiner la barre de vies

    def damage(self, amount): #Méthode pour infliger des dégâts aux monstres
        """Infliger des dégâts aux monstres"""
        self.health -= amount #Infliger des dégâts aux monstres
        if self.health <= 0: #Vérifier si l'entité est morte
            self.rect.x = 1000 + random.randint(0, 300)#Réinitialiser l'abcisse de l'entité
            self.velocity = random.randint(1, 3) #Changer la vitesse de l'entité
            self.health = self.max_health #Réinitialiser les vies de l'entité

            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def check_collision(self, sprite, group): #Méthode pour la collision du monstre
        """Vérifier les collisions"""
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) #Retourner les collisions

    def forward(self): #Définir la méthode pour faire marcher le joueur
        """Vérifier les collisions"""
        if not self.game.check_collision(self, self.game.all_players): #Vérifier les collisions
            """Faire déplacer vers la gauche les monstres"""
            self.rect.x -= self.velocity #Faire déplacer vers la gauche les monstres
        else: #Vérifier les collisions
            self.game.player.damage(self.attack)