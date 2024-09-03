import input_process_output

def main():
    value1 = int(input("Enter value1: "))
    value2 = int(input("Enter value2: "))

    result1 = input_process_output.float_division(value1, value2)
    result2 = input_process_output.integer_division(value1, value2)

    print(result1, result2)

main() #run the main function 
