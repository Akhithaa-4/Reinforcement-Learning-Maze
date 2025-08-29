import numpy as np
import matplotlib.pyplot as plt

def visualize_policy(Q, maze_size, terminal_state, title="Policy"):
    rows, cols = maze_size
    fig, ax = plt.subplots(figsize=(cols/2, rows/2))

    # Draw grid
    ax.set_xticks(np.arange(-0.5, cols, 1))
    ax.set_yticks(np.arange(-0.5, rows, 1))
    ax.grid(True)
    ax.set_xlim(-0.5, cols-0.5)
    ax.set_ylim(-0.5, rows-0.5)

    # Handle Q depending on format
    if isinstance(Q, np.ndarray):
        if Q.ndim == 3:  # shape (rows, cols, actions)
            best_policy = np.argmax(Q, axis=2)
            confidence = np.max(Q, axis=2)
        elif Q.ndim == 2:  # shape (num_states, num_actions)
            num_states, num_actions = Q.shape
            best_policy = np.full(maze_size, -1)
            confidence = np.full(maze_size, 0.0)
            for state in range(num_states):
                row = state // cols
                col = state % cols
                best_policy[row, col] = np.argmax(Q[state])
                confidence[row, col] = np.max(Q[state])
        else:
            raise ValueError(f"Unexpected Q shape: {Q.shape}")

    elif isinstance(Q, dict):
        best_policy = np.full(maze_size, -1)
        confidence = np.full(maze_size, 0.0)
        for state, actions in Q.items():
            if isinstance(state, tuple) and len(state) == 2:
                row, col = state
            else:
                row = state // cols
                col = state % cols
            best_policy[row, col] = np.argmax(actions)
            confidence[row, col] = np.max(actions)

    else:
        raise TypeError(f"Unsupported Q type: {type(Q)}")

    # Draw arrows based on best policy
    for r in range(rows):
        for c in range(cols):
            if (r, c) == terminal_state:
                ax.text(c, rows-r-1, "G", ha='center', va='center',
                        fontsize=12, color='green', fontweight='bold')
                continue
            action = best_policy[r, c]
            if action == -1:
                continue

            # Arrow direction
            dx, dy = 0, 0
            if action == 0:   # up
                dy = 0.4
            elif action == 1: # right
                dx = 0.4
            elif action == 2: # down
                dy = -0.4
            elif action == 3: # left
                dx = -0.4

            # Arrow thickness = confidence
            lw = 1 + 3 * (confidence[r, c] / (np.max(confidence) + 1e-6))

            ax.arrow(c, rows-r-1, dx, dy, head_width=0.2, head_length=0.2,
                     fc='blue', ec='blue', linewidth=lw)

    ax.set_title(title)
    plt.show()


    plt.title(title)
    plt.savefig(f"{title.replace(' ', '_')}.png")
    plt.show()



