import unittest

from src.examples.g_lists_and_tuples.lists import get_total_of_array_elements, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_total_of_array_elements(self):
        total = get_total_of_array_elements()

        self.assertEqual(total, 15)
