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

def for_range_display_numbers(num):

    for val in range(0, num):
        print(val+1)

def for_sum_of_squares(num):
    total = 0

    for val in range(0, num):
        total = total +  (val+1) * (val+1)   

    return total

def for_sum_of_squares_2(num):
    total = 0

    for val in range(1, num + 1):
        total = total + val * val

    return total

def nested_while_loop():

    outer_loops = 3
    outer_indx = 0

    while(outer_indx < outer_loops): #iterate three times
        inner_loops = 3
        inner_indx = 0
        print("Outer Loop", outer_indx, outer_indx < outer_loops)

        while(inner_indx < inner_loops):
            print("\tInner Loop", inner_indx, inner_indx < inner_loops)
            inner_indx += 1 #same as inner_indx = inner_indx + 1

        outer_indx += 1

def while_multiplication_table(row, col):

    r = 0

    while(r < row):
        c = 0

        while(c < col):
            product = (r + 1) * (c + 1)
            print(str(product).rjust(3, " "), end = " ")
            c += 1

        r += 1

        print(" ")



