import unittest

import numpy as np

from shapley import calculate_shapley_values


class TestShapleyMethods(unittest.TestCase):
    def setUp(self):
        self.test_players = None
        self.test_values = None
        self.expected_shapley_values = None

    def assertShapleyValues(self):
        shapley_values = calculate_shapley_values(self.test_players, self.test_values)
        self.assertTrue(np.allclose(shapley_values, self.expected_shapley_values))

    def test_one_player(self):
        """Test Shapley values for one player."""
        self.test_players = 1
        self.test_values = [100]
        self.expected_shapley_values = [100]
        self.assertShapleyValues()

    def test_two_player(self):
        """Test Shapley values for two players."""
        self.test_players = 2
        self.test_values = [98, 240, 495]
        self.expected_shapley_values = [176.5, 318.5]
        self.assertShapleyValues()

    def test_three_player(self):
        """Test Shapley values for three players."""
        self.test_players = 3
        self.test_values = [418000000, 74200000, 28800000, 500090000, 499395020, 0, 576585020]
        self.expected_shapley_values = [480942510.0, 59345000.0, 36297510.0]
        self.assertShapleyValues()

    def test_four_player(self):
        """Test Shapley values for four players."""
        self.test_players = 4
        self.test_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 500]
        self.expected_shapley_values = [87.5, 114.16666666667, 137.5, 160.83333333333]
        self.assertShapleyValues()


if __name__ == '__main__':
    unittest.main()