from iota.crypto.types import Seed
from iota.crypto.addresses import AddressGenerator
from pprint import pprint
import json

# TODO: create seed, check for previous usage, and store as current seed.
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgusian",
        "companions": ["Arthur Dent", "Marvin", "Trillian", "Ford Prefect"]
    }
}

seedLog = open("acc_log.json", "w")
json.dump(data, seedLog, indent=4)


class SeedGenCheck():

    newSeed = Seed.random()
    
#    def seedCheck():

        
    

# TODO: create address with new seed, check to see if previously used, stor as current address.

