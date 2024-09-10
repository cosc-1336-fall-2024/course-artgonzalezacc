import unittest

from src.examples.c_decisions.decisions import test_config, is_number_in_range

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_logical_and_truth_table(self):
        self.assertEqual(False, False and False)
        self.assertEqual(False, False and True)
        self.assertEqual(False, True and False)
        self.assertEqual(True, True and True)

    def test_logical_or_truth_table(self):
        self.assertEqual(False, False or False)
        self.assertEqual(True, False or True)
        self.assertEqual(True, True or False)
        self.assertEqual(True, True or True)

    def test_logical_not_truth_table(self):
        self.assertEqual(False, not True)
        self.assertEqual(True, not False)

