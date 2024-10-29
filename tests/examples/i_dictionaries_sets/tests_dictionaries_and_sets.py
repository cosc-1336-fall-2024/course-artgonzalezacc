import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_add_key_value_pair_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        expected_phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne', \
                              '555-4444':'Python'}
    
        key = '555-4444'
        value = 'Python'

        if key not in phonebook:
            phonebook[key] = value

        self.assertEqual(phonebook, expected_phonebook)

    def test_delete_key_value_pair_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        expected_phonebook = {'555-1111':'Chris', '555-3333':'Joanne'}

        key = '555-2222'
        
        if key in phonebook:
            del phonebook[key]

        self.assertEqual(phonebook, expected_phonebook)

    def test_update_value_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        expected_phonebook = {'555-1111':'Cris', '555-2222':'Katie', '555-3333':'Joanne'}

        key = '555-1111'
        value = 'Cris'

        if key in phonebook:
            phonebook[key] = value

        self.assertEqual(phonebook, expected_phonebook)

    def test_get_number_of_elements_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        key_value_count = len(phonebook)

        self.assertEqual(3, key_value_count)

    def test_different_data_type_values(self):
        test_scores = {'123':[88,92,100], '456':95, '789':'dropped'}
        expected_list = [88, 92, 100]
        list1 = test_scores['123']

        self.assertEqual(list1, expected_list)


