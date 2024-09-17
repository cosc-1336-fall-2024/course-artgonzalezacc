def test_config():
    return True

def print_hello():
    num = 5
    indx = 0

    while (indx < num):
        print(indx, (indx < num), 'hello')
        indx = indx + 1#statement that makes indx < num FALSE

#3 -> 1*1 +2*2+3*3 = 14   ----- num = 3    total = total + num * num 
def sum_of_squares(num):
    total = 0

    while num > 0:
        total = total + num * num 
        print(num, num > 0, total)
        num = num - 1 #statement that makes the boolean expression false; stops the the loop

    return total

def sum_of_squares_indx(num):
    indx = 0
    total = 0

    while indx <= num:
        total = total + indx * indx
        indx = indx + 1

    return total

