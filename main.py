import pygame, sys
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE
from enemy import Enemy
from maze import Maze
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.maze = Maze(pygame, 'maze.txt')
        self.screen = pygame.display.set_mode((self.maze.get_width(), self.maze.get_height()))
        pygame.display.set_caption('Maze Game')
        self.clock = pygame.time.Clock()
        self.maze.create_exit()
        self.player = Player(pygame, self.maze)
        self.enemy = Enemy(pygame, self.maze)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.move(-1, 0)
                elif event.key == K_RIGHT:
                    self.player.move(1, 0)
                elif event.key == K_UP:
                    self.player.move(0, -1)
                elif event.key == K_DOWN:
                    self.player.move(0, 1)
                elif event.key == K_SPACE:
                    self.player.shield_on()
        
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw_shield(self.screen)
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        pygame.display.update()    

    def check_player_win_condition(self):
        if self.maze.check_for_exit(self.player.x, self.player.y):
            print('Game Over: Player won, you found the exit')
            pygame.quit()
            sys.exit()

    def check_enemy_win_condition(self):
        if self.player.x == self.enemy.x and self.player.y == self.enemy.y:
            print('Game Over: You are dead, Enemy killed you')
            pygame.quit()
            sys.exit()

    def check_enemy_death(self):
        if self.player.is_shield_on and self.enemy.rect().colliderect(self.player.shield_rect()):
            print("Your shield has killed the enemy")
            self.enemy.die()
        
    
    @classmethod
    def run(cls):
        game = cls()
        while True:
            game.handle_events()
            game.check_player_win_condition()
            game.check_enemy_death()
            game.enemy.move()
            game.player.deminish_shield()
            game.draw()
            game.check_enemy_win_condition()
            game.clock.tick(60)

if __name__ == '__main__':
    Game.run()
