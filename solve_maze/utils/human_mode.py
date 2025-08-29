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

    # Maze layout is inside maze_view
    maze = env.env.maze_view.maze

    # Start at robot position
    r, c = env.env.maze_view.robot
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                old_r, old_c = r, c
                if event.key == pygame.K_UP:    r, c = max(0, r-1), c
                elif event.key == pygame.K_DOWN: r, c = min(rows-1, r+1), c
                elif event.key == pygame.K_LEFT: c = max(0, c-1)
                elif event.key == pygame.K_RIGHT: c = min(cols-1, c+1)

                # If wall, revert
                if maze[r][c] == 1:
                    r, c = old_r, old_c

                # Move robot in MazeEnv too
                env.env.maze_view.robot = np.array([r, c])

        # Draw
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
