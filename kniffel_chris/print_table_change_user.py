"""funktion für ausgabe der tabelle und weschsel des users"""
import file_handling

def act_user(active_user, loop_control):
    """aktiver user wird gewechselt"""
    player=file_handling.read_file_kniffel_player()
    if active_user==0:
        active_user=1
    else:
        active_user=0
    if loop_control==0:
        print(f'{player[active_user][0]} ist an der Reihe!\n\n')
    return active_user

def ausgabe():
    """ausgabe der kniffel-tabelle"""
    player=file_handling.read_file_kniffel_player()
    print('\nKNIFFEL:')
    print(f'\t\t\t{player[0][0]}\t\t{player[1][0]}')
    print(f'\n1er:\t\t\t{player[0][1]}\t\t{player[1][1]}')
    print(f'2er:\t\t\t{player[0][2]}\t\t{player[1][2]}')
    print(f'3er:\t\t\t{player[0][3]}\t\t{player[1][3]}')
    print(f'4er:\t\t\t{player[0][4]}\t\t{player[1][4]}')
    print(f'5er:\t\t\t{player[0][5]}\t\t{player[1][5]}')
    print(f'6er:\t\t\t{player[0][6]}\t\t{player[1][6]}')
    print(f'Summe oben:\t\t{player[0][8]}\t\t{player[1][8]}')
    print(f'Bonus:\t\t\t{player[0][7]}\t\t{player[1][7]}')
    print(f'Summe oben ges.:\t{player[0][9]}\t\t{player[1][9]}')
    print(f'\nDreierpasch:\t\t{player[0][10]}\t\t{player[1][10]}')
    print(f'Viererpasch:\t\t{player[0][11]}\t\t{player[1][11]}')
    print(f'Full House:\t\t{player[0][12]}\t\t{player[1][12]}')
    print(f'Kleine Straße:\t\t{player[0][13]}\t\t{player[1][13]}')
    print(f'Große Straße:\t\t{player[0][14]}\t\t{player[1][14]}')
    print(f'Kniffel:\t\t{player[0][15]}\t\t{player[1][15]}')
    print(f'Chance:\t\t\t{player[0][16]}\t\t{player[1][16]}')
    print(f'Summe unten:\t\t{player[0][17]}\t\t{player[1][17]}')
    print(f'Summe oben ges.:\t{player[0][9]}\t\t{player[1][9]}')
    print(f'Summe gesamt:\t\t{player[0][18]}\t\t{player[1][18]}\n\n')
