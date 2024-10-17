import unittest

from src.examples.g_lists_and_tuples.lists import get_total_of_array_elements, test_config, use_list_as_parameter

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_total_of_array_elements(self):
        total = get_total_of_array_elements()

        self.assertEqual(total, 15)

    def test_list_copy_memory(self):
        list1 = [5, 4, 10]
        list2 = list1 #no real copy created. list1 and list2 point to the same list in memory

        self.assertEqual(True, list1 == list2)
        list1[0] = 20

        #self.assertEqual(True, list1 != list2)

        self.assertEqual(True, list1[0] == list2[0])

    def test_list_copy_w_loop(self):
        list1 = [5, 4, 10]
        list2 = []

        for item in list1:
            list2.append(item)

        self.assertEqual(True, list1 == list2)#is it comparing values or the memory location?

        list1[0] = 20

        #self.assertEqual(True, list1 == list2)
        self.assertEqual(False, list1[0] == list2[0])

    def test_list_concatenate(self):
        list1 = [5, 4, 10]
        list2 = []
        list3 = list1 + list2

        self.assertEqual(True, list1 == list3)

        list1[0] = 20

        self.assertEqual(False, list1 == list3)

        self.assertEqual(False, list1[0] == list3[0])

    def test_list_repetition_operator(self):
        list1 = [0] * 5
        expected_list = [0,0,0,0,0]

        self.assertEqual(True, list1 == expected_list)

        list1 = [1,2,3] * 2
        expected_list = [1,2,3,1,2,3]

        self.assertEqual(True, list1 == expected_list)

    def test_list_in_key_word(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']

        self.assertEqual(True, 'V475' in prod_nums)
        self.assertEqual(False, 'v475' in prod_nums)

    def test_list_not_in_key_word(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']

        self.assertEqual(True, 'v475' not in prod_nums)
        self.assertEqual(False, 'V475' not in prod_nums)

    def test_list_clear_items(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']
        prod_nums.clear()

        self.assertEqual(True, prod_nums == [])

    def test_list_sort_function(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']
        prod_nums.sort()
        expected_list = ['F987', 'Q143', 'R688', 'V475']

        self.assertEqual(True, prod_nums == expected_list)

    def test_list_remove_item(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']
        prod_nums.remove('F987')
        expected_list = ['V475', 'Q143', 'R688']

        self.assertEqual(True, prod_nums == expected_list)

    def test_list_as_function_parameters(self):
        num = 1
        list1 = [5, 3, 10]

        use_list_as_parameter(list1, num)

        self.assertEqual(True, num == 1)
        self.assertEqual(True, list1[0] == 100)

