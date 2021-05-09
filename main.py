"""Importer les bibliothèques/modules"""
from game import Game #Importer la classe du jeu
import pygame #Importer la bibliothèque pygame
import math #Importer la bibliothèque Math

"""Créer et personnaliser la fenêtre"""
pygame.display.set_caption("Call fall game") #Créer une fenêtre et définir son titre
screen = pygame.display.set_mode((1080, 720)) #Définir les dimensions de la fenêtre

"""Charger les éléments"""
background = pygame.image.load("assets/bg.jpg") #Charger l'arrière-plan
#Charger la bannière
banner = pygame.image.load("assets/banner.png") #Charger la bannière
banner = pygame.transform.scale(banner, (500, 500)) #Redimensionner la bannière
banner_rect = banner.get_rect() #Demander la position de la bannière
banner_rect.x = math.ceil(screen.get_width() / 4) #Définir l'abcisse de la bannière


#Charger le bouton
play_button = pygame.image.load("assets/button.png") #Charger le bouton
play_button = pygame.transform.scale(play_button, (400, 150)) #Redimensionner le bouton
play_button_rect = play_button.get_rect() #Demander la position du bouton
play_button_rect.x = math.ceil(screen.get_width() / 3.33) #Définir l'abcisse du bouton
play_button_rect.y = math.ceil(screen.get_height() / 2)
game = Game() #Charger le jeu

"""Définir la boucle du jeu"""
running = True #Lancer le jeu

while running: #Boucle tant que que le jeu est exécuté
    """Mettre les images sur la fenêtre"""
    screen.blit(background, (0, -200)) #Afficher l'arrière-plan sur la fenêtre

    """Vérifier si le jeu a commencé"""
    if game.is_playing:
        game.update(screen)

    else: #Vérifier si le jeu n'a pas commencé
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect) #Afficher la bannière

    pygame.display.flip() #Mettre à jour le jeu

    for event in pygame.event.get(): #Boucle d'évènements
        """Arrêter le jeu"""
        if event.type == pygame.QUIT: #Action s'exécutant si le jeu doit s'arrêter
            running = False #Stopper le jeu
            pygame.quit() #Fermer la fenêtre

        """Détecter une touche du clavier"""
        if event.type == pygame.KEYDOWN: #Action s'exécutant si une touche du clavier est pressée
            game.pressed[event.key] = True #Signaler qu'une touche est pressée
            """Détecter si la touche espace est pressée pour lancer le projectile"""
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False #Signaler qu'aucune touche n'est pressée

        elif event.type == pygame.MOUSEBUTTONDOWN: #Action s'exécutant si le clic gauche est pressé
            if play_button_rect.collidepoint(event.pos): #Action s'exécutant si la souris touche le bouton
                game.start() #Lancer le jeu
