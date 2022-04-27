"""datei für backup handling"""
import file_handling

def delete_backup():
    """backup löschen + eingabe der spielernamen"""
    player=file_handling.read_file_kniffel_player()
    player[0][0] = input('\nName Player 1: ')
    player[1][0] = input('\nName Player 2: ')
    print('_______________________________________\n\n')
    count_reset_player_one = 1
    count_reset_player_two = 1
    while count_reset_player_one <= 18:
        player[0][count_reset_player_one] = '-'
        count_reset_player_one = count_reset_player_one + 1
    while count_reset_player_two <= 18:
        player[1][count_reset_player_two] = '-'
        count_reset_player_two = count_reset_player_two + 1
    file_handling.write_file_player(player)

def analyse_backup():
    """herausfinden welcher user an der reihe + ausgeben wer dran ist"""
    player=file_handling.read_file_kniffel_player()
    count_element_player_one=0
    count_player_one=1
    while count_player_one <=6:
        if player[0][count_player_one] != '-':
            count_element_player_one = count_element_player_one+1
        count_player_one=count_player_one+1
    count_player_one=10
    while count_player_one <=16:
        if player[0][count_player_one] != '-':
            count_element_player_one = count_element_player_one+1
        count_player_one=count_player_one+1
    count_element_player_two=0
    count_player_two=1
    while count_player_two <=6:
        if player[1][count_player_two] != '-':
            count_element_player_two = count_element_player_two+1
        count_player_two=count_player_two+1
    count_player_two=10
    while count_player_two <=16:
        if player[1][count_player_two] != '-':
            count_element_player_two = count_element_player_two+1
        count_player_two=count_player_two+1
    if count_element_player_one > count_element_player_two:
        print(f'{player[1][0]} ist an der Reihe!')
        return 1
    if count_element_player_one == count_element_player_two:
        print(f'{player[0][0]} ist an der Reihe!')
        return 0
