"""Importer les bibliothèques/modules"""
from functools import partial
from tkinter import *
from game import Game #Importer la classe du jeu
import pygame #Importer la bibliothèque pygame
import math #Importer la bibliothèque Math
import sys

game = Game()#Charger le jeu

def launch(version):
    game.version = version
    launcher.destroy()

"""Définir le launcher"""
launcher = Tk()

launcher.title("Launcher")
launcher.geometry("500x500")
launcher.resizable(False, False)
launcher.iconbitmap("assets/launcher.ico")
launcher.protocol("WM_DELETE_WINDOW", sys.exit)

menu = Menu(launcher)
versions = Menu(menu, tearoff=0)
versions.add_command(label="Last version (1.1.0)", command=partial(launch, 1.10))
"""Sound update"""
versions.add_command(label="1.1.0", command=partial(launch, 1.10))  # Option Mute
"""Game update"""
versions.add_command(label="1.0 (Final Version)", command=partial(launch, 1.04))  # Dernière version 1.0
versions.add_command(label="1.0.3", command=partial(launch, 1.04))  # Mode infini
versions.add_command(label="1.0.3", command=partial(launch, 1.03))  # Pause
versions.add_command(label="1.0.2", command=partial(launch, 1.02))  # Sauvegardes
versions.add_command(label="1.0.1", command=partial(launch, 1.01))  # Boss
versions.add_command(label="1.0.0", command=partial(launch, 1.00))  # Système niveaux
menu.add_cascade(label="Versions", menu=versions)
launcher.config(menu=menu)

launcher.mainloop()

"""Définir une clock"""
clock = pygame.time.Clock() #Définir la clock
FPS = 60 #Définir le nombre de fps

"""Créer et personnaliser la fenêtre"""
pygame.display.set_caption("Call fall game") #Créer une fenêtre et définir son titre
screen = pygame.display.set_mode((1080, 720)) #Définir les dimensions de la fenêtre
logo = pygame.image.load("assets/projectile.png")  # Charger le logo
pygame.display.set_icon(logo)  # Appliquer le logo

"""Charger les éléments"""
background = pygame.image.load("assets/bg.jpg") #Charger l'arrière-plan
#Charger la bannière
banner = pygame.image.load("assets/banner.png") #Charger la bannière
banner = pygame.transform.scale(banner, (500, 500)) #Redimensionner la bannière
banner_rect = banner.get_rect() #Demander la position de la bannière
banner_rect.x = math.ceil(screen.get_width() / 4) #Définir l'abcisse de la bannière

"""Charger le bouton"""
play_button = pygame.image.load("assets/button.png") #Charger le bouton
play_button = pygame.transform.scale(play_button, (400, 150)) #Redimensionner le bouton
play_button_rect = play_button.get_rect() #Demander la position du bouton
play_button_rect.x = math.ceil(screen.get_width() / 3.33) #Définir l'abcisse du bouton
play_button_rect.y = math.ceil(screen.get_height() / 2)

play2_button = pygame.image.load("assets/Infini.png") #Charger le bouton
play2_button = pygame.transform.scale(play2_button, (400, 150)) #Redimensionner le bouton
play2_button_rect = play2_button.get_rect() #Demander la position du bouton
play2_button_rect.x = math.ceil(screen.get_width() / 3.33) #Définir l'abcisse du bouton
play2_button_rect.y = 500

"""Définir la boucle du jeu"""
running = True #Lancer le jeu

while running: #Boucle tant que que le jeu est exécuté
    """Mettre les images sur la fenêtre"""
    screen.blit(background, (0, -200)) #Afficher l'arrière-plan sur la fenêtre
    if game.end_game is True:
        if game.version >= 1.11:
            screen.blit(game.end_text, (225, 20))

    """Vérifier si le jeu a commencé"""
    if game.is_playing and game.end_game is False:
        game.update(screen)

    elif game.is_playing and game.end_game:
        if game.version >= 1.11:
            game.end()

    elif game.is_playing is False and game.end_game is False: #Vérifier si le jeu n'a pas commencé
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)  # Afficher la bannière
        if game.version >= 1.04:
            screen.blit(play2_button, play2_button_rect)


    pygame.display.flip() #Mettre à jour le jeu

    for event in pygame.event.get(): #Boucle d'évènements
        """Arrêter le jeu"""
        if event.type == pygame.QUIT: #Action s'exécutant si le jeu doit s'arrêter
            running = False #Stopper le jeu
            game.register()
            pygame.quit() #Fermer la fenêtre

        """Détecter une touche du clavier"""
        if event.type == pygame.KEYDOWN: #Action s'exécutant si une touche du clavier est pressée
            game.pressed[event.key] = True #Signaler qu'une touche est pressée
            """Détecter si la touche espace est pressée pour lancer le projectile"""
            if event.key == pygame.K_SPACE and game.projectile is True and game.paused is False:
                game.player.launch_projectile()

            elif event.key == pygame.K_p:
                if game.version >= 1.03:
                    game.pause()

            elif event.key == pygame.K_m:
                if game.version >= 1.10:
                    if game.sound_manager.sound:
                        game.sound_manager.sound = False

                    else:
                        game.sound_manager.sound = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False #Signaler qu'aucune touche n'est pressée

        elif event.type == pygame.MOUSEBUTTONDOWN: #Action s'exécutant si le clic gauche est pressé
            if play_button_rect.collidepoint(event.pos): #Action s'exécutant si la souris touche le bouton
                game.infinite = False
                game.start() #Lancer le jeu
                game.sound_manager.play_sound("click") #Jouer le son du clic

            elif play2_button_rect.collidepoint(event.pos):
                if game.version >= 1.04:
                    game.infinite = True
                    game.start()
                    game.sound_manager.play_sound("click")  # Jouer le son du clic


    clock.tick(FPS) #Définir la vitesse du jeu