import array #PYthon library not in the core Python language

def test_config():
    return True

def create_array():
    nums = array.array('i', [1,2,3,4,5]) #create an array list
    
    for num in nums:
        print(num)