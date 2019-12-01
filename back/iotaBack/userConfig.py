from iota.crypto.types import Seed
from iota.crypto.addresses import AddressGenerator
from pprint import pprint
from datetime import datetime
from temps import basic
import json


class User:
    '''Creates a user object and passes the data to a json file (userLog.json)'''
    
    def createNewUser(self):
        with open('userLog.json', 'w') as write_file:
            json.dump(basic, write_file, indent=4)

        with open('userLog.json', 'r') as read:
            update = json.load(read)
            update['USER']['ID'] = ['PLACEHOLDER']
            update['USER']['CURRENT SEED'] = [str(Seed.random())]
            update['USER']['SEC_LVL'] = 3

        with open('userLog.json', 'w') as write:
            json.dump(update, write, indent=4)

    @classmethod
    def userManualSeed(cls):
        seed = input('Please enter your seed:')




ZAPHOD = User()


if __name__ == "__main__":
    ZAPHOD.createNewUser()

