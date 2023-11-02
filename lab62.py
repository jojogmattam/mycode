#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

print()
print("Write a for loop that returns all the animals from the NE Farm!")
print()

for farm in farms:
    if farm["name"] == "NE Farm":
        for animal in farm["agriculture"]:
            print(animal)
        break

print()
print("Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.")
print()

input_farm = input("Choose a farm (NE Farm, W Farm, or SE Farm): ").lower()

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

input_farm = input("Choose a farm (NE Farm, W Farm, or SE Farm): ").lower()
plants = ["carrots", "celery"]

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
