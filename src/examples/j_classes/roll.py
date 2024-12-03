class Roll:

    def __init__(self, die1, die2):
        self.__die1 = die1
        self.__die2 = die2
        self.__rolled_value = die1.roll() + die2.roll()

    def roll_value(self):
        return self.__rolled_value