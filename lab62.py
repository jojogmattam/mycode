#!/usr/bin/env python3

dataset1 = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

dataset2 = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

def main():
    input_dataset = input("Choose a dataset (1 or 2): ")
    if input_dataset == "1":
        farms = dataset1
        print(f"You chose dataset {input_dataset}")
        print()
    elif input_dataset == "2":
        farms = dataset2
        print(f"You chose dataset {input_dataset}")
        print()
    else:
        print("Invalid input")
        exit()
        
    lab_action(farms)



plants = ["carrots", "celery", "bananas", "apples", "oranges"]

def lab_action(farms):
    print()
    print("Write a for loop that returns all the animals from the NE Farm/NorthEast Farm")
    print()

    for farm in farms:
        if farm["name"] == "Northeast Farm":
            for animal in farm["agriculture"]:
                print(animal)
            break
        elif farm["name"] == "NE Farm":
            for animal in farm["agriculture"]:
                print(animal)
            break

    print()
    print("Ask a user to choose a farm. Return the plants/animals that are raised on that farm.")
    print()

    input_farm = input(f"Choose a farm {[farm['name'] for farm in farms]}: ").lower()

    for farm in farms:
        if farm["name"].lower() == input_farm:
            for animal in farm["agriculture"]:
                print(animal)
            break
        else:
            continue

    print()
    print("Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.")
    print()

    input_farm = input(f"Choose a farm {[farm['name'] for farm in farms]}: ").lower()

    for farm in farms:
        if farm["name"].lower() == input_farm:
            for animal in farm["agriculture"]:
                if animal not in plants:
                    print(animal)
            break
        else:
            continue

    print()
    print("Bye")
    print()
    

if __name__ == "__main__":
    main()
