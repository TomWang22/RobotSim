import numpy as np
import matplotlib.pyplot as plt
import heapq
import time
import random

class SimulationWithDynamics:
    def __init__(self, grid, start, goal, dynamic_obstacles):
        self.grid = grid
        self.rows, self.cols = grid.shape
        self.start = start
        self.goal = goal
        self.robot_position = start
        self.dynamic_obstacles = dynamic_obstacles
        self.path = []

        # Place initial dynamic obstacles
        for obs in self.dynamic_obstacles:
            self.grid[obs] = 1

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x, y] == 0

    def heuristic(self, a, b):
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def find_path(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.goal:
                return self.reconstruct_path(came_from)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if self.is_valid(*neighbor):
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, self.goal)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []

    def reconstruct_path(self, came_from):
        path = []
        current = self.goal
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(self.start)
        return path[::-1]

    def update_dynamic_obstacles(self):
        for i, (x, y) in enumerate(self.dynamic_obstacles):
            self.grid[x, y] = 0
            dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
            new_x, new_y = x + dx, y + dy

            if self.is_valid(new_x, new_y):
                self.dynamic_obstacles[i] = (new_x, new_y)
                self.grid[new_x, new_y] = 1

    def move_robot(self):
        while self.robot_position != self.goal:
            self.update_dynamic_obstacles()
            self.path = self.find_path()

            if not self.path:
                print("No path available!")
                break

            for step in self.path:
                self.robot_position = step
                self.render()
                time.sleep(0.5)
                self.update_dynamic_obstacles()

    def render(self):
        grid_copy = self.grid.copy()
        grid_copy[self.robot_position] = 2
        grid_copy[self.goal] = 3

        plt.imshow(grid_copy, cmap="gray")
        plt.title("Robot Simulation with Dynamic Obstacles")
        plt.pause(0.1)
        plt.clf()

# Example environment setup
grid = np.array([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

start = (0, 0)
goal = (4, 4)
dynamic_obstacles = [(2, 2), (3, 3)]

sim = SimulationWithDynamics(grid, start, goal, dynamic_obstacles)
plt.ion()
sim.move_robot()
plt.ioff()
plt.show()
