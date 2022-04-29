"""datei für alle funktionen der würfel"""
import random
import function_decision
import file_handling

def dices(active_user):
    """simuliert würfeln"""
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    dice_three = random.randint(1,6)
    dice_four = random.randint(1,6)
    dice_five = random.randint(1,6)
    dice = [dice_one, dice_two, dice_three, dice_four, dice_five]
    file_handling.write_file_dice(dice)
    action_count = 1
    print(f'Die Würfel: {dice[0]}  {dice[1]}  {dice[2]}  {dice[3]}  {dice[4]}')
    while action_count<=2:
        try:
            action_text = input('Welche(n) Würfel möchten Sie erneut würfeln? (0 für <keinen>)\n')
            action_numbers = []
            for element in action_text.split():
                if element.isdigit() and (element not in action_numbers):
                    if 0 <= int(element) <= 5:
                        action_numbers.append(element)
                    else:
                        raise ValueError
                else:
                    raise ValueError
            if action_numbers[0]!='0':
                dice_new(action_numbers)
            else:
                function_decision.combine(active_user)
                break
            dice=file_handling.read_file_dice()
            print(f'Neuer Wurf: {dice[0]}  {dice[1]}  {dice[2]}  {dice[3]}  {dice[4]}')
            action_count = action_count+1
        except IndexError:
            print('Bitte geben Sie Zahlen ein!')
        except ValueError:
            print('Bitte geben Sie eine Zahl von 0-5 und diese nur einmal ein!')
    if action_count==3: #max anz züge erreicht
        function_decision.combine(active_user)

def dice_new(action_numbers):
    """würfel neu würfeln"""
    dice_all=file_handling.read_file_dice()
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
    file_handling.write_file_dice(dice_all)
