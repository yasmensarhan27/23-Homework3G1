import unittest
import math

# Define the function to calculate the periodic time
def calculate_periodic_time(l):
    """Calculates the periodic time of a simple pendulum.

    Args:
        l: The length of the pendulum in meters.

    Returns:
        The periodic time of the pendulum in seconds.
    """
    # Acceleration due to gravity in meters per second squared.
    g = 9.81
    
    # Calculate the periodic time using the formula
    periodic_time = 2 * math.pi * math.sqrt(l / g)
    
    return periodic_time

class TestCalculatePeriodicTime(unittest.TestCase):

    def test_calculate_periodic_time(self):
        # Test cases with known results
        test_cases = [
            (0.5, 2.007),  # (length, expected_periodic_time)
            (1.0, 4.498),
            (1.5, 6.283),
            (2.0, 8.987),
            (2.5, 11.178)
        ]

        # Perform the tests
        for length, expected_periodic_time in test_cases:
            result = calculate_periodic_time(length)
            self.assertAlmostEqual(result, expected_periodic_time, delta=0.001)

if __name__ == '__main__':
    unittest.main()
