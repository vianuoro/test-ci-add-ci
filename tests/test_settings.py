import os
import sys

# ensure project root is on path so `app` package is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.settings import Settings


def test_settings_defaults():
    """Verify Settings class initializes expected attributes and values"""
    s = Settings()

    # screen/background color
    assert hasattr(s, 'color')
    assert s.color == (230, 230, 230)

    # bullet settings
    assert s.bullet_speed == 5
    assert s.bullet_width == 3
    assert s.bullet_height == 15
    assert s.bullet_color == (60, 60, 60)

    # target settings
    assert s.target_speed == 2
    assert s.target_color == (255, 0, 0)


def test_settings_mutability():
    """Changing attributes should be possible and independent"""
    s = Settings()
    orig_color = s.color
    s.color = (0, 0, 0)
    assert s.color != orig_color
    # other values remain unchanged
    assert s.bullet_speed == 5
    assert s.target_color == (255, 0, 0)
