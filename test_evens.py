import unittest
from evens import even_number_of_events

class TestEvens(unittest.TestCase):
    
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_events, 4)

    
    def test_values_in_list(self):
        self.assertEqual(even_number_of_events([]), False)
        self.assertEqual(even_number_of_events([2, 4]), True)
        self.assertEqual(even_number_of_events([2]), False)
        self.assertEqual(even_number_of_events([1, 3, 5]), False)


if __name__ == '__main__':
    unittest.main()