# rl_agent.py
import numpy as np
import random

class SimpleRLAgent:
    def __init__(self):
        self.q_table = np.zeros((5, 5, 4))  # Grid 5x5, 4 directions

    def choose_action(self, state):
        return np.argmax(self.q_table[state])

    def update(self, state, action, reward, new_state):
        self.q_table[state][action] = reward + 0.9 * np.max(self.q_table[new_state])
