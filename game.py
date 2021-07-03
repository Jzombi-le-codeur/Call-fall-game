"""Importer les modules"""
import pygame #Importer la bibliothèque Pygame
import monster #Importer le module Monster
from monster import Monster #Importer le classe Monster
from player import Player #Importer la classe du joueur
from monster import Mummy #Importer la classe des momies
from monster import Alien #Importer la classe des aliens
from comet_event import CometFallEvent #Importer la classe des comètes
from sounds import SoundManager #Importer la classe des sons
from boss import Boss #Importer la classe du boss

pygame.init()

"""Définir la classe du jeu"""
class Game: #Créer la classe du jeu
    """Définir les attributs du jeu"""
    def __init__(self): #Créer le constructeur de la classe
        self.is_playing = False #Dire que le jeu n'as pas commencé
        self.end_game = False #Signaler que le jeu n'est pas terminé
        self.all_players = pygame.sprite.Group() #Créer le groupe du joueur
        self.player = Player(self) #Ajouter le joueur au jeu
        self.all_players.add(self.player) #Ajouter le joueur au groupe
        self.all_monsters = pygame.sprite.Group() #Créer le groupe des monstres
        self.pressed = {} #Définir le dictionnaire pour savoir si des touches sont pressées
        self.comet_event = CometFallEvent(self) #Stocker la classe des comètes
        self.score = 0 #Définir la score initial
        self.level = 10  #Définir le niveau initial
        self.life = 3  # Définir le nombre de vies global initial
        self.font = pygame.font.Font("assets/Righteous-Regular.ttf", 25)  # Créer la police du texte du score
        self.sound_manager = SoundManager() #Stocker la classe des sons
        self.all_boss = pygame.sprite.Group() #Créer le groupe du monstre
        self.boss = Boss(self) #Stocker la classe du boss
        self.projectile = True
        self.event = 1

    def spawn_monster(self, monster_name): #Définir la méthode pour faire spawner les monstres
        """Faire spawner les monstres"""
        self.all_monsters.add(monster_name.__call__(self)) #Ajouter des monstres au groupe

    def spawn_boss(self):
        self.all_boss.add(self.boss)  # Ajouter un boss au groupe de boss

    def start(self): #Méthode pour lancer le jeu
        self.is_playing = True #Lancer le jeu
        """Faire spawner les monstres en fonction du niveau"""
        if self.level == 1:  # Action s'exécutant si on est au niveau 1
            self.spawn_monster(Mummy)

        elif self.level == 2:  # Action s'exécutant si on est au niveau 2
            self.spawn_monster(Mummy)  # Faire apparaître une momie
            self.spawn_monster(Mummy)  # Faire apparaître un momie

        elif self.level == 3:  # Action s'exécutant si on est au niveau 3
            self.spawn_monster(Alien)  # Faire apparaître un alien


        elif self.level == 10:
            self.all_monsters = pygame.sprite.Group()
            self.spawn_boss()

        else:
            self.spawn_monster(Mummy)  # Faire apparaître un momie
            self.spawn_monster(Mummy)  # Faire apparaître un momie
            self.spawn_monster(Alien)  # Faire apparaître un alien

    def add_level(self): #Méthode pour changer de niveau
        self.level += 1 #Changer de niveau

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) #Vérifier les collisions

    def game_over(self): #Méthode pour réinitialiser le jeu
        if self.life <= 0:
            self.all_monsters = pygame.sprite.Group() #Supprimer tous les monstres
            self.player.health = self.player.max_health #Réinitialiser les vies du joueur
            self.is_playing = False #Afficher le menu du jeu
            self.comet_event.all_comets = pygame.sprite.Group() #Supprimer les comètes
            self.comet_event.reset_percent() #Réinitialiser le pourcentage
            self.score = 0 #Réinitialiser le score
            self.sound_manager.play("game_over") #Jouer le son du Game Over
            self.life = 3
            self.level = 1

    def block_projectile(self):
        print(self.comet_event.fall_mode)
        if self.boss.rect.x == 800:
            self.projectile = False

        elif self.boss.rect.x == 600:
            self.projectile = True

    def end(self):
        self.end_game = True #Signaler que le jeu est terminé
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


    def add_score(self, points): #Définir une méthode pour définir le nombre de points à ajouter au score
        self.score += points  #Ajouter des points au score

    def update(self, screen): #Mettre à jour le jeu quand il est lancé
        """Afficher le score sur l'écran"""
        score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0)) #Créer le texte du score
        level_text = self.font.render(f"Level: {self.level}", 1, (0, 0, 0))  # Créer le texte du niveau
        life_text = self.font.render(f"Lifes: {self.life}", 1, (0, 0, 0))  # Créer le texte des vies globales
        end_text = self.font.render("Congratulations ! You have completed the game !!!", 1, (0, 0, 0))  # Créer le texte des vies globales

        """Dessiner les éléments"""
        screen.blit(self.player.image, self.player.rect)  # Afficher le joueur sur la fenêtre
        self.player.all_projectiles.draw(screen)  # Dessiner les projectiles sur la fenêtre
        self.all_monsters.draw(screen)  # Afficher les monstres sur la fenêtre
        self.comet_event.all_comets.draw(screen)  # Dessiner sur la fenêtre les comètes
        if self.end_game is False:
            screen.blit(score_text, (20, 20))  # Dessiner le texte du score
            screen.blit(level_text, (20, 60))  # Dessiner le texte du niveau
            screen.blit(life_text, (20, 100))  # Dessiner le texte des vies globales

        elif self.end_game is True:
            screen.blit(end_text, (20, 20))  # Dessiner le texte de fin

        if self.level == 10:
            screen.blit(self.boss.image, self.boss.rect)  # Afficher le joueur sur la fenêtre

        """Actualiser les barres"""
        self.player.updade_health_bar(screen) #Actualiser la barre de vies du joueur
        self.comet_event.update_bar(screen) #Actualiser la barre des comètes
        self.player.update_animation() #Actualiser l'animation du joueur
        if self.level == 10:
            self.boss.update_health_bar(screen) #Actualiser la barre de vies du joueur

        """Déplacer les éléments"""
        """Déplacer le projectile"""
        for projectile in self.player.all_projectiles:  # Dans Projectile
            projectile.move()  # Faire déplacer les projectile

        for comet in self.comet_event.all_comets: #Dans les comètes
            comet.fall() #Faire tomber la pluie de comètes

        """Appeler les évènements d'action du boss"""
        self.boss.go_and_back()
        self.boss.fly()
        self.block_projectile()
        if self.boss.rect.x == 800:
            self.event += 1
            if (self.event % 2) == 0:
                self.spawn_monster(Mummy)

        """Récupérer les monstres dans le main"""
        for monster in self.all_monsters:  # Dans Projectile
            monster.forward()  # Faire déplacer les projectile
            monster.updade_health_bar(screen) # Dessiner la barre de vie sur la fenêtre
            monster.update_animation() #Mettre à jour les animations du monstre

        """Vérifier la direction du joueur"""
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():  # Vérifier
            # que la touche gauche est pressée et que le joueur ne dépasse pas la bordure
            # droite
            self.player.move_right()  # Déplacer le joueur à droite

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:  # Vérifier que la touche gauche est pressée et que
            # le joueur ne dépasse pas la bordure gauche
            self.player.move_left()  # Déplacer le joueur à gauche