def infinite_loop():
    while True:
        print('Hello')

def print_hello(): #runaway recursion - fills stack memory - program crashes
    print('Hello')

    print_hello()

def print_hello_x_times(num):
    
    if(num == 0): #base case
        return

    print('Hello')

    print(num, 'load to stack: ')
    print_hello_x_times(num - 1)
    print(num, 'unload from stack: ')

def factorial(num):

    if(num == 0 or num == 1):
        print("return value: ", 1, " num: ", num)
        return 1
    
    print("load stack", "num", num)
    return_value = num * factorial(num - 1)
    print("unload stack", "return value: ", return_value, " num: ", num)
    return return_value

    

    