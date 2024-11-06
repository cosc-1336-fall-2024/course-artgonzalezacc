#main program


def main():
    baseball = set(['Jodi','Carmen','Aida','Alicia'])
    basketball=set(['Eva','Carmen','Alicia','Sarah'])

    print('The following play baseball but not basketball')
    baseball_only = baseball.difference(basketball)
    for player in baseball_only:
        print(player)

    print('only one sport list: ')
    only_one_sport_set = baseball.symmetric_difference(basketball)
    for player in only_one_sport_set:
        print(player)
    

main()