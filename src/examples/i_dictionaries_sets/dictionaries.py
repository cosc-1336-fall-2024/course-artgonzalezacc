def test_config():
    return True

def use_a_dictionary():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
    print(phonebook)

    print(phonebook['555-2222'])
    print(phonebook['555-1111'])     
    print(phonebook['555-3333'])
    #print(phonebook['555-1112']) generates a KeyError--key doesn't exist