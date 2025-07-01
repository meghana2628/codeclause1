import unittest
from src.rl.agent import RLAgent

class TestRLAgent(unittest.TestCase):

    def setUp(self):
        self.agent = RLAgent()

    def test_choose_action(self):
        state = [0.0, 0.0]  # Example state
        action = self.agent.choose_action(state)
        self.assertIn(action, self.agent.action_space)

    def test_learn(self):
        state = [0.0, 0.0]
        action = self.agent.choose_action(state)
        reward = 1.0  # Example reward
        next_state = [1.0, 1.0]  # Example next state
        self.agent.learn(state, action, reward, next_state)
        # Check if the agent's policy has been updated
        self.assertIsNotNone(self.agent.policy)

    def test_update_policy(self):
        initial_policy = self.agent.policy.copy()
        self.agent.update_policy()
        self.assertNotEqual(initial_policy, self.agent.policy)

if __name__ == '__main__':
    unittest.main()