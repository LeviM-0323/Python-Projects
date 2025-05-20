# Snake AI Project

This project implements a classic Snake game in Pygame, enhanced with a reinforcement learning AI agent that learns to play Snake using Q-learning. The AI agent can save and load its progress, allowing it to improve over time and eventually master the game.

---

## Features

- **Classic Snake Gameplay:** Faithful to the original, with a grid-based play area and simple graphics.
- **AI Agent:** Uses Q-learning to learn optimal strategies for playing Snake.
- **Persistent Learning:** The agent's knowledge (Q-table and exploration rate) is saved with `pickle` and loaded automatically.
- **Win Condition:** The game recognizes when the snake fills the board (all but one segment) and displays a "Winner found" message.
- **Customizable Parameters:** Easily adjust grid size, snake speed, and segment size for different difficulty levels.

---

## Project Structure

```
PythonProjects/SnakeAI/
│
├── snake.py           # Main implementation: game logic, AI agent, training loop
├── requirements.txt   # List of dependencies for the project
├── q_table.pkl        # Pickle file of previous runs best agent
├── training_log.txt   # Text file for training data logging
└── README.md          # Project documentation
```

---

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/LeviM-0323/Python-Projects.git
   cd PythonProjects/SnakeAI
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

---

## Usage

To run the Snake game with AI training enabled:
```
python snake.py
```
- The AI will play and learn automatically. Progress is saved after each episode.
- To watch the AI play, set `use_ai = True` in `snake.py`.
- To play manually, set `use_ai = False`.

---

## How It Works

- **Game Logic:** The game is built with Pygame and uses a grid defined by `window_x`, `window_y`, and `SEGMENT_SIZE`.
- **AI Agent:** The Q-learning agent observes the game state and chooses actions to maximize its score.
- **Saving Progress:** The agent's Q-table and exploration rate (`epsilon`) are saved to `q_table.pkl` after each episode and loaded on startup.
- **Win Condition:** If the snake fills the board (maximum possible length), the game freezes and displays "Winner found" on the screen and in the terminal.

---

## Customization

- **Change Game Size:** Edit `window_x`, `window_y`, and `SEGMENT_SIZE` in `snake.py`.
- **Adjust AI Parameters:** Modify learning rate, discount factor, or exploration rate in the `QLearningAgent` class.
- **Training Log:** Progress is logged to `training_log.txt`.

---

## Resetting Agent

To reset the learning data of the AI agent, delete `q_table.pkl` and `training_log.txt` (optional) before running the script again.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for suggestions, bug fixes, or improvements.

---

## License

This project is open source and available under the MIT License.