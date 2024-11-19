class BankAccount:

    __balance = 0 #class variable-attributes-data PRIVATE

    #constructor --- function
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amt):
        if(amt > 0):
            self.__balance += amt

