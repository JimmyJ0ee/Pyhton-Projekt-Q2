"""vorschlag für kniffel"""
import table_handling
import backup_handling
import dice_functions
import print_table_change_user

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
