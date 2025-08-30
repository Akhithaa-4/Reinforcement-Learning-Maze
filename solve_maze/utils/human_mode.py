import pygame
import sys

# Map key presses to actions
KEY_TO_ACTION = {
    pygame.K_UP: 0,    # up
    pygame.K_RIGHT: 1, # right
    pygame.K_DOWN: 2,  # down
    pygame.K_LEFT: 3   # left
}

def play_human(env):
    import pygame
    pygame.init()

    rows, cols = env.maze_size
    cell_size = 40
    width, height = cols * cell_size, rows * cell_size
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    maze = env.env.maze_view.maze.maze_cells

    # Start state
    state = env.reset()
    r, c = env.env.maze_view.robot

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                action = None
                if event.key == pygame.K_UP:
                    action = 0   # up
                elif event.key == pygame.K_DOWN:
                    action = 1   # down
                elif event.key == pygame.K_LEFT:
                    action = 2   # left
                elif event.key == pygame.K_RIGHT:
                    action = 3   # right

                if action is not None:
                    # Take a step in the environment
                    state, reward, done, _, _ = env.step(action)
                    r, c = env.env.maze_view.robot
                    if done:
                        print("🎉 Goal reached!")
                        running = False

        # Draw maze
        screen.fill((255,255,255))
        for i in range(rows):
            for j in range(cols):
                color = (0,0,0) if maze[i][j] == 1 else (200,200,200)
                pygame.draw.rect(screen, color, (j*cell_size, i*cell_size, cell_size, cell_size))

        # Draw goal
        goal_r, goal_c = env.env.maze_view.goal
        pygame.draw.rect(screen, (0,255,0), (goal_c*cell_size, goal_r*cell_size, cell_size, cell_size))

        # Draw player
        pygame.draw.circle(screen, (255,0,0), (c*cell_size+cell_size//2, r*cell_size+cell_size//2), cell_size//3)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()



    sys.exit()
