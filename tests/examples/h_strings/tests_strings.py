import unittest

from src.examples.h_strings.strings import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_string_concatenation(self):
        lang = "Python"
        result = lang + " is easy to learn"

        self.assertEqual(result, "Python is easy to learn")

    def test_string_is_alphanum(self):
        str = "Cpp"

        self.assertEqual(True, str.isalnum())

        str = "Cpp123"
        self.assertEqual(True, str.isalnum())

        str = "Cpp#"
        self.assertEqual(False, str.isalnum())

    def test_string_is_alpha(self):
        str = "Cpp"

        self.assertEqual(True, str.isalpha())

        str = "Cpp123"

        self.assertEqual(False, str.isalpha())

    def test_substring_in_string(self):
        text = 'Four score and seven years ago'

        self.assertEqual(True, 'seven' in text)
        self.assertEqual(False, 'Seven' in text)

    def test_substring_not_in_string(self):
        text = 'Four score and seven years ago'

        self.assertEqual(False, 'seven' not in text)
        self.assertEqual(True, 'Seven' not in text)




