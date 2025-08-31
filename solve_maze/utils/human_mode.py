import pygame
import numpy as np

# Map arrow keys to actions (assuming 0:UP, 1:RIGHT, 2:DOWN, 3:LEFT)
KEY_TO_ACTION = {
    pygame.K_UP: 0,
    pygame.K_RIGHT: 1,
    pygame.K_DOWN: 2,
    pygame.K_LEFT: 3,
}

def play_human(env):
    print("🎮 Use arrow keys to play the maze. Press ESC to quit.")

    running = True
    while running:
        env.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    env.step(0)
                elif event.key == pygame.K_RIGHT:
                    env.step(1)
                elif event.key == pygame.K_DOWN:
                    env.step(2)
                elif event.key == pygame.K_LEFT:
                    env.step(3)

    env.close()
    pygame.quit()
