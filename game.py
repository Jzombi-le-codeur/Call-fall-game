"""Importer les modules"""
import pygame #Importer la bibliothèque Pygame
from player import Player #Importer la classe du joueur
from monster import Mummy #Importer la classe des momies
from monster import Alien #Importer la classe des aliens
from comet_event import CometFallEvent

"""Définir la classe du jeu"""
class Game: #Créer la classe du jeu
    """Définir les attributs du jeu"""
    def __init__(self): #Créer le constructeur de la classe
        self.is_playing = False #Dire que le jeu n'as pas commencé
        self.all_players = pygame.sprite.Group() #Créer le groupe du joueur
        self.player = Player(self) #Ajouter le joueur au jeu
        self.all_players.add(self.player) #Ajouter le joueur au groupe
        self.all_monsters = pygame.sprite.Group() #Créer le groupe des monstres
        self.pressed = {} #Définir le dictionnaire pour savoir si des touches sont pressées
        self.comet_event = CometFallEvent(self)

    def spawn_monster(self, monster_name): #Définir la méthode pour faire spawner les monstres
        """Faire spawner les monstres"""
        self.all_monsters.add(monster_name.__call__(self)) #Ajouter des monstres au groupe

    def start(self): #Méthode pour lancer le jeu
        self.is_playing = True
        self.spawn_monster(Mummy) #Faire apparaître un momie
        self.spawn_monster(Mummy) #Faire apparaître une momie
        self.spawn_monster(Alien) #Faire apparaître un alien

    def check_collision(self, sprite, group):
        """Vérifier les collisions"""
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) #Vérifier les collisions

    def game_over(self): #Méthode pour réinitialiser le jeu
        self.all_monsters = pygame.sprite.Group() #Supprimer tous les monstres
        self.player.health = self.player.max_health #Réinitialiser les vies du joueur
        self.is_playing = False #Afficher le menu du jeu
        self.comet_event.all_comets = pygame.sprite.Group() #Supprimer les comètes
        self.comet_event.reset_percent() #Réinitialiser le pourcentage

    def update(self, screen): #Mettre à jour le jeu quand il est lancé
        screen.blit(self.player.image, self.player.rect)  # Afficher le joueur sur la fenêtre
        self.player.all_projectiles.draw(screen)  # Dessiner les projectiles sur la fenêtre
        self.all_monsters.draw(screen)  # Afficher les monstres sur la fenêtre
        self.comet_event.all_comets.draw(screen) #Dessiner sur la fenêtre les comètes

        """Actualiser les barres"""
        self.player.updade_health_bar(screen) # Actualiser la barre de vies du joueur
        self.comet_event.update_bar(screen) #Actualiser la barre des comètes
        self.player.update_animation() #Mettre à jour l'animation du joueur

        """Déplacer les éléments"""
        """Déplacer le projectile"""
        for projectile in self.player.all_projectiles:  # Dans Projectile
            projectile.move()  # Faire déplacer les projectile

        for comet in self.comet_event.all_comets: #Dans les comètes
            comet.fall() #Faire tomber la pluie de comètes


        """Récupérer les monstres dans le main"""
        for monster in self.all_monsters:  # Dans Projectile
            monster.forward()  # Faire déplacer les projectile
            monster.updade_health_bar(screen) # Dessiner la barre de vie sur la fenêtre
            monster.update_animation() #Mettre à jour les animations du monstre

        """Vérifier la direction du joueur"""
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():  # Vérifier
            # que la touche gauche est pressée et que le joueur ne dépasse pas la bordure
            # droite
            self.player.move_right()  # Si c'est le cas déplacer le joueur à droite

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:  # Vérifier que la touche gauche est pressée et que
            # le joueur ne dépasse pas la bordure gauche
            self.player.move_left()  # Si c'est le cas déplacer le joueur à gauche