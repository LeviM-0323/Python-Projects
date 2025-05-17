import pygame
import time
import random
import numpy as np

snake_speed = 15

window_x = 480
window_y = 360

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("AI Snake")
        self.game_window = pygame.display.set_mode((window_x, window_y))
        self.fps = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.snake_position = [100, 50]
        self.snake_body = [
            [100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
        ]
        self.fruit_position = [random.randrange(1, (window_x//10)) * 10,
                               random.randrange(1, (window_y//10)) * 10]
        self.fruit_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.game_over_flag = False
        # Return initial state
        return self._get_state()

    def step(self, action=None):
        reward = -0.1  # Small negative reward for each step
        prev_distance = abs(self.snake_position[0] - self.fruit_position[0]) + abs(self.snake_position[1] - self.fruit_position[1])
        if action:
            self.change_to = action

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    self.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    self.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    self.change_to = 'RIGHT'

        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        if self.direction == 'UP':
            self.snake_position[1] -= 10
        if self.direction == 'DOWN':
            self.snake_position[1] += 10
        if self.direction == 'LEFT':
            self.snake_position[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_position[0] += 10

        self.snake_body.insert(0, list(self.snake_position))
        if self.snake_position[0] == self.fruit_position[0] and self.snake_position[1] == self.fruit_position[1]:
            self.score += 10
            reward = 100  # reward for eating fruit
            self.fruit_spawn = False
        else:
            self.snake_body.pop()

        if not self.fruit_spawn:
            self.fruit_position = [random.randrange(1, (window_x//10)) * 10,
                                   random.randrange(1, (window_y//10)) * 10]
        self.fruit_spawn = True

        # Optional: reward for getting closer to the fruit
        new_distance = abs(self.snake_position[0] - self.fruit_position[0]) + abs(self.snake_position[1] - self.fruit_position[1])
        if new_distance < prev_distance:
            reward += 0.1  # smaller bonus for moving closer

        self.game_window.fill(black)
        for pos in self.snake_body:
            pygame.draw.rect(self.game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.game_window, white, pygame.Rect(self.fruit_position[0], self.fruit_position[1], 10, 10))

        # Check for game over
        if (self.snake_position[0] < 0 or self.snake_position[0] > window_x-10 or
            self.snake_position[1] < 0 or self.snake_position[1] > window_y-10):
            self.game_over_flag = True
            reward = -10  # penalty for dying
        for block in self.snake_body[1:]:
            if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                self.game_over_flag = True
                reward = -10  # penalty for dying

        self.show_score(1, white, 'times new roman', 20)
        pygame.display.update()
        self.fps.tick(snake_speed)

        # Return state, reward, done, info
        return self._get_state(), reward, self.game_over_flag, {}

    def _get_state(self):
        head_x, head_y = self.snake_position
        fruit_x, fruit_y = self.fruit_position

        # Danger straight, right, left
        danger_straight = self._danger_in_direction(self.direction)
        danger_right = self._danger_in_direction(self._turn_right(self.direction))
        danger_left = self._danger_in_direction(self._turn_left(self.direction))

        # Fruit location relative to head
        fruit_left = fruit_x < head_x
        fruit_right = fruit_x > head_x
        fruit_up = fruit_y < head_y
        fruit_down = fruit_y > head_y

        # State as a tuple of booleans
        return (
            danger_straight,
            danger_right,
            danger_left,
            self.direction,
            fruit_left,
            fruit_right,
            fruit_up,
            fruit_down
        )

    def _danger_in_direction(self, direction):
        x, y = self.snake_position
        if direction == 'UP':
            y -= 10
        elif direction == 'DOWN':
            y += 10
        elif direction == 'LEFT':
            x -= 10
        elif direction == 'RIGHT':
            x += 10
        # Check wall collision
        if x < 0 or x >= window_x or y < 0 or y >= window_y:
            return True
        # Check self collision
        if [x, y] in self.snake_body:
            return True
        return False

    def _turn_right(self, direction):
        return {'UP': 'RIGHT', 'RIGHT': 'DOWN', 'DOWN': 'LEFT', 'LEFT': 'UP'}[direction]

    def _turn_left(self, direction):
        return {'UP': 'LEFT', 'LEFT': 'DOWN', 'DOWN': 'RIGHT', 'RIGHT': 'UP'}[direction]

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score: ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score Is: ' + str(self.score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01):
        self.q_table = {}  # state -> action values
        self.actions = actions
        self.alpha = alpha      # learning rate
        self.gamma = gamma      # discount factor
        self.epsilon = epsilon  # exploration rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

    def get_state_key(self, state):
        return state

    def choose_action(self, state):
        state_key = self.get_state_key(state)
        if np.random.rand() < self.epsilon or state_key not in self.q_table:
            return random.choice(self.actions)
        return max(self.q_table[state_key], key=self.q_table[state_key].get)

    def learn(self, state, action, reward, next_state, done):
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)
        if state_key not in self.q_table:
            self.q_table[state_key] = {a: 0.0 for a in self.actions}
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = {a: 0.0 for a in self.actions}
        q_predict = self.q_table[state_key][action]
        if done:
            q_target = reward
        else:
            q_target = reward + self.gamma * max(self.q_table[next_state_key].values())
        self.q_table[state_key][action] += self.alpha * (q_target - q_predict)
        # Decay epsilon
        if done and self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

def get_random_action(current_direction):
    actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    # Prevent the snake from reversing directly
    if current_direction == 'UP':
        actions.remove('DOWN')
    elif current_direction == 'DOWN':
        actions.remove('UP')
    elif current_direction == 'LEFT':
        actions.remove('RIGHT')
    elif current_direction == 'RIGHT':
        actions.remove('LEFT')
    return random.choice(actions)

if __name__ == "__main__":
    log_file = open("training_log.txt", "a")
    use_ai = True
    actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    agent = QLearningAgent(actions)
    episode = 0

    while True:
        episode += 1
        game = SnakeGame()
        state = game.reset()
        total_reward = 0
        while not game.game_over_flag:
            if use_ai:
                action = agent.choose_action(state)
                next_state, reward, done, info = game.step(action)
                agent.learn(state, action, reward, next_state, done)
                state = next_state
            else:
                state, reward, done, info = game.step()
            total_reward += reward

        print(f"Episode {episode} | Score: {game.score} | Total Reward: {total_reward} | Epsilon: {agent.epsilon:.3f}")
        log_file.write(f"Episode {episode} | Score: {game.score} | Total Reward: {total_reward} | Epsilon: {agent.epsilon:.3f}\n")
        log_file.flush()  # Ensure it's written to disk
        time.sleep(0.1)

    log_file.close()