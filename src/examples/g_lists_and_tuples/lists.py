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
