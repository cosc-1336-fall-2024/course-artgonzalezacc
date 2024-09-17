def test_config():
    return True

def print_hello():
    num = 5
    indx = 0

    while (indx < num):
        print(indx, (indx < num), 'hello')
        indx = indx + 1#statement that makes indx < num FALSE
