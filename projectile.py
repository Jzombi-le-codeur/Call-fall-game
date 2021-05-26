"""Importer les bibliothèques/modules"""
import pygame #Importer la bibliothèque Pygame

"""Définir la classe du projectile"""
class Projectile(pygame.sprite.Sprite): #Créer la classe du projectile
    """Définir les attributs"""
    def __init__(self, player): #Créer le constructeur de la classe
        super().__init__() #Dire à pygame que les projectiles sont des éléments graphiques du jeu
        self.velocity = 5 #Définir la vitesse du projectile
        self.image = pygame.image.load("assets/projectile.png") #Importer l'image du joueur
        self.image = pygame.transform.scale(self.image, (50, 50)) #Réduire la taille du projectile
        self.rect = self.image.get_rect() #Demander la position du projectile
        self.rect.x = player.rect.x + 120 #Définir l'abcisse du projectile
        self.rect.y = player.rect.y + 80 #Définir l'ordonnée du projectile
        self.origin_image = self.image #Garder l'image d'origine
        self.angle = 0 #Définir l'angle du projectile
        self.player = player

    def remove(self): #Méthode pour supprimer le projectile
        """Supprimer un projectile"""
        self.player.all_projectiles.remove(self)  # Supprimer le projectile

    def move(self): #Méthode pour déplacer le projectile
        """Définir l'animation du projectile"""
        self.rect.x += self.velocity #Déplacer le projectile
        self.rotate() #Faire tourner le projectile

        """Vérifier les collisions"""
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters): #Vérifier les collisions
            self.remove() #Supprimer le projectile
            """Infliger des dégâts aux monstres"""
            monster.damage(5) #Infliger des dégâts aux monstres
        """Vérifier que le projectile n'est plus sur l'écran"""
        if self.rect.x > 1080: #Vérifier que le projectile est à la bordure
            self.remove() #Supprimer le projectile

    def rotate(self):  # Méthode pour faire tourner le projectile
        """Faire tourner le projectile"""
        self.angle += 12 #Définir la rotation
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1) #Définir la rotation du projectile
        self.rect = self.image.get_rect(center = self.rect.center) #Définir le centre de rotation du projectile