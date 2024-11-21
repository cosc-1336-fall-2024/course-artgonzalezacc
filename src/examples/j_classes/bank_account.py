import random

class BankAccount:

    __balance = 0 #class variable-attributes-data PRIVATE
    __cust_id = 123456

    #constructor --- function-executes on instance/object/variable creation one time
    def __init__(self, balance):
        
        if(balance == 0):
            self.__get_balance_from_db()    
        else:
            self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amt):
        if(amt > 0):
            self.__balance += amt

    def withdraw(self, amt):
        if(amt > 0 and amt <= self.__balance):
            self.__balance -= amt

    def __get_balance_from_db(self):
        self.__balance = random.randint(1, 10000)

