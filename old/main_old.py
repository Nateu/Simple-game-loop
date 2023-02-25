import sys

import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT


class Game:
    WIDTH = 200
    HEIGHT = 200
    PLAYER_SIZE = 10
    PLAYER_COLOR = (127, 0, 255)
    WALL_COLOR = (0, 255, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("Maze Game")
        self.clock = pygame.time.Clock()
        self.player_x = 10
        self.player_y = 10
        self.walls = []
        self.move_direction = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.move_direction = (-1, 0)
                elif event.key == K_RIGHT:
                    self.move_direction = (1, 0)
                elif event.key == K_UP:
                    self.move_direction = (0, -1)
                elif event.key == K_DOWN:
                    self.move_direction = (0, 1)

    def move_player(self):
        if self.move_direction:
            dx, dy = self.move_direction
            new_x = self.player_x + dx * Game.PLAYER_SIZE
            new_y = self.player_y + dy * Game.PLAYER_SIZE
            if self.can_move_to(new_x, new_y):
                self.player_x = new_x
                self.player_y = new_y
            self.move_direction = None

    def can_move_to(self, x, y):
        new_rect = pygame.Rect(x, y, Game.PLAYER_SIZE, Game.PLAYER_SIZE)
        for wall in self.walls:
            if new_rect.colliderect(wall):
                return False
        return True

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(
            self.screen,
            Game.PLAYER_COLOR,
            (self.player_x, self.player_y, Game.PLAYER_SIZE, Game.PLAYER_SIZE),
        )
        for wall in self.walls:
            pygame.draw.rect(self.screen, Game.WALL_COLOR, wall)
        pygame.display.update()

    def load_maze(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                if char == "#":
                    self.walls.append(
                        pygame.Rect(
                            x * Game.PLAYER_SIZE,
                            y * Game.PLAYER_SIZE,
                            Game.PLAYER_SIZE,
                            Game.PLAYER_SIZE,
                        )
                    )

    @classmethod
    def run(cls, filename):
        game = cls()
        game.load_maze(filename)
        while True:
            game.handle_events()
            game.move_player()
            game.draw()
            game.clock.tick(60)


if __name__ == "__main__":
    Game.run("maze.txt")
