#!/usr/bin/python3

import requests
import pandas as pd

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        print(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

    # Use the PokeAPI to export a list of all Pokemon as plaintext, JSON, and Excel formats. 
    pokemon_df = pd.DataFrame(pokemon["results"])
    pokemon_df.to_csv("pokemon.csv")
    pokemon_df.to_json("pokemon.json")
    pokemon_df.to_excel("pokemon.xlsx")
    print(pokemon_df)


if __name__ == "__main__":
    main()

