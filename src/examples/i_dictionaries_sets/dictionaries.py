def test_config():
    return True

def use_a_dictionary():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
    print(phonebook)

    print(phonebook['555-2222'])
    print(phonebook['555-1111'])     
    print(phonebook['555-3333'])
    
    if('555-1112' in phonebook):
        print(phonebook['555-1112'])
    else:
        print('Key does not exist') 

def add_key_value_pair():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
    
    key = input("Enter the key: ")
    value = input("Enter the value: ")

    if key not in phonebook:
        phonebook[key] = value
    else:
        print(key, " already exists.")

    print(phonebook)

def delete_key_value_pair():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
    
    key = input("Enter the key: ")

    if key in phonebook:
        del phonebook[key]
    else:
        print("Key ", key, " does not exist.")

    print(phonebook)

def update_value():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

    key = input("Enter the key: ")
    value = input("Enter the new value: ")

    if key in phonebook:
        phonebook[key] = value
    else:
        print("Key ", key, " does not exist.")
    
    print(phonebook)

def loop_dictionary_w_for():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

    for key in phonebook:
        print(phonebook[key])