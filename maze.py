import matplotlib.pyplot as plt
import numpy as np
import random


def visualize_maze(maze, start, goal, figure = 1):
    # Plot maze
    plt.figure(figure)
    plt.imshow(maze, cmap=plt.cm.binary)
    plt.scatter([start[1]], [start[0]], color='b')  # Start point
    plt.scatter([goal[1]], [goal[0]], color='r')



# DFS function to generate maze
def generate_maze(start, goal, size = 21):
    # Directions for DFS
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    maze = np.full((size, size), 1)

    stack = [start]
    while stack:
        x, y = stack[-1]
        maze[x][y] = 0
        options = [(dx, dy) for dx, dy in dirs if 0 <= x+2*dx < size and 0 <= y+2*dy < size and maze[x+2*dx][y+2*dy]]
        if options:
            dx, dy = random.choice(options)
            maze[x+dx][y+dy] = 0
            stack.append((x+2*dx, y+2*dy))
        else:
            stack.pop()
    maze[goal] = 0
    return maze

# Maze size
n = 21

# Start and goal positions
startNW = (0, 0)
startNE = (0, n-1)
startSW = (n-1, 0)
startSE = (n-1, n-1)
goal = (n//2, n//2)





# Generate mazes
maze1 = generate_maze(startNW, goal, n)
maze2 = generate_maze(startNE, goal, n)
maze3 = generate_maze(startSW, goal, n)
maze4 = generate_maze(startSW, goal, n)


visualize_maze(maze1, startNW, goal, 1)
visualize_maze(maze2, startNE, goal, 2)
visualize_maze(maze3, startSW, goal, 3)
visualize_maze(maze4, startSE, goal, 4)

plt.show()