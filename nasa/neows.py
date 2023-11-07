import requests
import os
from dotenv import load_dotenv

env_loc = '/home/student/.env'
load_dotenv(env_loc)

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this is our main function
def main():
    api_key = os.getenv("api_key")

    # make a request with the request library
    neowrequest = requests.get(NEOURL + "api_key=" + api_key)
    
    # strip off json attachment from our response
    neodata = neowrequest.json()

    largest_diameter = None
    fastest_speed = None
    closest_distance = None

    for date in neodata["near_earth_objects"]:
        for asteroid in neodata["near_earth_objects"][date]:
            # largest diameter
            if largest_diameter is None or asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"] > largest_diameter:
                largest_diameter = asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"]

            # fastest asteroid
            if fastest_speed is None or asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"] > fastest_speed:
                fastest_speed = asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]

            # closest asteroid to Earth
            if closest_distance is None or asteroid["close_approach_data"][0]["miss_distance"]["kilometers"] < closest_distance:
                closest_distance = asteroid["close_approach_data"][0]["miss_distance"]["kilometers"]

    ## display data
    print("Largest in km:", largest_diameter)
    print("Fastest in km/s:", fastest_speed)
    print("Closest in km:", closest_distance)

if __name__ == "__main__":
    main()

