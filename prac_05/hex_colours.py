"""
CP1404/CP5632 Practical 5
Hex Colours Dictionary Lookup
"""

colour_codes = {
        'blue': '#0018a8',
        'cyan': '#00ffff',
        'crimson': '#dc143c',
        'daffodil': '#ffff31',
        'ebony': '555d50',
        'emerald': '#50c878',
        'firebrick': '#ff3030',
        'gray': '#bebebe',
        'heliotrope': '#df73ff',
        'magenta': '#ff00ff'
        }

while True:
    try:
        colour_choice = input('Select your colour:').lower()
        if colour_choice == '':
            break
        print(f'The code for {colour_choice} is {colour_codes[colour_choice]}')
        break
    except KeyError:
        print("Colour not in the list")

