import unittest

from src.examples.j_classes.account_free_functions import get_account_object, make_deposit
from src.examples.j_classes.bank_account import BankAccount
from src.examples.j_classes.bank_account_db import BankAccountDB

class Test_Config(unittest.TestCase):

    def test_account_begin_balance(self):
        account = BankAccount(1000)
        self.assertEqual(1000, account.get_balance())

    def test_account_deposit(self):
        account = BankAccount(1000) #created instance/object --- variable

        self.assertEqual(1000, account.get_balance())

        account.deposit(100)

        self.assertEqual(1100, account.get_balance())

    def test_account_withdraw(self):
        account = BankAccount(1000)

        self.assertEqual(1000, account.get_balance())

        account.withdraw(100)

        self.assertEqual(900, account.get_balance())

    def test_account_deposit_withdraw(self):
        account = BankAccount(1000)

        self.assertEqual(1000, account.get_balance())

        account.deposit(100)
        self.assertEqual(1100, account.get_balance())

        account.withdraw(50)
        self.assertEqual(1050, account.get_balance())

    def test_account_withdraw_deposit(self):

        account = BankAccount(1000)

        self.assertEqual(1000, account.get_balance())

        account.withdraw(100)
        self.assertEqual(900, account.get_balance())

        account.deposit(200)
        self.assertEqual(1100, account.get_balance())

    def test_account_object_as_parameter(self):
        account = BankAccount(500)
        self.assertEqual(500, account.get_balance())

        make_deposit(account)

        self.assertEqual(600, account.get_balance())

    def test_account_as_return_value(self):
        account = BankAccount(500)
        print(id(account))

        a = get_account_object(account)
        print(id(a))

        self.assertEqual(500, account.get_balance())

    def test_account_get_balance_from_db(self):
        accountDB = BankAccountDB()
        balance = accountDB.get_current_balance()

        account = BankAccount(balance)

        self.assertEqual(True, account.get_balance() >= 1)
        self.assertEqual(True, account.get_balance() <= 10000)


