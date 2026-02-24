
import pygame

class Raketa:
    def __init__(self, r_game):
        self.screen = r_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/rocket.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 80))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.speed = 3
        self.x = float(self.rect.x)


    def draw_rocket(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed # flytta float-positionen
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        self.rect.x = int(self.x) # uppdatera rect från x


