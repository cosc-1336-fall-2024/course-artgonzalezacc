import decisions

def main():
    num = int(input("Enter a number: "))

    is_even = decisions.is_number_even(num)

    if(is_even):
        print(num, 'Even')
        print('------')

main()#run our program

