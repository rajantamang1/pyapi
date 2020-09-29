#!/usr/bin/env python3
import argparse, socket
from datetime import datetime


def hero(heroinput, statinput):
    print(f"{heroinput.capitalize()}'s {statinput} is: {main_dictionary[heroinput][statinput]}")

if __name__ == '__main__':
    main_dictionary = {"flash": {"speed": "fastest", "intelligence": "lowest", "strength": "lowest"},
                       "batman": {"speed": "slowest", "intelligence": "highest", "strength": "money"},
                       "superman": {"speed": "fast", "intelligence": "average", "strength": "strongest"}}


    parser = argparse.ArgumentParser(description='Stat of Hero')
    parser.add_argument('-role', choices=main_dictionary['flash']['speed'], help='which character to select') 
    parser.add_argument('stat', choices=main_dictionary['flash'].keys(), help='which character to select')
    
args = parser.parse_args()
hero(args.role,args.stat)

