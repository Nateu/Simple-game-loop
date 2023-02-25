from maze import Maze

class Player:
    PLAYER_SIZE = 10
    PLAYER_COLOR = (128, 0, 255)
    PLAYER_SHIELD_COLOR = (255, 255, 204)
    
    def __init__(self, pygame, maze: Maze):
        self.pygame = pygame
        self.maze = maze
        self.is_shield_on = False
        self.shield_cooldown = -1000
        self.x, self.y = self.maze.get_open_space()        
        self.direction = (0, 0)
        
    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if self.maze.is_open_space(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def rect(self):
        return self.pygame.Rect(
            self.x * Maze.WALL_SIZE + (0.5 * (Maze.WALL_SIZE - self.PLAYER_SIZE)), 
            self.y * Maze.WALL_SIZE + (0.5 * (Maze.WALL_SIZE - self.PLAYER_SIZE)),
            self.PLAYER_SIZE,
            self.PLAYER_SIZE
        )

    def shield_rect(self):
        return self.pygame.Rect(
            (self.x * Maze.WALL_SIZE) - (0.5 * Maze.WALL_SIZE), 
            (self.y * Maze.WALL_SIZE) - (0.5 * Maze.WALL_SIZE),
            2 * Maze.WALL_SIZE,
            2 * Maze.WALL_SIZE
        )
        
    def draw(self, screen):
        self.pygame.draw.rect(screen, self.PLAYER_COLOR, self.rect())

    def draw_shield(self, screen):
        if self.is_shield_on:
            self.pygame.draw.rect(screen, self.PLAYER_SHIELD_COLOR, self.shield_rect())

    def shield_on(self):
        if self.shield_cooldown <= -150:
            self.is_shield_on = True
            self.shield_cooldown = 50

    def deminish_shield(self):
        self.shield_cooldown -= 1
        if self.shield_cooldown <= 0:
            self.is_shield_on = False
