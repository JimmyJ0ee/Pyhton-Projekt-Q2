"""datei für file handling, also alles was mit dateien zu tun hat"""
import json
import sys

def read_file_kniffel_player():
    """file kniffel_player lesen"""
    try:
        with open ('kniffel_player.json', 'r', encoding='utf8') as kniffel_player:
            player=json.load(kniffel_player)
            return player
    except IOError:
        print("IOError!")
        sys.exit()
    except ValueError:
        print("ValueError!")
        sys.exit()

def read_file_dice():
    """file dice lesen"""
    try:
        with open ('dice.json', 'r', encoding='utf8') as dice:
            dice_all = json.load(dice)
            return dice_all
    except IOError:
        print("IOError!")
        sys.exit()
    except ValueError:
        print("ValueError!")
        sys.exit()

def write_file_player(player):
    """file kniffel_player schreiben"""
    try:
        with open ('kniffel_player.json', 'w', encoding='utf8') as kniffel_player:
            json.dump(player, kniffel_player, indent=4)
    except IOError:
        print("IOError!")
        sys.exit()
    except ValueError:
        print("ValueError!")
        sys.exit()

def write_file_dice(dice_all):
    """file dice schreiben"""
    try:
        with open ('dice.json', 'w', encoding='utf8') as dice:
            json.dump(dice_all, dice, indent=4)
    except IOError:
        print("IOError!")
        sys.exit()
    except ValueError:
        print("ValueError!")
        sys.exit()
