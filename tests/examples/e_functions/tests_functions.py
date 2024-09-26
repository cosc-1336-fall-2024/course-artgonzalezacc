import unittest

from src.examples.e_functions.value_return_functions import test_config, get_random_value

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_random_number(self):
        
        for i in range(0, 10):
            number = get_random_value(1, 100)
            self.assertEqual(True, (number >= 1))
            self.assertEqual(True, (number <= 100))

