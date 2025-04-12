import unittest
from yatzy import Yatzy

class TestYatzy(unittest.TestCase):
    def test_roll_initial_dice(self):
        game = Yatzy()
        self.assertEqual(len(game.dice), 5)

    def test_scoring_ones(self):
        game = Yatzy()
        game.dice = [1, 1, 3, 4, 5]
        self.assertEqual(game.ones(), 2)

    def test_scoring_sixes(self):
        game = Yatzy()
        game.dice = [6, 6, 6, 1, 2]
        self.assertEqual(game.sixes(), 18)

if __name__ == "__main__":
    unittest.main()
