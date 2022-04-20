"""vorschlag für kniffel"""
import file_handling
import bottom_table_function
import table_handling
import backup_handling
import dice_functions
import print_table

#evtl. schönheit der arbeit: z.B. live summen,
#option alle würfel neu würfeln, bei spielende abfrage ob spiel erneut gestartet werden soll

def main():
    """hauptprogramm"""
    active_user = 0
    loop_control_main = 0
    loop_control_backup = 0
    print('Willkommen bei Kniffel!')
    while loop_control_backup == 0:
        backup_decision = input('\nMöchten Sie aus einem Backup laden? (j/n)\n')
        if backup_decision == 'n':
            backup_handling.delete_backup()
            loop_control_backup = 1
        elif backup_decision == 'j':
            print_table.ausgabe()
            active_user = backup_handling.analyse_backup()
            loop_control_backup = 1
        else:
            print('Bitte geben Sie n oder j ein!')
    while loop_control_main == 0:
        dice_functions.dices(active_user)
        table_handling.bonus(active_user)
        table_handling.sum_bottom_table(active_user)
        print_table.ausgabe()
        loop_control_main = table_handling.winner()
        active_user = act_user(active_user, loop_control_main)

def combine(active_user):
    """mit finalem wurf zahlen kombinieren"""
    dice_all=file_handling.read_file_dice()
    loop_control=0
    while loop_control==0:
        print(f'Die Würfel: {dice_all[0]},{dice_all[1]},{dice_all[2]},{dice_all[3]},{dice_all[4]}')
        print('Welche Kombination wählen Sie?\n1. 1er\n2. 2er\n3. 3er\n4. 4er\n5. 5er\n6. 6er')
        print('7. Dreierpasch\n8. Viererpasch\n9. Full House\n10. Kleine Straße')
        print('11. Große Straße\n12. Kniffel\n13. Chance\n14. Feld streichen')
        try:
            action_combine = int (input('\nIhre Wahl: '))
            if 1 <= action_combine <=6:
                loop_control=upper_table_function(active_user, action_combine)
            elif 7 <= action_combine <= 13:
                loop_control=bottom_table(action_combine, active_user)
            elif action_combine==14:
                loop_control=bottom_table_function.strikeout(active_user)
            else:
                print('\nGeben Sie bitte eine Zahl von 1-14 ein!')
        except ValueError:
            print('\nGeben Sie bitte eine Zahl ein!')

def upper_table_function(active_user, action_combine):
    """funktionen für obere Tabelle"""
    player=file_handling.read_file_kniffel_player()
    dice_all=file_handling.read_file_dice()
    if player[active_user][action_combine] == '-':
        count_elements=0
        for element in dice_all:
            if element==action_combine:
                count_elements= count_elements + 1
        sum_elements=count_elements*action_combine
        player[active_user][action_combine]=sum_elements
        print(sum_elements)
        file_handling.write_file_player(player)
        file_handling.write_file_dice(dice_all)
        return 1
    print('\nSie haben in das Feld breits etwas eingetragen!\n')
    return 0

def bottom_table(action_combine, active_user):
    """wegen pylint | optionen unterer teil der tabelle"""
    if action_combine==7:
        check = bottom_table_function.pasch_three(active_user)
    if action_combine==8:
        check = bottom_table_function.pasch_four(active_user)
    if action_combine==9:
        check = bottom_table_function.full_house(active_user)
    if action_combine==10:
        check = bottom_table_function.small_straight(active_user)
    if action_combine==11:
        check = bottom_table_function.large_straight(active_user)
    if action_combine==12:
        check = bottom_table_function.kniffel(active_user)
    if action_combine==13:
        check = bottom_table_function.chance(active_user)
    return check

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

if __name__ == '__main__':
    main()
