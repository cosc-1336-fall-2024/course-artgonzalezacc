#
GLOBAL_INT = 100 #CONSTANT
GLOBAL_INT = 1000 #honor system - it can be changed

def hello_world():
    global GLOBAL_INT #i want to override the global GLOBAL_INT VARIABLE
    GLOBAL_INT = 5000 
    print(GLOBAL_INT)
    print('Hello world!')

def display_number():
    num = 5 #local variable
    print(num)
    print(GLOBAL_INT)

def show_numbers(num): #parameter(variable)
    num1 = 5 #local variable
    print("show_numbers", num, num1)
    print(GLOBAL_INT)

def local_and_params(num1):
    print("local_and_params0" ,num1)
    num1 = 10
    print("local_and_params1" ,num1)
    print(GLOBAL_INT)