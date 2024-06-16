# test_game.py
import unittest
import game


class TestGame(unittest.TestCase):
    def test_get_computer_choice(self):
        # Test if the function returns one of the valid choices
        self.assertIn(game.get_computer_choice(), ["rock", "paper", "scissors"])

    def test_compare_choices(self):
        # Test all possible scenarios
        self.assertEqual(game.compare_choices("rock", "scissors"), "You win!")
        self.assertEqual(game.compare_choices("rock", "paper"), "You lose!")
        self.assertEqual(game.compare_choices("rock", "rock"), "It's a tie!")
        self.assertEqual(game.compare_choices("paper", "rock"), "You win!")
        self.assertEqual(game.compare_choices("paper", "scissors"), "You lose!")
        self.assertEqual(game.compare_choices("paper", "paper"), "It's a tie!")
        self.assertEqual(game.compare_choices("scissors", "paper"), "You win!")
        self.assertEqual(game.compare_choices("scissors", "rock"), "You lose!")
        self.assertEqual(game.compare_choices("scissors", "scissors"), "It's a tie!")
        self.assertEqual(game.compare_choices("inv", "rock"), "Invalid choice!")


if __name__ == "__main__":
    unittest.main()
