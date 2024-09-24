#
def hello_world():
    print('Hello world!')

def display_number():
    num = 5 #local variable
    print(num)

def show_numbers(num): #parameter(variable)
    num1 = 5 #local variable
    print("show_numbers", num, num1)

def local_and_params(num1):
    print("local_and_params0" ,num1)
    num1 = 10
    print("local_and_params1" ,num1)