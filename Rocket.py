import pygame
import sys
from settings import Settings
from raketa import Raketa
from bullet import Bullet
from target import Target


class Rocket:
    """Easy Rocket Game"""
    def __init__(self):
        pygame.init()

        screen_width = 1200
        screen_height = 800
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Rocket")

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.raketa = Raketa(self)

        self.bullets = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()

        # Poäng + text
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

        # Spawn (en gång per frame)
        self.spawn_counter = 0
        self.spawn_rate_frames = 300  # 300 frames ≈ 5 sek (vid 60 FPS)

        # Starta med en ballong
        self.new_target()

    def game_start(self):
        while True:
            self._check_events()

            # Update
            self.raketa.update()
            self.bullets.update()
            self.targets.update()

            # Kollisioner + poäng
            collisions = pygame.sprite.groupcollide(
                self.bullets,
                self.targets,
                True,   # ta bort bullet
                True    # ta bort target
            )
            for targets_hit in collisions.values():
                self.score += len(targets_hit)

            # Spawn nya targets (en gång per frame)
            self.spawn_counter += 1
            if self.spawn_counter >= self.spawn_rate_frames:
                self.new_target()
                self.spawn_counter = 0

            # Draw
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._fire_bullet()

            self.moving_left(event)
            self.moving_right(event)

    def _update_screen(self):
        self.screen.fill(self.settings.color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for target in self.targets.sprites():
            target.draw()

        self.raketa.draw_rocket()

        # Rita poäng
        score_img = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_img, (10, 10))

        pygame.display.flip()

    def _fire_bullet(self):
        """Skapa en ny projektil och lägg den i gruppen bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def new_target(self):
        """Skapa en ny target och lägg den i gruppen targets"""
        new_target = Target(self)
        self.targets.add(new_target)

    def moving_right(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.raketa.moving_right = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            self.raketa.moving_right = False

    def moving_left(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.raketa.moving_left = True
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            self.raketa.moving_left = False


if __name__ == '__main__':
    r = Rocket()
    r.game_start()
