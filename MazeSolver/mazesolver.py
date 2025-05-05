import tkinter as tk
import random
import heapq
import time
from collections import deque

# Colors and constants
DARK_BG = "#1e1e1e"
DARK_GRID = "#2d2d2d"
WALL_COLOR = "#444"
PATH_COLOR = "#1f77b4"
START_COLOR = "#3fb950"
END_COLOR = "#e5534b"
VISITED_COLOR = "#6c6c6c"
FINAL_PATH_COLOR = "#f0e442"

CELL_SIZE = 20
DELAY = 20

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]
        self._generate_maze(1, 1)
        self.randomize_start_end()

    def prepare_generation(self):
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        self.stack = []
        self.visited = set()

        start_x = random.randrange(0, self.width, 2)
        start_y = random.randrange(0, self.height, 2)
        self.stack.append((start_x, start_y))
        self.visited.add((start_x, start_y))

    def generate_step(self):
        if not self.stack:
            return False

        x, y = self.stack[-1]
        self.grid[y][x] = 0

        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in self.visited:
                self.grid[ny][nx] = 0
                self.grid[y + dy // 2][x + dx // 2] = 0
                self.visited.add((nx, ny))
                self.stack.append((nx, ny))
                return True

        self.stack.pop()
        return True

    def _generate_maze(self, x, y):
        self.grid[y][x] = 0
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self._is_valid(nx, ny):
                mx, my = x + dx // 2, y + dy // 2
                self.grid[my][mx] = 0
                self._generate_maze(nx, ny)

    def generate_prims(self):
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        walls = []
        start_x, start_y = random.randrange(0, self.width, 2), random.randrange(0, self.height, 2)
        self.grid[start_y][start_x] = 0

        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = start_x + dx, start_y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                walls.append((start_x, start_y, nx, ny))

        while walls:
            x, y, nx, ny = random.choice(walls)
            walls.remove((x, y, nx, ny))

            if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == 1:
                self.grid[ny][nx] = 0
                self.grid[y + (ny - y) // 2][x + (nx - x) // 2] = 0

                for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                    nnx, nny = nx + dx, ny + dy
                    if 0 <= nnx < self.width and 0 <= nny < self.height:
                        walls.append((nx, ny, nnx, nny))

    def generate_prims_step(self):
        if not hasattr(self, 'walls'):
            self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
            self.walls = []
            start_x, start_y = random.randrange(0, self.width, 2), random.randrange(0, self.height, 2)
            self.grid[start_y][start_x] = 0

            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nx, ny = start_x + dx, start_y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    self.walls.append((start_x, start_y, nx, ny))

        if self.walls:
            x, y, nx, ny = random.choice(self.walls)
            self.walls.remove((x, y, nx, ny))

            if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == 1:
                self.grid[ny][nx] = 0
                self.grid[y + (ny - y) // 2][x + (nx - x) // 2] = 0

                for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                    nnx, nny = nx + dx, ny + dy
                    if 0 <= nnx < self.width and 0 <= nny < self.height:
                        self.walls.append((nx, ny, nnx, nny))

            return True 
        else:
            del self.walls
            return False

    def generate_kruskals(self):
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        edges = []
        parent = {}
        rank = {}

        def find(cell):
            if parent[cell] != cell:
                parent[cell] = find(parent[cell])
            return parent[cell]

        def union(cell1, cell2):
            root1 = find(cell1)
            root2 = find(cell2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        for y in range(0, self.height, 2):
            for x in range(0, self.width, 2):
                cell = (x, y)
                parent[cell] = cell
                rank[cell] = 0
                for dx, dy in [(2, 0), (0, 2)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        edges.append(((x, y), (nx, ny)))

        random.shuffle(edges)

        for (x1, y1), (x2, y2) in edges:
            if find((x1, y1)) != find((x2, y2)):
                union((x1, y1), (x2, y2))
                self.grid[y1][x1] = 0
                self.grid[y2][x2] = 0
                self.grid[y1 + (y2 - y1) // 2][x1 + (x2 - x1) // 2] = 0

    def generate_kruskals_step(self):
        if not hasattr(self, 'kruskal_data'):
            self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
            self.kruskal_data = {
                'edges': [],
                'parent': {},
                'rank': {}
            }

            def find(cell):
                if self.kruskal_data['parent'][cell] != cell:
                    self.kruskal_data['parent'][cell] = find(self.kruskal_data['parent'][cell])
                return self.kruskal_data['parent'][cell]

            def union(cell1, cell2):
                root1 = find(cell1)
                root2 = find(cell2)
                if root1 != root2:
                    if self.kruskal_data['rank'][root1] > self.kruskal_data['rank'][root2]:
                        self.kruskal_data['parent'][root2] = root1
                    elif self.kruskal_data['rank'][root1] < self.kruskal_data['rank'][root2]:
                        self.kruskal_data['parent'][root1] = root2
                    else:
                        self.kruskal_data['parent'][root2] = root1
                        self.kruskal_data['rank'][root1] += 1

            self.kruskal_data['find'] = find
            self.kruskal_data['union'] = union

            for y in range(0, self.height, 2):
                for x in range(0, self.width, 2):
                    cell = (x, y)
                    self.kruskal_data['parent'][cell] = cell
                    self.kruskal_data['rank'][cell] = 0
                    for dx, dy in [(2, 0), (0, 2)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            self.kruskal_data['edges'].append(((x, y), (nx, ny)))

            random.shuffle(self.kruskal_data['edges'])

        if self.kruskal_data['edges']:
            (x1, y1), (x2, y2) = self.kruskal_data['edges'].pop()
            find = self.kruskal_data['find']
            union = self.kruskal_data['union']

            if find((x1, y1)) != find((x2, y2)):
                union((x1, y1), (x2, y2))
                self.grid[y1][x1] = 0
                self.grid[y2][x2] = 0
                self.grid[y1 + (y2 - y1) // 2][x1 + (x2 - x1) // 2] = 0

            return True 
        else:
            del self.kruskal_data
            return False

    def _is_valid(self, x, y):
        return 0 < x < self.width - 1 and 0 < y < self.height - 1 and self.grid[y][x] == 1

    def randomize_start_end(self):
        empty_cells = [(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == 0]
        if len(empty_cells) < 2:
            return
        self.start, self.end = random.sample(empty_cells, 2)

class MazeApp:
    def __init__(self, master, width, height):
        self.master = master
        self.height = height
        self.width = width

        self.dark_mode = True
        self.bg_color = DARK_BG
        self.grid_color = DARK_GRID
        self.wall_color = WALL_COLOR
        self.path_color = PATH_COLOR  
        self.start_color = START_COLOR
        self.end_color = END_COLOR
        self.visited_color = VISITED_COLOR
        self.final_path_color = FINAL_PATH_COLOR
        self.text_color = "white"

        self.algorithm = tk.StringVar(value="bfs")
        self.generation_algorithm = tk.StringVar(value="rbt")

        self.master.configure(bg=self.bg_color)

        self.canvas = tk.Canvas(master, width=width * CELL_SIZE, height=height * CELL_SIZE, bg=self.bg_color, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Left side
        self.btn_generate = tk.Button(master, text="Generate Maze", command=self.generate_maze, bg=self.bg_color, fg=self.text_color)
        self.btn_generate.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        self.generation_status_label = tk.Label(master, text="Status: Ready", bg=self.bg_color, fg=self.text_color)
        self.generation_status_label.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        self.generation_time_label = tk.Label(master, text="Generation Time: -- ms", bg=self.bg_color, fg=self.text_color)
        self.generation_time_label.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
        
        # Right side
        self.btn_solve = tk.Button(master, text="Solve Maze", command=self.solve_maze, bg=self.bg_color, fg=self.text_color)
        self.btn_solve.grid(row=1, column=1, sticky="ew")

        self.time_label = tk.Label(master, text="Solver Time: -- ms", bg=self.bg_color, fg=self.text_color)
        self.time_label.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

        self.visited_label = tk.Label(master, text="Nodes Visited: --", bg=self.bg_color, fg=self.text_color)
        self.visited_label.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

        # Radio Buttons
        self.radio_label = tk.Label(master, text="Solver Algorihtm", bg=self.bg_color, fg=self.text_color)
        self.radio_label.grid(row=1, column=2, sticky="ew", padx=10, pady=5)
        
        self.radio_frame = tk.Frame(master, bg=self.bg_color)
        self.radio_frame.grid(row=2, column=2, sticky="ew", padx=10, pady=5)

        tk.Radiobutton(self.radio_frame, text="BFS", variable=self.algorithm, value="bfs", bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color).pack(anchor="w")
        tk.Radiobutton(self.radio_frame, text="DFS", variable=self.algorithm, value="dfs", bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color).pack(anchor="w")
        tk.Radiobutton(self.radio_frame, text="A*", variable=self.algorithm, value="astar", bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color).pack(anchor="w")

        self.generation_type_label = tk.Label(master, text="Generation Algorithm", bg=self.bg_color, fg=self.text_color)
        self.generation_type_label.grid(row=1, column=3, sticky="ew", padx=10, pady=5)

        self.generation_frame = tk.Frame(master, bg=self.bg_color)
        self.generation_frame.grid(row= 2, column=3, sticky="ew", padx=10, pady=5)

        tk.Radiobutton(self.generation_frame, text="RBT", variable=self.generation_algorithm, value="rbt", bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color).pack(anchor="w")
        tk.Radiobutton(self.generation_frame, text="Prims", variable=self.generation_algorithm, value="prims", bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color).pack(anchor="w")
        tk.Radiobutton(self.generation_frame, text="Kruskals", variable=self.generation_algorithm, value="kruskals", bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color).pack(anchor="w")

        self.generate_maze()

    def generate_maze(self):
        algorithm = self.generation_algorithm.get()
        if algorithm == "rbt":
            self.maze = Maze(self.width, self.height)
            self.maze.prepare_generation()
            self.animate_maze_generation()
        elif algorithm == "prims":
            self.maze = Maze(self.width, self.height)
            self.animate_prims_generation()
        elif algorithm == "kruskals":
            self.maze = Maze(self.width, self.height)
            self.animate_kruskals_generation()
        else:
            print("Unkown generation algorithm selected.")
        
    def animate_kruskals_generation(self):
        if self.maze.generate_kruskals_step():
            self.draw_maze()
            self.master.after(DELAY, self.animate_kruskals_generation)
        else:
            self.generation_status_label.config(text="Status: Done!")
            self.maze.randomize_start_end()
            self.draw_maze()

    def animate_prims_generation(self):
        if self.maze.generate_prims_step():
            self.draw_maze()
            self.master.after(DELAY, self.animate_prims_generation)
        else:
            self.generation_status_label.config(text="Status: Done!")
            self.maze.randomize_start_end()
            self.draw_maze()

    def draw_maze(self):
        self.canvas.delete("all")
        self.canvas.configure(bg=self.bg_color)
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.maze.grid[y][x] == 1:
                    self._draw_cell(x, y, self.wall_color)
                else:  # Path
                    self._draw_cell(x, y, self.path_color)

        sx, sy = self.maze.start
        self._draw_cell(sx, sy, self.start_color)

        ex, ey = self.maze.end
        self._draw_cell(ex, ey, self.end_color)

    def _draw_cell(self, x, y, color):
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=self.grid_color)

    def animate_maze_generation(self):
        if not hasattr(self, 'generation_start_time'):
            self.generation_start_time = time.perf_counter()
            self.generation_status_label.config(text="Status: Generating maze...")

        if self.maze.generate_step():
            self.draw_maze()
            self.master.after(DELAY, self.animate_maze_generation)
        else:
            elapsed = (time.perf_counter() - self.generation_start_time) * 1000
            self.generation_time_label.config(text=f"Generation Time: {elapsed:.2f} ms")
            self.generation_status_label.config(text="Status: Done!")
            del self.generation_start_time 
            self.maze.randomize_start_end()
            self.draw_maze()

    def start_timer(self):
        self.solve_start_time = time.perf_counter()

    def stop_timer(self):
        elapsed = (time.perf_counter() - self.solve_start_time) * 1000
        self.time_label.config(text=f"Solver Time: {elapsed:.2f} ms")

    def solve_maze(self):
        self.start_timer()
        algorithm = self.algorithm.get()
        if algorithm == "bfs":
            self.solve_bfs()
        elif algorithm == "dfs":
            self.solve_dfs()
        elif algorithm == "astar":
            self.solve_a_star()
        else:
            print("Unknown algorihm selected.")
    
    def solve_bfs(self):
        queue = deque()
        visited = set()
        prev = {}
        visited_count = 0

        start = self.maze.start
        end = self.maze.end

        queue.append(start)
        visited.add(start)

        def step():
            nonlocal visited_count
            if queue:
                current = queue.popleft()
                if current == end:
                    self.stop_timer()
                    self.visited_label.config(text=f"Nodes Visited: {visited_count}")
                    self.trace_path(prev, start, end)
                    return
                
                x, y = current
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    neighbor = (nx, ny)
                    if (0 <= nx < self.maze.width and 0 <= ny < self.maze.height and self.maze.grid[ny][nx] == 0 and neighbor not in visited):
                        visited.add(neighbor)
                        visited_count += 1
                        prev[neighbor] = current
                        queue.append(neighbor)
                        self._draw_cell(nx, ny, VISITED_COLOR)
                self.master.after(DELAY, step)
            else:
                print("No path found.")
        step()

    def solve_dfs(self):
        stack = []
        visited = set()
        prev = {}
        visited_count = 0

        start = self.maze.start
        end = self.maze.end
        stack.append(start)
        visited.add(start)

        def step():
            nonlocal visited_count
            if stack:
                current = stack.pop()
                if current == end:
                    self.stop_timer()
                    self.visited_label.config(text=f"Nodes Visited: {visited_count}")
                    self.trace_path(prev, start, end)
                    return

                x, y = current
                for dx, dy in [(-1, 0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    neighbor = (nx, ny)
                    if (0 <= nx < self.maze.width and 0 <= ny < self.maze.height and self.maze.grid[ny][nx] == 0 and neighbor not in visited):
                        visited.add(neighbor)
                        visited_count += 1
                        prev[neighbor] = current
                        stack.append(neighbor)
                        self._draw_cell(nx, ny, VISITED_COLOR)
                self.master.after(DELAY, step)
            else:
                print("No path found.")
        
        step()

    def solve_a_star(self):
        start = self.maze.start
        end = self.maze.end
        visited_count = 0

        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}
        g_score = {start: 0}

        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        def step():
            nonlocal visited_count
            if open_set:
                _, current = heapq.heappop(open_set)

                if current == end:
                    self.stop_timer()
                    self.visited_label.config(text=f"Nodes Visited: {visited_count}")
                    self.trace_path(came_from, start, end)
                    return

                x, y = current
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    neighbor = (nx, ny)

                    if (0 <= nx < self.maze.width and 0 <= ny < self.maze.height and self.maze.grid[ny][nx] == 0):
                        tentative_g = g_score[current] + 1

                        if neighbor not in g_score or tentative_g < g_score[neighbor]:
                            came_from[neighbor] = current
                            g_score[neighbor] = tentative_g
                            f = tentative_g + heuristic(neighbor, end)
                            heapq.heappush(open_set, (f, neighbor))
                            self._draw_cell(nx, ny, VISITED_COLOR)
                            visited_count += 1

                self.master.after(DELAY, step)
            else:
                print("No path found.")

        step()
    
    def trace_path(self, prev, start, end):
        path = []
        at = end
        while at != start:
            path.append(at)
            at = prev[at]
        path.append(start)
        path.reverse()

        def draw_step(i):
            if i < len(path):
                x, y = path[i]
                self._draw_cell(x, y, 'yellow')
                self.master.after(DELAY, lambda: draw_step(i + 1))

        draw_step(0)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Solver")
    WIDTH, HEIGHT = 21, 21
    app = MazeApp(root, WIDTH, HEIGHT)
    root.mainloop()