"""summen tabelle und gewinner werden ermittelt"""
import print_table_change_user
import file_handling

def bonus(active_user):
    """prüfen, ob mindestpunktzahl für bonus (oberer tabelle ; 63P) erreicht + summe eintragen"""
    player=file_handling.read_file_kniffel_player()
    bonus_count = 1
    count_value = 0
    sum_six_coloums = 0
    #prüfen, ob alle 6 felder belegt
    while bonus_count <= 6:
        if player[active_user][bonus_count] != '-':
            count_value = count_value + 1
        bonus_count = bonus_count + 1
    #alle felder addieren
    bonus_count = 1
    if count_value == 6:
        while bonus_count <= 6:
            sum_six_coloums = sum_six_coloums + player[active_user][bonus_count]
            bonus_count = bonus_count + 1
        player[active_user][8] = sum_six_coloums
        if sum_six_coloums >= 63:
            player[active_user][7] = 35
            player[active_user][9] = sum_six_coloums + 35
        else:
            player[active_user][7] = 0
            player[active_user][9] = sum_six_coloums
    file_handling.write_file_player(player)

def sum_bottom_table(active_user):
    """summe für unteren teil"""
    player=file_handling.read_file_kniffel_player()
    sum_count = 10
    count_value = 0
    sum_six_coloums = 0
    #prüfen, ob alle 7 felder belegt
    while sum_count <= 16:
        if player[active_user][sum_count] != '-':
            count_value = count_value + 1
        sum_count = sum_count + 1
    #alle felder addieren
    sum_count = 10
    if count_value == 7:
        while sum_count <= 16:
            sum_six_coloums = sum_six_coloums + player[active_user][sum_count]
            sum_count = sum_count + 1
        player[active_user][17] = sum_six_coloums
    file_handling.write_file_player(player)

def winner():
    """geiwnner wird ermittelt und ausgegeben, spiel wird beendet"""
    player=file_handling.read_file_kniffel_player()
    if player[0][9]!='-' and player[0][17]!='-' and player[1][9]!='-' and player[1][17]!='-':
        total_sum_one = player[0][9] + player[0][17]
        total_sum_two = player[1][9] + player[1][17]
        player[0][18]=total_sum_one
        player[1][18]=total_sum_two
        if total_sum_one > total_sum_two:
            print(f'Wow, {player[0][0]} hat gewonnen!')
        elif total_sum_two > total_sum_one:
            print(f'Wow, {player[1][0]} hat gewonnen!')
        else:
            print('Wahnsinn... ein Unentschieden!!')
        file_handling.write_file_player(player)
        print_table_change_user.ausgabe()
        return 1
    return 0
