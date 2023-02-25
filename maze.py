import random


class Maze:
    WALL_COLOR = (0, 255, 0)
    WALL_SIZE = 15
    EXIT_COLOR = (200, 200, 200)

    def __init__(self, pygame, filename: str):
        self.pygame = pygame
        self.walls = []
        self.exit_location = (0, 0)
        self.maze_lines = None
        self.load_maze(filename)
        self.list_open_spaces()
        self.width = max(len(line.strip()) for line in self.maze_lines) * self.WALL_SIZE
        self.height = len(self.maze_lines) * self.WALL_SIZE

    def create_exit(self):
        self.exit_location = self.get_open_space()

    def check_for_exit(self, x, y):
        return (x, y) == self.exit_location

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def list_open_spaces(self):
        self.open_spaces = []
        for y, line in enumerate(self.maze_lines):
            for x, char in enumerate(line.strip()):
                if char == " ":
                    self.open_spaces.append((x, y))

    def get_open_space(self):
        return random.choice(self.open_spaces)

    def is_open_space(self, x: int, y: int):
        return (x, y) in self.open_spaces

    def load_maze(self, filename):
        with open(filename, "r") as f:
            self.maze_lines = f.readlines()

        for y, line in enumerate(self.maze_lines):
            for x, char in enumerate(line.strip()):
                if char == "#":
                    self.walls.append(
                        self.pygame.Rect(
                            x * self.WALL_SIZE,
                            y * self.WALL_SIZE,
                            self.WALL_SIZE,
                            self.WALL_SIZE,
                        )
                    )

    def draw(self, screen):
        for wall in self.walls:
            self.pygame.draw.rect(screen, self.WALL_COLOR, wall)
        exit_x, exit_y = self.exit_location
        self.pygame.draw.rect(
            screen,
            self.EXIT_COLOR,
            (
                exit_x * self.WALL_SIZE,
                exit_y * self.WALL_SIZE,
                self.WALL_SIZE,
                self.WALL_SIZE,
            ),
        )
