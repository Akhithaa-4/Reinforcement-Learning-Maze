import pygame
import sys

def play_human(env):
    pygame.init()
   
    pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Maze Human Mode")
    print("✅ Human mode started... (using env.render like QLearning/SARSA)")

    state = env.reset()
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
                        next_state, reward, done, _, _ = step_result
                    else:
                        next_state, reward, done, _ = step_result

                    state = next_state
                    if done:
                        print("🎉 Goal reached!")
                        running = False

        # 🔹 rely on env's own rendering system
        env.render()

    pygame.quit()
    sys.exit()



    