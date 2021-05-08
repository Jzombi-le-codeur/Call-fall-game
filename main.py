"""Importer les bibliothèques/modules"""
from game import Game #Importer la classe du jeu
import pygame #Importer la bibliothèque pygame

"""Créer et personnaliser la fenêtre"""
pygame.display.set_caption("Call fall game") #Créer une fenêtre et définir son titre
screen = pygame.display.set_mode((1080, 720)) #Définir les dimensions de la fenêtre

"""Charger les éléments"""
background = pygame.image.load("assets/bg.jpg") #Charger l'arrière-plan
game = Game() #Charger le jeu

"""Définir la boucle du jeu"""
running = True #Lancer le jeu

while running: #Boucle tant que que le jeu est exécuté
    """Mettre les images sur la fenêtre"""
    screen.blit(background, (0, -200)) #Afficher l'arrière-plan sur la fenêtre
    screen.blit(game.player.image, game.player.rect) #Afficher le joueur sur la fenêtre
    game.player.all_projectiles.draw(screen)  # Dessiner les projectiles sur la fenêtre
    game.all_monsters.draw(screen) #Afficher les monstres sur la fenêtre

    """Actualiser la barre de vies du joueur"""
    game.player.updade_health_bar(screen)

    """Déplacer les éléments"""
    #Déplacer le projectile
    for projectile in game.player.all_projectiles: #Dans Projectile
        projectile.move() #Faire déplacer les projectile

    """Récupérer les monstres dans le main"""
    for monster in game.all_monsters: #Dans Projectile
        monster.forward() #Faire déplacer les projectile
        monster.updade_health_bar(screen) #Dessiner la barre de vie sur la fenêtre

    """Vérifier la direction du joueur"""
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width(): #Vérifier
                                         # que la touche gauche est pressée et que le joueur ne dépasse pas la bordure
                                         # droite
        game.player.move_right() #Si c'est le cas déplacer le joueur à droite

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0: #Vérifier que la touche gauche est pressée et que
                                                             # le joueur ne dépasse pas la bordure gauche
        game.player.move_left() #Si c'est le cas déplacer le joueur à gauche

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
