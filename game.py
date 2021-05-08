"""Importer les modules"""
import pygame #Importer la bibliothèque Pygame
from player import Player #Importer la classe du joueur
from monster import Monster #Importer la classe des monstres

"""Définir la classe du jeu"""
class Game: #Créer la classe du jeu
    """Définir les attributs du jeu"""
    def __init__(self): #Créer le constructeur de la classe
        self.all_players = pygame.sprite.Group() #Créer le groupe du joueur
        self.player = Player(self) #Ajouter le joueur au jeu
        self.all_players.add(self.player) #Ajouter le joueur au groupe
        self.all_monsters = pygame.sprite.Group() #Créer le groupe des monstres
        self.pressed = {} #Définir le dictionnaire pour savoir si des touches sont pressées
        self.spawn_monster() #Faire apparaître un monstre
        self.spawn_monster() #Faire apparaître un monstre

    def spawn_monster(self): #Définir la méthode pour faire spawner les monstres
        """Faire spawner les monstres"""
        monster = Monster(self) #Définir la variable monster
        self.all_monsters.add(monster) #Ajouter un monstre au groupe de monstres

    def check_collision(self, sprite, group):
        """Vérifier les collisions"""
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) #Vérifier les collisions