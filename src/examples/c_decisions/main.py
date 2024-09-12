import decisions

def main():
    year = int(input("Enter a year: "))

    generation = decisions.get_generation(year)

    print(year, generation)

main()#run our program

