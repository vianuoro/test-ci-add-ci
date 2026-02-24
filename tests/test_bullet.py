import os
import sys

# make sure the project root is on the import path so `app` can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pygame
import pytest

from app.bullet import Bullet


class DummySettings:
    bullet_color = (255, 0, 0)
    bullet_width = 5
    bullet_height = 10
    bullet_speed = 2.0


class DummyRaketa:
    def __init__(self):
        # starting position doesn't really matter, just a Rect is required
        self.rect = pygame.Rect(50, 100, 20, 20)


class DummyGame:
    def __init__(self):
        # a surface can act as the "screen" for testing purposes
        self.screen = pygame.Surface((800, 600))
        self.settings = DummySettings()
        self.raketa = DummyRaketa()


def test_bullet_initial_position():
    """Bullet is positioned at the rocket's midtop and uses the game settings"""
    game = DummyGame()
    bullet = Bullet(game)

    assert bullet.screen is game.screen
    assert bullet.color == game.settings.bullet_color
    assert bullet.rect.midtop == game.raketa.rect.midtop


def test_bullet_update_moves_upwards():
    """Calling update should decrement the y coordinate by the speed"""
    game = DummyGame()
    bullet = Bullet(game)

    initial_y = bullet.y
    bullet.update()

    assert bullet.y == pytest.approx(initial_y - game.settings.bullet_speed)
    assert bullet.rect.y == bullet.y


def test_draw_bullet_calls_pygame_draw_rect(monkeypatch):
    """draw_bullet should call pygame.draw.rect with correct arguments"""
    game = DummyGame()
    bullet = Bullet(game)

    called = {}

    def fake_rect(screen, color, rect):
        called['args'] = (screen, color, rect)

    monkeypatch.setattr(pygame.draw, 'rect', fake_rect)
    bullet.draw_bullet()

    assert called['args'][0] is game.screen
    assert called['args'][1] == game.settings.bullet_color
    assert called['args'][2] == bullet.rect
