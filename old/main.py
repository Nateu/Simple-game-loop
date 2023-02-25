import random
import sys

import pygame
from pygame.locals import QUIT


class Game:
    WIDTH = 800
    HEIGHT = 600
    PLAYER_SIZE = 50
    ENEMY_SIZE = 50
    PLAYER_COLOR = (255, 0, 0)
    ENEMY_COLOR = (0, 255, 0)
    ENEMY_SPEED = 10

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("Avoid the Enemies!")
        self.player_x = Game.WIDTH // 2 - Game.PLAYER_SIZE // 2
        self.player_y = Game.HEIGHT - Game.PLAYER_SIZE - 10
        self.enemy_x = random.randint(0, Game.WIDTH - Game.ENEMY_SIZE)
        self.enemy_y = 0
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= 5
        if keys[pygame.K_RIGHT]:
            self.player_x += 5

    def move_enemy(self):
        self.enemy_y += Game.ENEMY_SPEED
        if self.enemy_y > Game.HEIGHT:
            self.enemy_x = random.randint(0, Game.WIDTH - Game.ENEMY_SIZE)
            self.enemy_y = 0

    def check_collision(self):
        if (
            self.player_x < self.enemy_x + Game.ENEMY_SIZE
            and self.player_x + Game.PLAYER_SIZE > self.enemy_x
            and self.player_y < self.enemy_y + Game.ENEMY_SIZE
            and self.player_y + Game.PLAYER_SIZE > self.enemy_y
        ):
            pygame.quit()
            sys.exit()

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(
            self.screen,
            Game.PLAYER_COLOR,
            (self.player_x, self.player_y, Game.PLAYER_SIZE, Game.PLAYER_SIZE),
        )
        pygame.draw.rect(
            self.screen,
            Game.ENEMY_COLOR,
            (self.enemy_x, self.enemy_y, Game.ENEMY_SIZE, Game.ENEMY_SIZE),
        )
        pygame.display.update()

    @classmethod
    def run(cls):
        game = cls()
        while True:
            game.handle_events()
            game.move_player()
            game.move_enemy()
            game.check_collision()
            game.draw()
            game.clock.tick(60)


if __name__ == "__main__":
    Game.run()
