import lists
#main program

def main():
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    item = input("Enter item: ")

    if(item in prod_nums):
        prod_nums.remove(item)
    else:
        print(item, "not in list")

    print(prod_nums)    

main()