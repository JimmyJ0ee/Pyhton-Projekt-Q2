"""vorschlag für kniffel"""
import json
import random
import numpy as np

#good to know für eingabe neue würfel: leerzeichen vor und nach nummer des würfels
#bsp: 2. und 4. würfel neu: '2 4' dann enter (auch: '2 und 4' davor/danach leer, rest egal)
#zu tun: evtl klassen, testfunktion
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
            delete_backup()
            loop_control_backup = 1
        elif backup_decision == 'j':
            ausgabe()
            active_user = analyse_backup()
            loop_control_backup = 1
        else:
            print('Bitte geben Sie n oder j ein!')
    while loop_control_main == 0:
        dices(active_user)
        bonus(active_user)
        sum_bottom_table(active_user)
        ausgabe()
        loop_control_main = winner()
        active_user = act_user(active_user, loop_control_main)

def delete_backup():
    """backup löschen + eingabe der spielernamen"""
    with open ('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    player[0][0] = input('Name Spieler 1: ')
    player[1][0] = input('Name Spieler 2: ')
    print('_______________________________________\n\n')
    count_reset_player_one = 1
    count_reset_player_two = 1
    while count_reset_player_one <= 18:
        player[0][count_reset_player_one] = '-'
        count_reset_player_one = count_reset_player_one + 1
    while count_reset_player_two <= 18:
        player[1][count_reset_player_two] = '-'
        count_reset_player_two = count_reset_player_two + 1
    with open ('kniffel_player.json', 'w') as kniffel_player:
        json.dump(player, kniffel_player, indent=4)

def analyse_backup():
    """herausfinden welcher user dran + aktuelle tabelle printen"""
    with open ('kniffel_player.json', 'r') as kniffel_input:
        player=json.load(kniffel_input)
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

def dices(active_user):
    """simuliert würfeln"""
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    dice_three = random.randint(1,6)
    dice_four = random.randint(1,6)
    dice_five = random.randint(1,6)
    dice_all = [dice_one, dice_two, dice_three, dice_four, dice_five]
    with open ('dice.json', 'w') as dice:
        json.dump(dice_all, dice, indent=4)
    action_count = 1
    print(f'Die Würfel: {dice_all[0]}  {dice_all[1]}  {dice_all[2]}  {dice_all[3]}  {dice_all[4]}')
    while action_count<=2:
        action_text = input('Welche(n) Würfel möchten Sie erneut würfeln? (0 für <keinen>)\n')
        action_numbers = []
        for element in action_text.split():
            if element.isdigit():
                action_numbers.append(element)
        if action_numbers[0]!='0':
            dice_new(action_numbers)
        else:
            combine(active_user)
            break
        with open ('dice.json', 'r') as dice:
            dice_all = json.load(dice)
        print(f'Neuer Wurf: {dice_all[0]},{dice_all[1]},{dice_all[2]},{dice_all[3]},{dice_all[4]}')
        action_count = action_count+1
    if action_count==3: #max anz züge erreicht
        combine(active_user)

def dice_new(action_numbers):
    """würfel neu würfeln"""
    with open ('dice.json', 'r') as dice:
        dice_all = json.load(dice)
    for element in action_numbers:
        if element=='1':
            dice_all[0] = random.randint(1,6)
        if element=='2':
            dice_all[1] = random.randint(1,6)
        if element=='3':
            dice_all[2] = random.randint(1,6)
        if element=='4':
            dice_all[3] = random.randint(1,6)
        if element=='5':
            dice_all[4] = random.randint(1,6)
    with open ('dice.json', 'w') as dice:
        json.dump(dice_all, dice, indent=4)

def combine(active_user):
    """mit finalem wurf zahlen kombinieren"""
    with open('dice.json', 'r') as dice_input:
        dice_all=json.load(dice_input)
    loop_control=0
    while loop_control==0:
        print(f'Die Würfel: {dice_all[0]},{dice_all[1]},{dice_all[2]},{dice_all[3]},{dice_all[4]}')
        print('Welche Kombination wählen Sie?\n1. 1er\n2. 2er\n3. 3er\n4. 4er\n5. 5er\n6. 6er')
        print('7. Dreierpasch\n8. Viererpasch\n9. Full House\n10. Kleine Straße')
        print('11. Große Straße\n12. Kniffel\n13. Chance\n14. Feld streichen')
        try:
            action_combine = int (input('\nIhre Wahl: '))
            if 1 <= action_combine <=6:
                loop_control=upper_table(action_combine, active_user)
            elif 7 <= action_combine <= 13:
                loop_control=bottom_table(action_combine, active_user)
            elif action_combine==14:
                loop_control=strikeout(active_user)
            else:
                print('\nGeben Sie bitte eine Zahl von 1-14 ein!')
        except ValueError:
            print('\nGeben Sie bitte eine Zahl ein!')

def upper_table(action_combine, active_user):
    """wegen pylint | optionen oberer teil der tabelle"""
    check = upper_table_function(active_user, action_combine)
    return check

def bottom_table(action_combine, active_user):
    """wegen pylint | optionen unterer teil der tabelle"""
    if action_combine==7:
        check = pasch_three(active_user)
    if action_combine==8:
        check = pasch_four(active_user)
    if action_combine==9:
        check = full_house(active_user)
    if action_combine==10:
        check = small_straight(active_user)
    if action_combine==11:
        check = large_straight(active_user)
    if action_combine==12:
        check = kniffel(active_user)
    if action_combine==13:
        check = chance(active_user)
    return check

def upper_table_function(active_user, action_combine):
    """funktionen für obere Tabelle"""
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    with open('dice.json', 'r') as dice:
        dice_all=json.load(dice)
    if player[active_user][action_combine] == '-':
        count_elements=0
        for element in dice_all:
            if element==action_combine:
                count_elements= count_elements + 1
        sum_elements=count_elements*action_combine
        player[active_user][action_combine]=sum_elements
        print(sum_elements)
        with open ('kniffel_player.json', 'w') as kniffel_player:
            json.dump(player, kniffel_player, indent=4)
        with open ('dice.json', 'w') as dice:
            json.dump(dice_all, dice, indent=4)
        return 1
    print('\nSie haben in das Feld breits etwas eingetragen!\n')
    return 0

def pasch_three(active_user):
    """Dreierpasch"""
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    with open('dice.json', 'r') as dice:
        dice_all=json.load(dice)
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
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(dice_all, dice, indent=4)
            return 1
        print('\nEs ist kein Dreierpasch möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def pasch_four(active_user):
    """Viererpasch"""
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    with open('dice.json', 'r') as dice:
        dice_all=json.load(dice)
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
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(dice_all, dice, indent=4)
            return 1
        print('\nEs ist kein Viererpasch möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def full_house(active_user):
    """Full House"""
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    with open('dice.json', 'r') as dice:
        dice_all=json.load(dice)
    if player[active_user][12] == '-':
        dice_all_sorted = np.sort(dice_all)
        el_eins = dice_all_sorted[0]
        el_zwei = dice_all_sorted[3]
        if dice_all.count(el_eins)==3 and dice_all.count(el_zwei)==2:
            player[active_user][12] = 25
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(dice_all, dice, indent=4)
            return 1
        if dice_all.count(el_eins)==2 and dice_all.count(el_zwei)==3:
            player[active_user][12] = 25
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(dice_all, dice, indent=4)
            return 1
        print('\nEs ist kein Full House möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def small_straight(active_user):
    """kleine Straße"""
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    with open('dice.json', 'r') as dice:
        dice_all=json.load(dice)
    if player[active_user][13] == '-':
        if (1 in dice_all) and (2 in dice_all) and (3 in dice_all) and (4 in dice_all):
            player[active_user][13]=30
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(dice_all, dice, indent=4)
            return 1
        if (2 in dice_all) and (3 in dice_all) and (4 in dice_all) and (5 in dice_all):
            player[active_user][13]=30
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(dice_all, dice, indent=4)
            return 1
        if (3 in dice_all) and (4 in dice_all) and (5 in dice_all) and (6 in dice_all):
            player[active_user][13]=30
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(dice_all, dice, indent=4)
            return 1
        print('\nKeine kleine Straße möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def large_straight(active_user):
    """große Straße"""
    #statt dice all, d_a da pylint sonst line too long
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    with open('dice.json', 'r') as dice:
        d_a=json.load(dice)
    if player[active_user][14] == '-':
        if (1 in d_a) and (2 in d_a) and (3 in d_a) and (4 in d_a) and (5 in d_a):
            player[active_user][14]=40
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(d_a, dice, indent=4)
            return 1
        if (2 in d_a) and (3 in d_a) and (4 in d_a) and (5 in d_a) and (6 in d_a):
            player[active_user][14]=40
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(d_a, dice, indent=4)
            return 1
        print('\nKeine große Straße möglich!\n')
        return 0
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def kniffel(active_user):
    """Kniffel"""
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    with open('dice.json', 'r') as dice:
        dice_all=json.load(dice)
    check=dice_all[0]
    if dice_all[1]==check and dice_all[2]==check and dice_all[3]==check and dice_all[4]==check:
        if player[active_user][15] == '-':
            player[active_user][15]=50
            with open ('kniffel_player.json', 'w') as kniffel_player:
                json.dump(player, kniffel_player, indent=4)
            with open ('dice.json', 'w') as dice:
                json.dump(dice_all, dice, indent=4)
            return 1
        player[active_user][15]=player[active_user][15] + 50
        with open ('kniffel_player.json', 'w') as kniffel_player:
            json.dump(player, kniffel_player, indent=4)
        with open ('dice.json', 'w') as dice:
            json.dump(dice_all, dice, indent=4)
        bonus_kniffel(active_user, check)
        return 1
    print('\nKein Kniffel möglich!\n')
    return 0

def bonus_kniffel(active_user, check):
    """interpretation: wenn feld frei: kniffel als max wert gesetzt, wenn belegt: addiert"""
    #check als input spart dice-datei einlesen, plus variable neu declarieren
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    if player[active_user][check]=='-':
        player[active_user][check] = check*5
    else:
        player[active_user][check] = player[active_user][check] + check*5
    with open ('kniffel_player.json', 'w') as kniffel_player:
        json.dump(player, kniffel_player, indent=4)

def chance(active_user):
    """Chance"""
    with open('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
    with open('dice.json', 'r') as dice:
        dice_all=json.load(dice)
    if player[active_user][16] == '-':
        dice_count=0
        sum_dice=0
        while dice_count <= 4:
            sum_dice = sum_dice + dice_all[dice_count]
            dice_count = dice_count + 1
        player[active_user][16]=sum_dice
        with open ('kniffel_player.json', 'w') as kniffel_player:
            json.dump(player, kniffel_player, indent=4)
        with open ('dice.json', 'w') as dice:
            json.dump(dice_all, dice, indent=4)
        return 1
    print('\nSie haben in das Feld bereits etwas eingetragen!\n')
    return 0

def strikeout(active_user):
    """feld streichen"""
    with open('kniffel_player.json', 'r') as player_input:
        player = json.load(player_input)
    loop_control=0
    while loop_control==0:
        try:
            print('Welches Feld möchten Sie streichen?')
            print('7. Dreierpasch\n8. Viererpasch\n9. Full House\n10. Kleine Straße')
            choice_field = int (input('11. Große Straße\n12. Kniffel\n13. Chance\n'))
            if player[active_user][choice_field+3] == '-':
                if 7 <= choice_field <=13:
                    player[active_user][choice_field+3]=0
                    with open('kniffel_player.json', 'w') as kniffel_player:
                        json.dump(player, kniffel_player, indent=4)
                    loop_control=1
                    return 1
                print('Bitte geben Sie eine Zahl zischen 7 und 13 ein!\n')
            else:
                print('\nSie können das Feld nicht streichen, da bereits etwas eingetragen ist!\n')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein!\n')

def bonus(active_user):
    """prüfen, ob mindestpunktzahl (63) für bonus erreicht"""
    with open('kniffel_player.json', 'r') as player_input:
        player = json.load(player_input)
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
    with open('kniffel_player.json', 'w') as kniffel_player:
        json.dump(player, kniffel_player, indent=4)

def sum_bottom_table(active_user):
    """summe für unteren teil"""
    with open('kniffel_player.json', 'r') as player_input:
        player = json.load(player_input)
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
    with open('kniffel_player.json', 'w') as kniffel_player:
        json.dump(player, kniffel_player, indent=4)

def winner():
    """geiwnner wird ermittelt und ausgegeben, plus spiel beendet"""
    with open('kniffel_player.json', 'r') as player_input:
        player = json.load(player_input)
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
        with open('kniffel_player.json', 'w') as kniffel_player:
            json.dump(player, kniffel_player, indent=4)
        ausgabe()
        return 1
    return 0

def ausgabe():
    """ausgabe der kniffel-tabelle"""
    with open ('kniffel_player.json', 'r') as kniffel_player:
        player=json.load(kniffel_player)
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

def act_user(active_user, loop_control):
    """aktiver user wird gewechselt"""
    with open('kniffel_player.json', 'r') as player_input:
        player=json.load(player_input)
    if active_user==0:
        active_user=1
    else:
        active_user=0
    if loop_control==0:
        print(f'{player[active_user][0]} ist an der Reihe!\n\n')
    return active_user

if __name__ == '__main__':
    main()
