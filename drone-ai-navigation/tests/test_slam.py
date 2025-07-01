import unittest
from src.vision.slam import SLAM

class TestSLAM(unittest.TestCase):

    def setUp(self):
        self.slam = SLAM()

    def test_initialize(self):
        self.slam.initialize()
        self.assertIsNotNone(self.slam.map)
        self.assertEqual(self.slam.position, (0, 0))

    def test_update_map(self):
        initial_map = self.slam.map.copy()
        self.slam.update_map((1, 1), "obstacle")
        self.assertNotEqual(initial_map, self.slam.map)

    def test_get_position(self):
        self.slam.initialize()
        position = self.slam.get_position()
        self.assertEqual(position, (0, 0))

if __name__ == '__main__':
    unittest.main()