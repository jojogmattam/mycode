#!/usr/bin/python3
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

# check on the names of data passed
def name_finder(got_list):
    names = []  # list to return back of decoded names
    for x in got_list:
        # send HTTP GET to one of the entries within the list
        r = requests.get(x)
        decodedjson = r.json() # decode the JSON on the response
        names.append(decodedjson.get("name"))  # this returns the housename and adds it to our list
    return names  # when operation is over, send it back


def main():
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        print(f"\nThe names of the books the character appears in\n")
        for x in name_finder(got_dj.get("books")):
            print(x)

        print(f"\nThe names of the allegiances the character has (if any)\n")
        for x in name_finder(got_dj.get("allegiances")):
            print(x)

        print(f"\nThe names of the character, and if the character doesn't have a name, their first alias")
        print(got_dj.get("name"))
        if got_dj.get("name") == '':
             print("The character doesn't have a name")
             print("The first alias is:")
             print(got_dj.get("aliases")[0])
             print()
            
if __name__ == "__main__":
    main()

