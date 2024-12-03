from src.examples.j_classes.die import Die
from src.examples.j_classes.player import Player

def main():
    die1 = Die()
    die2 = Die()

    player = Player()

    choice = 'Y'

    while choice == 'Y' or choice == 'y':
        roll = player.roll_dice(die1, die2)

        print("player rolled: ", roll.roll_value())

        choice = input('Enter y to roll again: ')


main()
