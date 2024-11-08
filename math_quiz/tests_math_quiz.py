import unittest
from math_quiz import random_int, random_operation, calculation_func


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        # Test if random_operation returns a valid operator
        valid_operations = ['+', '-', '*']
        for _ in range(1000):  # Check multiple times for randomness
            operation = random_operation()
            self.assertIn(operation, valid_operations)

    def test_calculation_func(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, 5, '+', '2 + 5', 7),
                (8, 6, '+', '8 + 6', 14),
                (5, 2, '-', '5 - 2', 3),
                (2, 5, '-', '2 - 5', -1),
                (8, 6, '-', '8 - 6', 2),
                (5, 2, '*', '5 * 2', 10),
                (2, 5, '*', '2 * 5', 7),
                (8, 6, '*', '8 * 6', 48),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer= calculation_func(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
