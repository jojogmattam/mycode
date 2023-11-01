#!/usr/bin/env python3
depp = {
    "full_name": "John Christopher Depp II",
    "birth_date": "June 9, 1963",
    "occupation": ["Actor", "Musician", "Producer"],
    "spouses": [
        {
            "name": "Lori Allison",
            "married": 1983,
            "divorced": 1985
        },
        {
            "name": "Amber Heard",
            "married": 2015,
            "divorced": 2017
        }
    ],
    "children": {
        "count": 2,
        "names": ["Lily", "Rose"]
    }
}

def display_menu(keys):
    print("Menu:")
    for i, key in enumerate(keys, start=1):
        print(f"{i}. {key}")
    print(f"{len(keys) + 1}. Add or Delete Data")
    print(f"{len(keys) + 2}. Quit")

def get_value(key):
    return depp.get(key, "Data not found")

def add_data(key, value):
    depp[key] = value
    print(f"{key} added to the dictionary.")

def delete_data(key):
    if key in depp:
        del depp[key]
        print(f"{key} deleted from the dictionary.")
    else:
        print(f"{key} not found in the dictionary.")

keys = list(depp.keys())

while True:
    display_menu(keys)
    choice = input("Choose the option: ")

    if choice.isnumeric():
        choice = int(choice)
        if 1 <= choice <= len(keys):
            key = keys[choice - 1]
            print("\n\nOutput\n")
            print(get_value(key))
            print("\n\n")
        elif choice == len(keys) + 1:
            add_del_option = input("Add (A) or Delete (D) data: ")
            if add_del_option == "A":
                key = input("Enter the key you want to add: ")
                value = input("Enter the value: ")
                add_data(key, value)
                keys.append(key)
            elif add_del_option == "D":
                choice = int(input("Enter the key you want to delete: "))
                key = keys[choice - 1]
                delete_data(key)
                if key in keys:
                    keys.remove(key)
        elif choice == len(keys) + 2:
            print("Bye for now, See you soon!")
            break
        else:
            print("Invalid option. Please try again")
    else:
        print("Invalid option. Please try again.")

