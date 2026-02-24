import pygame
import random
from pygame.sprite import Sprite

class Target(Sprite):

    def __init__(self, r_game):
        super().__init__()

        self.screen = r_game.screen
        self.color = (0, 0, 255)  # blå
        self.radius = 40

        # skapa en "låda" som håller positionen
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)

        # startposition (uppe på skärmen t.ex.)
        self.rect.midtop = r_game.screen.get_rect().midtop

        self.y = float(self.rect.y)
        self.speed = 2
        screen_rect = r_game.screen.get_rect()
        x = random.randint(self.radius, screen_rect.width - self.radius)
        self.rect.midtop = (x, 0)

        

    def update(self):
        # flytta neråt
         self.y += self.speed
         self.rect.y = self.y
        

    def draw(self):
        # rita cirkeln varje frame
        pygame.draw.circle(
            self.screen,
            self.color,
            self.rect.center,
            self.radius
        )
