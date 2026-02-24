import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ clas som hanterar projektiler som skjuts av raketen """
    def __init__(self,r_game):
        super().__init__()
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = r_game.raketa.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """ flytta projektilen uppåt på skärmen """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    def draw_bullet(self):
        """ rita projektilen på skärmen """
        pygame.draw.rect(self.screen,self.color,self.rect)

