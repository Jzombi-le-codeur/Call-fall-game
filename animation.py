"""Importer les bibliothèques/modules"""
import pygame #Importer la bibliothèque Pygame
import os #Importer la bibliothèque Os

"""Définir la classe pour animer les sprites"""
class AnimateSprite(pygame.sprite.Sprite): #Créer la classe pour animer les sprites
    def __init__(self, sprite_name, size=(200, 200)): #Définir le constructeur
        super().__init__() #Dire que cette classe fait partie du jeu
        self.size = size #Récupérer les dimensions des sprites
        self.image = pygame.image.load(f"assets/{sprite_name}.png") #Importer les images des animations
        self.image = pygame.transform.scale(self.image, size) #Redimensioner les images
        self.current_image = 0 #Dire que les images sont à 0
        self.images = animations.get(sprite_name) #Avoir le nom des sprites pour l'animation
        self.animation = False #Désactiver les animations

    """Définir les méthodes"""
    def start_animation(self): #Créer la classe pour lancer les animations
        self.animation = True #Activer les animations

    def animate(self, loop=False): #Créer la méthode pour animer les sprites
        """Animer les sprites"""
        if self.animation and self.game.paused is False: #Action s'exécutant si les animations sont activées
            self.current_image += 1 #Changer d'image d'annimation
            """Quand la dernière image est atteinte"""
            if self.current_image >= len(self.images): #Action s'exécutant si la dernière image du sprite est atteinte
                self.current_image = 0 #Réinitialiser les images
                """Quand l'animation est terminée"""
                if loop is False: #Action s'exécutant si une animation est terminée
                     self.animation = False #Désactiver les animations

            self.image = self.images[self.current_image] #Changer l'image par la suivante
            self.image = pygame.transform.scale(self.image, self.size)  # Redimensioner les images

"""Définir les fonctions"""
def load_animation_images(sprite_name): #Créer une fonction pour charger les images des animations
    images = [] #Créer une liste pour stocker les images
    path = f"assets/{sprite_name}/{sprite_name}" #Définir les chemins des images

    for num in range(1, 24): #Faire une boucle pour changer d'image
        image_path = path + str(num) + ".png" #Définir les chemins pour une image
        images.append(pygame.image.load(image_path)) #Ajouter l'image à la liste

    return images #Renvoyer la liste des images

animations = { #Créer un dictionnaire pour les sprites
    "mummy": load_animation_images("mummy"), #Créer un élément pour la momie
    "player": load_animation_images("player"), #Créer un élément pour le joueur
    "alien": load_animation_images("alien"), #Créer un élément pour l'alien
}