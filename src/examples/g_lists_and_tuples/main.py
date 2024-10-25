import lists
#main program

def main():
    class_list = [
        ['C++', [100, 80, 90, 70, 100], 0],
        ['Java', [90, 80, 50, 70, 60], 0],
        ['C#', [100, 50, 95, 0, 80], 0]
    ]

    print(class_list)
    print('---------------------------------')
    lists.calculate_student_grades(class_list)
    
    print(class_list)

    


    

main()