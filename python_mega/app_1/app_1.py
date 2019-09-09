import json
from difflib import get_close_matches

"""
Word meaning dictionary with word similarity.
"""

def load_json(key):

    with open("data.json") as dt_file:
        data = json.load(dt_file)

    key = key.lower()
    if key in data.keys():
        return data[key]
    else:
        similar = get_close_matches(key, data.keys(), cutoff=0.8)
        if similar:
            corr = input(f"Did you mean {similar[0]}?\nEnter Y/N: ")
            if corr == 'Y':
                return data[similar[0]]
            return "Could not find anything similar. Check your spelling."
        else:
            return 'The word does not exists.'


input_val = input('Enter word: ')
result = load_json(input_val)

if isinstance(result, list):
    for i in result:
        print(i)
else:
    print(result)