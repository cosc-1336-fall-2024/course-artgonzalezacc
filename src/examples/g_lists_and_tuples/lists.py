import array #PYthon library not in the core Python language

def test_config():
    return True

def create_array():
    nums = array.array('i', [1,2,3,4,5]) #create an array list
    
    for num in nums:
        print(num)

def access_array_elements():
    nums = array.array('i', [1,2,3,4,5]) #create an array list

    print(nums[0])
    print(nums[1])
    print(nums[2])

def loop_array_elements_while():
    nums = array.array('i', [1,2,3,4,5]) #create an array list
    indx = 0

    while(indx < len(nums)):
        print(nums[indx])
        indx += 1

def loop_array_elements_for_range():
    nums = array.array('i', [1,2,3,4,5]) #create an array list

    for indx in range(0, len(nums)):
        print(nums[indx])

def modify_array_element():
    nums = array.array('i', [1,2,3,4,5]) #create an array list

    print(nums[0])

    nums[0] = 10
    print(nums[0])

def add_array_elements():
    nums = array.array('i', [1,2,3,4,5]) #create an array list
    nums.append(6)

    for num in nums:
        print(num)

def delete_array_elements():
    nums = array.array('i', [1,2,3,4,5]) #create an array list
    
    nums.remove(3)

    for num in nums:
        print(num)

def get_total_of_array_elements():
    nums = array.array('i', [1,2,3,4,5]) #create an array list
    total = 0

    for num in nums:
        total += num

    return total

def create_list():
    list = [1,'bb', 5.5, True]

    print(list)

    for item in list:
        print(item)

def access_list_elements():
    list = [1,'bb', 5.5, True]

    print(list[0])    
    print(list[1])

def update_list_elements():
    list = [1,'bb', 5.5, True]

    print(list[0])    
    list[0] = 'abc'

    print(list[0])

def loop_list_items_w_while():
    list = [1,'bb', 5.5, True]
    indx = 0

    while(indx < len(list)):
        print(list[indx])
        indx += 1

def loop_list_items_w_for_range():
    list = [1,'bb', 5.5, True]

    for indx in range(0, len(list)):
        print(list[indx])

def use_list_as_parameter(list1, num):

    list1[0] = 100
    num = 25

def list_as_return_values(list1):
    list1[0] = 100

    return list1

def list_as_return_value_no_param():
    list1 = [5, 3, 10]

    return list1, id(list1)

def get_the_total_values_of_list_items_while():
    total = 0
    indx = 0
    list1 = [2, 4, 6, 8, 10]

    while(indx < len(list1)):
        total += list1[indx] #same as total = total + list1[indx]

        indx += 1

    return total

def get_the_total_values_of_list_items_for_range():
    total = 0
    list1 = [2, 4, 6, 8, 10]

    for i in range(0, len(list1)):
        total += list1[i]

    return total

def get_the_total_values_of_list_items_for():
    total = 0
    list1 = [2, 4, 6, 8, 10]

    for item in list1:
        total += item

    return total

def get_multiplication_table(rows, cols):
    list = []

    for i in range(0, rows):#loop all rows
        row_list = []

        for j in range(0, cols): #loop all cols
            row_list.append((i + 1) * (j + 1))

        list.append(row_list)    

    return list

def display_multiplication_table(list):

    for row_list in list:
        for item in row_list:
            print(str(item).rjust(3, " "), end = " ")

        print(" ")

def calculate_employee_gross_pay(payroll_list):

    for employee in payroll_list:
        employee[3] = employee[1] * employee[2]

def display_employee_payroll_list(payroll_list):

    for employee in payroll_list:
        print(employee[0], employee[1], employee[2], employee[3])

def calculate_student_grades(class_list):

    for student in class_list:
        lowest = min(student[1])
        #print( get_grades_total(student[1])-lowest, '/',  len(student[1])-1)
        #print((get_grades_total(student[1])-lowest) / len(student[1])-1)
        student[2] = (get_grades_total(student[1])-lowest) / (len(student[1])-1)

def get_grades_total(grade_list):
    total = 0

    for grade in grade_list:
        total += grade
    
    return total