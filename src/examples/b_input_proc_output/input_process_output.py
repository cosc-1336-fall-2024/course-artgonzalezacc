INTEREST_RATE = .059 #named constant

#output comments variables input calculations output constants
def display_output():
    print('hello')

def test_config():
    return True

def float_division(value1, value2): #parameters(variables)
    return value1 / value2 #float division(decimals)

def integer_division(value1, value2): #value return functions (fruitful)
    return value1 // value2 #integer (whole number division) doesn't include decimal portion

def use_named_constant(): #void function doesn't return a value
    amount = 1000 * INTEREST_RATE
    print(amount)

def use_local_variables_int():
    num = 10 #create an int(whole number) variable 
    print(num)
    print(num + 10) #math operation

def use_local_variables_str():
    num = '10' #create an int(whole number) variable 
    print(num)
    print(num + '10') #string concatenation

def use_reuse_local_variable():
    str1 = 'Python' #assign a value
    print(str1)

    str1 = 'C++' #reassign a value
    print(str1)

def use_reuse_local_variable_data_type():
    num = 10 #whole number --- int
    print(num + 15) #math operation

    num = 10.99 #(float)
    print(num + .49)

    num = 'python' #string data type
    print(num)