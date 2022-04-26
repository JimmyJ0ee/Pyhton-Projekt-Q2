"""datei für entscheidung der aktion des users"""
import file_handling
import bottom_table_function

def combine(active_user):
    """endgültige augenzahlen kombinieren"""
    dice_all=file_handling.read_file_dice()
    loop_control=0
    while loop_control==0:
        print(f'''\nDie finalen Würfel:
        \r{dice_all[0]}  {dice_all[1]}  {dice_all[2]}  {dice_all[3]}  {dice_all[4]}
        \rWelche Kombination wählen Sie?\n1. 1er\n2. 2er\n3. 3er\n4. 4er\n5. 5er\n6. 6er
        \r7. Dreierpasch\n8. Viererpasch\n9. Full House\n10. Kleine Straße\n11. Große Straße
        \r12. Kniffel\n13. Chance\n14. Feld streichen''')
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
    """funktion für optionen der oberen Tabelle"""
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
    """optionen unterer teil der tabelle"""
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
