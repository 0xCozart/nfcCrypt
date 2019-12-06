import json 



basic_template = '''{
    "USER": {
        "ID": [],
        "SEC_LVL": [],
        "CURRENT SEED": [],
        "CURRENT ADDRESS":[],
        "ADDRESS LIST": [],
        "PAST SEEDS": [],
        "PAST ADDRESSES": [],
        "PENDING TRANSACTIONS": [],
        "CONFIRMED TRANSACTIONS": []
    }
}''' 

basic = json.loads(basic_template)