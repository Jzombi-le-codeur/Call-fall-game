"""Importer les modules"""
import pygame #Importer la bibliothèque Pygame
from player import Player #Importer la classe du joueur
import monster #Importer le module Monster
from monster import Monster #Importer le classe Monster
from monster import Mummy #Importer la classe des momies
from monster import Alien #Importer la classe des aliens
from comet_event import CometFallEvent #Importer la classe des comètes
from sounds import SoundManager #Importer la classe des sons
from boss import Boss #Importer la classe du boss
import json

pygame.init()

"""Définir la classe du jeu"""
class Game: #Créer la classe du jeu
    """Définir les attributs du jeu"""
    def __init__(self): #Créer le constructeur de la classe
        self.version = None
        self.is_playing = False #Dire que le jeu n'as pas commencé
        self.end_game = False #Signaler que le jeu n'est pas terminé
        self.all_players = pygame.sprite.Group() #Créer le groupe du joueur
        self.player = Player(self) #Ajouter le joueur au jeu
        self.all_players.add(self.player) #Ajouter le joueur au groupe
        self.all_monsters = pygame.sprite.Group() #Créer le groupe des monstres
        self.pressed = {} #Définir le dictionnaire pour savoir si des touches sont pressées
        self.comet_event = CometFallEvent(self) #Stocker la classe des comètes
        self.score = 0 #Définir la score initial
        self.font = pygame.font.Font("assets/Righteous-Regular.ttf", 25)  # Créer la police du texte du score
        self.sound_manager = SoundManager() #Stocker la classe des sons
        self.all_boss = pygame.sprite.Group()  # Créer le groupe du monstre
        self.boss = Boss(self)  # Stocker la classe du boss
        self.projectile = True
        self.event = 1
        self.paused = False
        self.end_text = self.font.render("Congratulations ! You have completed the game !!!", 1,(0, 0, 0))  # Créer le texte des vies globales
        self.general_data = {}
        self.infinite = False

    def register(self):
        if self.infinite is False and self.version >= 1.02:
            self.general_data["level"] = self.level
            self.general_data["lives"] = self.life
            with open("data.json", "w") as database:
                json.dump(self.general_data, database)

    def pause(self):
        if self.version >= 1.03:
            if self.paused is False:
                self.paused = True

            else:
                self.paused = False

    def recovback(self):
        if self.infinite is False and self.version >= 1.02:
            database = open("data.json").read()
            data = json.loads(database)
            self.level = data["level"]
            self.life = data["lives"]

        elif self.version >= 1.00 and self.version < 1.02:
            self.level = 1
            self.life = 3

        elif self.infinite or self.version < 1.00:
            self.level = ""
            self.life = 3

    def spawn_boss(self):
        self.all_boss.add(self.boss)  # Ajouter un boss au groupe de boss

    def spawn_monster(self, monster_name): #Définir la méthode pour faire spawner les monstres
        """Faire spawner les monstres"""
        self.all_monsters.add(monster_name.__call__(self)) #Ajouter des monstres au groupe

    def start(self): #Méthode pour lancer le jeu
        self.recovback()
        self.is_playing = True  # Lancer le jeu
        if self.infinite is False:
            """Faire spawner les monstres en fonction du niveau"""
            if self.level == 1:  # Action s'exécutant si on est au niveau 1
                self.spawn_monster(Mummy)

            elif self.level == 2:  # Action s'exécutant si on est au niveau 2
                self.spawn_monster(Mummy)  # Faire apparaître une momie
                self.spawn_monster(Mummy)  # Faire apparaître un momie

            elif self.level == 3:  # Action s'exécutant si on est au niveau 3
                self.spawn_monster(Alien)  # Faire apparaître un alien


            elif self.level == 10 and self.version >= 1.01:
                self.all_monsters = pygame.sprite.Group()
                self.spawn_boss()

            else:
                self.spawn_monster(Mummy)  # Faire apparaître un momie
                self.spawn_monster(Mummy)  # Faire apparaître un momie
                self.spawn_monster(Alien)  # Faire apparaître un alien

        else:
            self.spawn_monster(Mummy)  # Faire apparaître un momie
            self.spawn_monster(Mummy)  # Faire apparaître un momie
            self.spawn_monster(Alien)  # Faire apparaître un alien

    def game_over(self):  # Méthode pour réinitialiser le jeu
        if self.life <= 0:
            self.all_monsters = pygame.sprite.Group()  # Supprimer tous les monstres
            self.player.health = self.player.max_health  # Réinitialiser les vies du joueur
            self.is_playing = False  # Afficher le menu du jeu
            self.comet_event.all_comets = pygame.sprite.Group()  # Supprimer les comètes
            self.comet_event.reset_percent()  # Réinitialiser le pourcentage
            self.score = 0  # Réinitialiser le score
            self.sound_manager.play_sound("game_over")  # Jouer le son du Game Over
            self.life = 3
            self.level = 1

    def block_projectile(self):
        if self.boss.rect.x == 800:
            self.projectile = False

        elif self.boss.rect.x == 600:
            self.projectile = True

    def end(self):
        self.end_game = True  # Signaler que le jeu est terminé
        self.all_monsters = pygame.sprite.Group()  # Supprimer tous les monstres
        self.player.health = self.player.max_health  # Réinitialiser les vies du joueur
        self.comet_event.all_comets = pygame.sprite.Group()  # Supprimer les comètes
        self.comet_event.reset_percent()  # Réinitialiser le pourcentage

    def remove_life(self):
        self.life -= 1
        self.player.health = self.player.max_health  # Réinitialiser les vies du joueur
        self.comet_event.all_comets = pygame.sprite.Group()  # Supprimer les comètes
        self.comet_event.reset_percent()  # Réinitialiser le pourcentage
        self.all_monsters = pygame.sprite.Group()  # Supprimer tous les monstres
        self.comet_event.game.start()  # Faire apparaître les monstres
        self.player.rect.x = 400  # Définir l'abcisse du joueur

    def check_collision(self, sprite, group):
        """Vérifier les collisions"""
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) #Vérifier les collisions

    def game_over(self): #Méthode pour réinitialiser le jeu
        self.all_monsters = pygame.sprite.Group() #Supprimer tous les monstres
        self.player.health = self.player.max_health #Réinitialiser les vies du joueur
        self.is_playing = False #Afficher le menu du jeu
        self.comet_event.all_comets = pygame.sprite.Group() #Supprimer les comètes
        self.comet_event.reset_percent() #Réinitialiser le pourcentage
        self.score = 0 #Réinitialiser le score
        self.sound_manager.play_sound("game_over") #Jouer le son du Game Over
        self.level = 1
        self.life = 3

    def add_level(self):
        self.level += 1

    def add_score(self, points): #Définir une méthode pour définir le nombre de points à ajouter au score
        self.score += points  #Ajouter des points au score

    def update(self, screen): #Mettre à jour le jeu quand il est lancé
        """Afficher le score sur l'écran"""
        self.score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0))  # Créer le texte du score
        self.level_text = self.font.render(f"Level: {self.level}", 1, (0, 0, 0))  # Créer le texte du niveau
        self.life_text = self.font.render(f"Lifes: {self.life}", 1, (0, 0, 0))  # Créer le texte des vies globales

        """Dessiner les éléments"""
        screen.blit(self.player.image, self.player.rect)  # Afficher le joueur sur la fenêtre
        self.player.all_projectiles.draw(screen)  # Dessiner les projectiles sur la fenêtre
        self.all_monsters.draw(screen)  # Afficher les monstres sur la fenêtre
        self.comet_event.all_comets.draw(screen) #Dessiner sur la fenêtre les comètes
        if self.end_game is False:
            if self.infinite:
                screen.blit(self.score_text, (20, 20))  # Dessiner le texte du score
                screen.blit(self.life_text, (20, 60))  # Dessiner le texte des vies globales

            elif self.infinite is False:
                screen.blit(self.score_text, (20, 20))  # Dessiner le texte du score
                screen.blit(self.level_text, (20, 60))  # Dessiner le texte du niveau
                screen.blit(self.life_text, (20, 100))  # Dessiner le texte des vies globales

        if self.level == 10 and self.version >= 1.01:
            screen.blit(self.boss.image, self.boss.rect)  # Afficher le joueur sur la fenêtre

        """Actualiser les barres"""
        self.player.updade_health_bar(screen) # Actualiser la barre de vies du joueur
        self.comet_event.update_bar(screen) #Actualiser la barre des comètes
        self.player.update_animation() #Mettre à jour l'animation du joueur
        if self.level == 10:
            self.boss.update_health_bar(screen)  # Actualiser la barre de vies du joueur

        """Déplacer les éléments"""
        """Déplacer le projectile"""
        for projectile in self.player.all_projectiles:  # Dans Projectile
            projectile.move()  # Faire déplacer les projectile

        for comet in self.comet_event.all_comets: #Dans les comètes
            comet.fall() #Faire tomber la pluie de comètes

        """Appeler les évènements d'action du boss"""
        if self.level == 10 and self.version >= 1.01:
            self.boss.go_and_back()
            self.boss.fly()
            self.block_projectile()
            if self.boss.rect.x == 800:
                self.event += 1
                if (self.event % 2) == 0 and self.comet_event.fall_mode is False:
                    self.spawn_monster(Mummy)

        """Récupérer les monstres dans le main"""
        for monster in self.all_monsters:  # Dans Projectile
            monster.forward()  # Faire déplacer les projectile
            monster.updade_health_bar(screen) # Dessiner la barre de vie sur la fenêtre
            monster.update_animation() #Mettre à jour les animations du monstre

        """Vérifier la direction du joueur"""
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width() and self.paused is False:  # Vérifier
            # que la touche gauche est pressée et que le joueur ne dépasse pas la bordure
            # droite et que le jeu n'est pas en pause
            self.player.move_right()  # Si c'est le cas déplacer le joueur à droite

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0 and self.paused is False:  # Vérifier que la touche gauche est pressée, que
            #et que le joueur ne dépasse pas la bordure gauche
            self.player.move_left()  # Si c'est le cas déplacer le joueur à gauche