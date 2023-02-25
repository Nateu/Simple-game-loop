import sys

import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World!")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


import random

import pygame

# Initialize Pygame
pygame.init()

# Set up game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up player
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_color = (255, 0, 0)

# Set up enemy
enemy_size = 50
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = 0
enemy_color = (0, 255, 0)
enemy_speed = 10

# Set up game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemy_y = 0

    # Check for collision
    if (
        player_x < enemy_x + enemy_size
        and player_x + player_size > enemy_x
        and player_y < enemy_y + enemy_size
        and player_y + player_size > enemy_y
    ):
        running = False

    # Draw everything
    screen.fill((255, 255, 255))
    pygame.draw.rect(
        screen, player_color, (player_x, player_y, player_size, player_size)
    )
    pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.display.update()

    # Set game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
