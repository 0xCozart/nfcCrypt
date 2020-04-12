from iota.crypto.types import Seed
from iota.crypto.addresses import AddressGenerator
from temps import basic

import json


class User:
    '''
    Creates a user object and passes the data to a json file (user_logjson)
    '''

    def create_new_user(self):
        '''
        Creates a new user profile
        :param user_ID: <str> Username provided from Snapchat API.
        :return user_log.json: <json_file> Creates standard user template.  
        '''

        new_seed = str(Seed.random())
        address_generator = AddressGenerator(seed=new_seed, checksum=True, security_level=2)
        address_list = address_generator.get_addresses(0,10)
        serialized_address_list = [str(x) for x in address_list]
        
        with open('user_log.json', 'w') as write_file:
            json.dump(basic, write_file, indent=4)

        with open('user_log.json', 'r') as read_file:
            update = json.load(read_file)
            update['USER']['ID'] = ['PLACEHOLDER']
            update['USER']['SEC_LVL'] = 2
            update['USER']['CURRENT SEED'] = [new_seed]
            update['USER']['CURRENT ADDRESS'] = serialized_address_list[0]
            update['USER']['ADDRESS LIST'] = serialized_address_list


        with open('user_log.json', 'w') as write_file:
            json.dump(update, write_file, indent=4)

        
    @classmethod
    def userManualSeed(cls, seed):
        '''
        '''
        pass

    


ZAPHOD = User()


if __name__ == "__main__":
    ZAPHOD.create_new_user()

