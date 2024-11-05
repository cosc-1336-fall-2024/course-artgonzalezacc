import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_union_of_a_set(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        expected_set = set([1,2,3,4,5,6])
        union_set = set1.union(set2) # set1 | set2

        self.assertEqual(expected_set, union_set)

    def test_intersection_of_a_set(self):
        set1 = set() #empty set
        set1.add(1)
        set1.add(2)
        set1.add(3)
        set1.add(4)
        set2 = set([3,4,5,6])
        expected_set = set([3,4])
        intersection_set = set1.intersection(set2) #set1 & set2

        self.assertEqual(expected_set, intersection_set)

    def test_difference_of_sets(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        expected_set = set([1,2])

        difference_set = set1.difference(set2) #set1 - set2

        self.assertEqual(expected_set, difference_set)

    def test_symmetric_difference_sets(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        expected_set = set([1,2,5,6])

        symm_diff_set = set1.symmetric_difference(set2) #set1 ^ set2

        self.assertEqual(expected_set, symm_diff_set)

    def test_is_subset(self):
        set1 = set([1,2,3,4])
        set2 = set([2,3])

        self.assertEqual(True, set2.issubset(set1))

    def test_is_superset(self):
        set1 = set([1,2,3,4])
        set2 = set([2,3])

        self.assertEqual(True, set1.issuperset(set2))



    




