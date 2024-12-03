import unittest

from src.examples.j_classes.account_free_functions import get_account_object, make_deposit
from src.examples.j_classes.bank_account import BankAccount
from src.examples.j_classes.bank_account_db import BankAccountDB
from src.examples.j_classes.die import Die
from src.examples.j_classes.roll import Roll

class Test_Config(unittest.TestCase):

    def test_die_rolls_1_to_6(self):
        die = Die()

        for i in range(0, 12):
            roll_value = die.roll()
            self.assertEqual(True, roll_value >= 1)
            self.assertEqual(True, roll_value <= 6)

    def test_rolls(self):
        die1 = Die()
        die2 = Die()

        for i in range(0, 24):
            roll = Roll(die1, die2)

            self.assertEqual(True, roll.roll_value() >= 2)
            self.assertEqual(True, roll.roll_value() <= 12)