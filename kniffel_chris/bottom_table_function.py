"""datei für funktionen der unteren tabelle"""
import numpy as np
import file_handling

def pasch_three(active_user):
    """Dreierpasch (prüfen und in tabelle eintragen)"""
    player=file_handling.read_file_kniffel_player()
    dice_all=file_handling.read_file_dice()
    if player[active_user][10] == '-':
        el_eins = dice_all[0]
        el_zwei = dice_all[1]
        el_drei = dice_all[2]
        if dice_all.count(el_eins)>=3 or dice_all.count(el_zwei)>=3 or dice_all.count(el_drei)>=3:
            dice_count=0
            sum_dice=0
            while dice_count <= 4:
                sum_dice = sum_dice + dice_all[dice_count]
                dice_count = dice_count + 1
            player[active_user][10]=sum_dice
            file_handling.write_file_player(player)
            file_handling.write_file_dice(dice_all)
            return 1
        print('\nEs ist kein Dreierpasch möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def pasch_four(active_user):
    """Viererpasch (prüfen und in tabelle eintragen)"""
    player=file_handling.read_file_kniffel_player()
    dice_all=file_handling.read_file_dice()
    if player[active_user][11] == '-':
        el_eins = dice_all[0]
        el_zwei = dice_all[1]
        if dice_all.count(el_eins)>=4 or dice_all.count(el_zwei)>=4:
            dice_count=0
            sum_dice=0
            while dice_count <= 4:
                sum_dice = sum_dice + dice_all[dice_count]
                dice_count = dice_count + 1
            player[active_user][11]=sum_dice
            file_handling.write_file_player(player)
            file_handling.write_file_dice(dice_all)
            return 1
        print('\nEs ist kein Viererpasch möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def full_house(active_user):
    """Full House (prüfen und in tabelle eintragen)"""
    player=file_handling.read_file_kniffel_player()
    dice_all=file_handling.read_file_dice()
    if player[active_user][12] == '-':
        dice_all_sorted = np.sort(dice_all)
        el_eins = dice_all_sorted[0]
        el_zwei = dice_all_sorted[3]
        if dice_all.count(el_eins)==3 and dice_all.count(el_zwei)==2:
            player[active_user][12] = 25
            file_handling.write_file_player(player)
            file_handling.write_file_dice(dice_all)
            return 1
        if dice_all.count(el_eins)==2 and dice_all.count(el_zwei)==3:
            player[active_user][12] = 25
            file_handling.write_file_player(player)
            file_handling.write_file_dice(dice_all)
            return 1
        print('\nEs ist kein Full House möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def small_straight(active_user):
    """kleine Straße (prüfen und in tabelle eintragen)"""
    player=file_handling.read_file_kniffel_player()
    dice_all=file_handling.read_file_dice()
    if player[active_user][13] == '-':
        if (1 in dice_all) and (2 in dice_all) and (3 in dice_all) and (4 in dice_all):
            player[active_user][13]=30
            file_handling.write_file_player(player)
            file_handling.write_file_dice(dice_all)
            return 1
        if (2 in dice_all) and (3 in dice_all) and (4 in dice_all) and (5 in dice_all):
            player[active_user][13]=30
            file_handling.write_file_player(player)
            file_handling.write_file_dice(dice_all)
            return 1
        if (3 in dice_all) and (4 in dice_all) and (5 in dice_all) and (6 in dice_all):
            player[active_user][13]=30
            file_handling.write_file_player(player)
            file_handling.write_file_dice(dice_all)
            return 1
        print('\nKeine kleine Straße möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def large_straight(active_user):
    """große Straße (prüfen und in tabelle eintragen)"""
    player=file_handling.read_file_kniffel_player()
    d_a=file_handling.read_file_dice()
    if player[active_user][14] == '-':
        if (1 in d_a) and (2 in d_a) and (3 in d_a) and (4 in d_a) and (5 in d_a):
            player[active_user][14]=40
            file_handling.write_file_player(player)
            file_handling.write_file_dice(d_a)
            return 1
        if (2 in d_a) and (3 in d_a) and (4 in d_a) and (5 in d_a) and (6 in d_a):
            player[active_user][14]=40
            file_handling.write_file_player(player)
            file_handling.write_file_dice(d_a)
            return 1
        print('\nKeine große Straße möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def kniffel(active_user):
    """Kniffel (prüfen und in tabelle eintragen)"""
    player=file_handling.read_file_kniffel_player()
    dice_all=file_handling.read_file_dice()
    check=dice_all[0]
    if dice_all[1]==check and dice_all[2]==check and dice_all[3]==check and dice_all[4]==check:
        if player[active_user][15] == '-':
            player[active_user][15]=50
            file_handling.write_file_player(player)
            file_handling.write_file_dice(dice_all)
            return 1
        player[active_user][15]=player[active_user][15] + 50
        file_handling.write_file_player(player)
        file_handling.write_file_dice(dice_all)
        bonus_kniffel(active_user, check)
        return 1
    print('\nKein Kniffel möglich!\n')
    return 0

def bonus_kniffel(active_user, check):
    """ wenn feld der kniffel-augenzahl frei: kniffel wert gesetzt, wenn belegt: dazu addiert"""
    player=file_handling.read_file_kniffel_player()
    if player[active_user][check]=='-':
        player[active_user][check] = check*5
    else:
        player[active_user][check] = player[active_user][check] + check*5
    file_handling.write_file_player(player)

def chance(active_user):
    """Chance (prüfen und in tabelle eintragen)"""
    player=file_handling.read_file_kniffel_player()
    dice_all=file_handling.read_file_dice()
    if player[active_user][16] == '-':
        dice_count=0
        sum_dice=0
        while dice_count <= 4:
            sum_dice = sum_dice + dice_all[dice_count]
            dice_count = dice_count + 1
        player[active_user][16]=sum_dice
        file_handling.write_file_player(player)
        file_handling.write_file_dice(dice_all)
        return 1
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def strikeout(active_user):
    """feld streichen (auswahl + 0 eintragen)"""
    player=file_handling.read_file_kniffel_player()
    loop_control=0
    while loop_control==0:
        try:
            choice_field = int (input('''Welches Feld möchten Sie streichen?
            \r7. Dreierpasch\n8. Viererpasch\n9. Full House\n10. Kleine Straße
            \r11. Große Straße\n12. Kniffel\n13. Chance\n14. keins\n'''))
            if player[active_user][choice_field+3] == '-':
                if 7 <= choice_field <=13:
                    player[active_user][choice_field+3]=0
                    file_handling.write_file_player(player)
                    loop_control=1
                    return 1
                if choice_field == 14:
                    return 0
                print('Bitte geben Sie eine Zahl zischen 7 und 14 ein!\n')
            else:
                print('\nSie können das Feld nicht streichen, da bereits etwas eingetragen ist!\n')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein!\n')
