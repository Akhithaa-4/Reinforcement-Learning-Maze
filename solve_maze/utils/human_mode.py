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

    env.reset()
    print("✅ Human mode started...")

    r, c = env.env.maze_view.robot
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("❌ Quit event detected")
                running = False
            elif event.type == pygame.KEYDOWN:
                print(f"⌨️ Key pressed: {event.key}")
                ...
        
        env.render()
        pygame.display.update()
        pygame.time.wait(50)



    pygame.quit()
    sys.exit()
