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

