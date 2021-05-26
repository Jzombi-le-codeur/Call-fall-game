"""Importer les bibiliothèques/modules"""
import pygame #Importer la bibliothèque Pygame
import random #Importer la bibliothèque Random
import animation #Importer le module animation

"""Définir la classe des monstres"""
class Monster(animation.AnimateSprite): #Créer la classe des monstres
    """Définir les attributs"""
    def __init__(self, game, name, size, offset=0): #Créer le constructeur de la classe
        super().__init__(name, size) #Dire à pygame que les monstres sont des éléments graphiques du jeu
        self.game = game #Stocker la classe Game
        self.health = 100 #Définir le nombre de vies des monstres
        self.max_health = 100 #Définir le nombre de vies maximal des monstres
        self.attack = 0.3 #Définir les points d'attaque des joueurs
        self.rect = self.image.get_rect() #Demander les positions des joueurs
        self.rect.x = 1000 + random.randint(0, 300) #Définir l'abcisse des monstres
        self.rect.y = 540 - offset #Définir l'ordonée des monstres
        self.start_animation() #Démarrer l'animation
        self.loot_amount = 10 #Définir le nombre de points par défaut à ajouter au score

    """Définir les méthodes"""
    def set_speed(self, speed): #Définir la méthode pour définir les vitesses des sprites
        self.default_speed = speed #Définir la vitesse par défaut
        self.velocity = random.randint(1, self.default_speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def update_animation(self): #Définir la méthode pour mettre à jour l'animation
        self.animate(loop=True) #Activer l'animation

    def updade_health_bar(self, surface): #Méthode pour définir la barre de vies
        """Dessiner la barre de vie"""
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])  # Dessiner l'arrière-plan de la barre de vies
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5]) #Dessiner la barre de vies

    def damage(self, amount): #Méthode pour infliger des dégâts aux monstres
        """Infliger des dégâts aux monstres"""
        self.health -= amount #Infliger des dégâts aux monstres
        if self.health <= 0: #Vérifier si l'entité est morte
            self.rect.x = 1000 + random.randint(0, 300)#Réinitialiser l'abcisse de l'entité
            self.health = self.max_health #Réinitialiser les vies de l'entité
            self.game.add_score(self.loot_amount) #Ajouter des points au score
            """Quand la barre est chargée"""
            if self.game.comet_event.is_full_loaded(): #Action s'exécutant si la barre est chargée
                self.game.all_monsters.remove(self) #Supprimer un monstre
                self.game.comet_event.attempt_fall() #Lancer la pluie de comètes

    def check_collision(self, sprite, group): #Méthode pour la collision du monstre
        """Vérifier les collisions"""
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) #Retourner les collisions

    def forward(self): #Définir la méthode pour faire marcher le joueur
        """Vérifier les collisions"""
        if not self.game.check_collision(self, self.game.all_players): #Vérifier les collisions
            """Faire déplacer vers la gauche les monstres"""
            self.rect.x -= self.velocity #Faire déplacer vers la gauche les monstres
        else: #Vérifier les collisions
            self.game.player.damage(self.attack) #Infliger des dégâts aux monstres


"""Définir les classes des monstres"""
"""Définir la classe des momies"""
class Mummy(Monster): #Créer la classe des mommies
    """Définir les attributs"""
    def __init__(self, game): #Définir les infos des momies
        super().__init__(game, "mummy", (130, 130)) #Définir les infos des momies
        self.set_loot_amount(20) #Ajouter 20 points au score
        self.set_speed(3)  # Définir la vitesse des momies


"""Définir la classe de l'alien"""
class Alien(Monster): #Créer la classe de l'alien
    """Définir les attributs"""
    def __init__(self, game): #Définir le constructeur de l'alien
        super().__init__(game, "alien", (300, 300), 130) #Définir les informations de l'alien
        self.health = 250 #Définir le nombre de vies initiales de l'alien
        self.max_health = 250 #Définir le nombre de vies maximal de l'alien
        self.attack = 0.8 #Définir les points d'attaque de l'alien
        self.set_speed(1) #Définir la vitesse de l'alien
        self.set_loot_amount(80)  # Ajouter 80 points au score