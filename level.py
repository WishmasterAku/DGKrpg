import pygame
class Level:
    def __init__(self):
        
        # get display surface 
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
    def run(self):
        #update and draw on game
        pass