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
    pygame.init()

    # 👇 Reset environment so maze + robot start properly
    env.reset()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                action = None
                if event.key == pygame.K_UP:
                    action = 0
                elif event.key == pygame.K_DOWN:
                    action = 1
                elif event.key == pygame.K_LEFT:
                    action = 2
                elif event.key == pygame.K_RIGHT:
                    action = 3
                elif event.key == pygame.K_q:   # quit
                    running = False

                if action is not None:
                    step_result = env.step(action)
                    if len(step_result) == 5:
                        state, reward, done, _, _ = step_result
                    else:
                        state, reward, done, _ = step_result

                    if done:
                        print("🎉 Goal reached!")
                        running = False

        # 👇 Render environment each frame
        env.render()

    pygame.quit()
    sys.exit()
