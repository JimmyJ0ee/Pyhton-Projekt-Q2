"""mainfunktion von kniffel"""
import table_handling
import backup_handling
import dice_functions
import print_table_change_user

def main():
    """hauptprogramm"""
    active_user = 0
    loop_control_main = 0
    loop_control_backup = 0
    print('''\nWillkommen bei Kniffel!\n\nKleine Info: um Würfel erneut zu würfeln ist es wichtig,
    \rdass die Stelle des Würfels eingegeben wird.
    \rSie wollen z.B. den 3. und 5. Würfel neu eingeben? Geben Sie wie folgt ein: 3 5
    \rDas Spiel kann jederzeit mit der Kombination strg + c unterbrochen
    \rund später wiederhergestellt werden\n''')
    while loop_control_backup == 0:
        backup_decision = input('Möchten Sie aus einem Backup laden? (j/n)\n')
        if backup_decision == 'n':
            backup_handling.delete_backup()
            loop_control_backup = 1
        elif backup_decision == 'j':
            print_table_change_user.ausgabe()
            active_user = backup_handling.analyse_backup()
            loop_control_backup = 1
        else:
            print('Bitte geben Sie n oder j ein!')
    while loop_control_main == 0:
        dice_functions.dices(active_user)
        table_handling.bonus(active_user)
        table_handling.sum_bottom_table(active_user)
        print_table_change_user.ausgabe()
        loop_control_main = table_handling.winner()
        active_user = print_table_change_user.act_user(active_user, loop_control_main)

if __name__ == '__main__':
    main()
