#!/usr/bin/env python
"""
    Runs as a command line script
"""
import sys
import requests

class bcolors:
    """
        Add color properties to prnt statements
    """
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    UNDERLINE = '\033[4m'
    WARNING = '\033[93m'

def get_word(word):
    """
        Searches for word and gets a response from urbandictionary API
    """
    req = requests.get(
        'http://api.urbandictionary.com/v0/define?', {'term': word})
    return req.json()['list']


def print_definitions(word):
    """
        Loops through first 3 results and prints them out to console
    """
    definitions = get_word(word)

    if len(definitions) >= 3:
        defLength = 3
        print(f'You entered "{word}" and these are the top 3 results:\n')
    elif len(definitions) == 0:
        print(bcolors.FAIL + "ERROR: " + bcolors.ENDC + "No entries found, for " + bcolors.HEADER + word + bcolors.ENDC)
        get_input()
    else:
        defLength = len(definitions)

    for i in range(0, defLength):
        obj = definitions[i]

        print('========================================================')
        print(f'Word: ' + bcolors.HEADER + str(obj["word"]) + bcolors.ENDC)
        print(f'Definition: ' + bcolors.HEADER + obj["definition"] + bcolors.ENDC)
        print(f'Score: {obj["thumbs_up"] - obj["thumbs_down"]}')
        print('Ayys: ' + bcolors.OKGREEN + str(obj["thumbs_up"]) + bcolors.ENDC + ' | Nayys: ' + bcolors.FAIL + str(obj["thumbs_down"]) + bcolors.ENDC)

def get_input():
    """
        Parent function for this script.
        Gets input string from user and returns 3 definitions.
    """
    while True:
        print('========================================================')
        words_to_lookup = input('Slng: ')

        if not words_to_lookup:
            print(
                'You didn\'t enter anything.  Please enter a search string.')
        elif words_to_lookup == 'exit':
            sys.exit()
        elif words_to_lookup:
            print_definitions(words_to_lookup)
        else:
            print(f'Did not recognize command {words_to_lookup} \n')

get_input()
