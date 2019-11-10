"""Unit Tests for Dice Module."""
import unittest
import dice

class TestDice(unittest.TestCase):
    """Test the Dice module."""

    def test_default(self):
        """Test default aspect of a die."""
        die = dice.Die()
        self.assertTrue(die in range(1, 6 + 1))

    def test_roll(self):
        """Test the roll() function of a die."""
        die = dice.Die(6)
        self.assertTrue(die.roll() in range(1, 6 + 1))


if __name__ == "__main__":
    unittest.main()
