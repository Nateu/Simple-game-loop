import random
from maze import Maze

class Enemy:
    ENEMY_SIZE = 8
    ENEMY_COLOR = (255, 0, 0)
    
    def __init__(self, pygame, maze: Maze):
        self.pygame = pygame
        self.maze = maze
        self.is_alive = True
        self.x, self.y = self.maze.get_open_space()
        self.direction = (0, 0)
        
    def move(self):
        if not self.is_alive:
            return
        while True:
            (new_x, new_y) = self.select_new_location()            
            if self.maze.is_open_space(new_x, new_y):
                self.x = new_x
                self.y = new_y
                self.direction = (0,0)
                return

    def select_new_location(self):
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        dx, dy = self.direction
        new_x = self.x + dx
        new_y = self.y + dy
        return (new_x, new_y)

    def rect(self):
        return self.pygame.Rect(
            self.x * Maze.WALL_SIZE + (0.5 * (Maze.WALL_SIZE - self.ENEMY_SIZE)), 
            self.y * Maze.WALL_SIZE + (0.5 * (Maze.WALL_SIZE - self.ENEMY_SIZE)),
            self.ENEMY_SIZE,
            self.ENEMY_SIZE
        )

    def draw(self, screen):
        if self.is_alive:
            self.pygame.draw.rect(screen, self.ENEMY_COLOR, self.rect())

    def die(self):
        self.x = -1
        self.y = -1
        self.is_alive = False