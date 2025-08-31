import pygame
import sys

# Map key presses to actions
KEY_TO_ACTION = {
    pygame.K_UP: 0,    # up
    pygame.K_RIGHT: 1, # right
    pygame.K_DOWN: 2,  # down
    pygame.K_LEFT: 3   # left
}

import pygame
import sys

def play_human(env):
    print("✅ Human mode started...")

    pygame.init()
    screen = pygame.display.set_mode((600, 600))  # force open a window
    clock = pygame.time.Clock()

    running = True
    while running:
        print("🔄 Loop running... waiting for event")  # debug log
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                print(f"⌨️ Key pressed: {event.key}")
                if event.key == pygame.K_q:
                    running = False
                elif event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    action = {pygame.K_UP: 0, pygame.K_DOWN: 1,
                              pygame.K_LEFT: 2, pygame.K_RIGHT: 3}[event.key]
                    step_result = env.step(action)
                    if len(step_result) == 5:
                        _, _, done, _, _ = step_result
                    else:
                        _, _, done, _ = step_result
                    if done:
                        print("🎉 Goal reached!")
                        running = False

        # force drawing (even empty) to show window
        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()



    