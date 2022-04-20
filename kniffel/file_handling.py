"""datei für file_handling"""
import json

def read_file_kniffel_player():
    """file lesen"""
    try:
        with open ('kniffel_player.json', 'r', encoding='utf8') as kniffel_player:
            player=json.load(kniffel_player)
    except IOError:
        print("IOError!")
    except ValueError:
        print("ValueError!")
    return player

def read_file_dice():
    """file lesen"""
    try:
        with open ('dice.json', 'r', encoding='utf8') as dice:
            dice_all = json.load(dice)
    except IOError:
        print("IOError!")
    except ValueError:
        print("ValueError!")
    return dice_all

def write_file_player(player):
    """file schreiben"""
    try:
        with open ('kniffel_player.json', 'w', encoding='utf8') as kniffel_player:
            json.dump(player, kniffel_player, indent=4)
        print("Automatisches Speichern erfolgreich!")
    except IOError:
        print("IOError!")
    except ValueError:
        print("ValueError!")

def write_file_dice(dice_all):
    """file schreiben"""
    try:
        with open ('dice.json', 'w', encoding='utf8') as dice:
            json.dump(dice_all, dice, indent=4)
    except IOError:
        print("IOError!")
    except ValueError:
        print("ValueError!")
