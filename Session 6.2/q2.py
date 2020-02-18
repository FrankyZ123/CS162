'''
This is a short python program intended to query Pokemon data
and print that pokemon's base stats.
'''

import requests, string

pokemon_type = input("What pokemon do you want me to look for: ")

r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{(pokemon_type).lower()}').json()

print(f"Here are the keys I found {[*r]}")
r_key = input("Enter the key you'd like to query: ")

try:
    print(r[r_key])
except:
    print("Oops yikers I'm a shell of a script")