import lists
#main program

def main():
    payroll_list = [
        ['C++', 40, 20, 0],
        ['Java', 35, 25, 0],
        ['C#', 40, 30, 0]
    ]

    lists.display_employee_payroll_list(payroll_list)
    print('------------------------')
    lists.calculate_employee_gross_pay(payroll_list)

    lists.display_employee_payroll_list(payroll_list)


    

main()