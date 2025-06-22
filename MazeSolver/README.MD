# MazeSolver

MazeSolver is a Python application that generates and solves mazes visually using Tkinter. It supports multiple maze generation and solving algorithms, and provides a modern, interactive GUI with both light and dark modes.

---

## Features

- **Maze Generation Algorithms:**
  - Randomized Backtracking (RBT)
  - Prim's Algorithm
  - Kruskal's Algorithm
- **Maze Solving Algorithms:**
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - A* Search
- **Visualization:**
  - Step-by-step animation of both maze generation and solving
  - Adjustable speed for visualization
  - Dark mode and light mode toggle
  - Color-coded cells for walls, paths, start/end, visited nodes, and solution path
- **Statistics:**
  - Displays generation and solving time
  - Shows number of nodes visited

---

## Project Structure

```
PythonProjects/MazeSolver/
│
├── mazesolver.py      # Main application (GUI, maze logic, algorithms)
└── README.md          # Project documentation
```

---

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/LeviM-0323/Python-Projects.git
   cd PythonProjects/MazeSolver
   ```

2. **Usage:**
    ```sh
    python mazesolver.py
    ```

    - Use the "Generate Maze" button to create a new maze with the selected algorithm.
    - Select the solving algorithm (BFS, DFS, or A*) and click "Solve Maze" to watch the solution.
    - Adjust the speed slider to control animation speed.
    - Toggle dark mode for a different visual style.

    ---

## Customization

- **Maze Size:** Change the `WIDTH` and `HEIGHT` variables at the bottom of `mazesolver.py`.
- **Cell Size:** Adjust the `CELL_SIZE` constant for larger or smaller cells.
- **Add Algorithms:** Implement new algorithms by extending the `Maze` or `MazeApp` classes.

---

## License

This project is open source and available under the MIT License.