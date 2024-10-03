def test_config():
    return True

def string_access_a_character():
    lang = "C++"

    print(lang)

    print(lang[0])
    print(lang[1])
    print(lang[2])

    #lang[0] = 'c' cannot modify individual characters in a string 

def loop_a_string_w_while():
    lang = "Python"
    indx = 0

    while(indx < len(lang)):
        print(lang[indx])
        indx += 1 # index = index + 1

def loop_a_string_w_for_range():
    lang = "Python"

    for i in range(0, len(lang)):
        print(lang[i])
    
    