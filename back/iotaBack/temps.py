import json 



user_template = '''{
    "USER": {
        "ID": "",
        "SEC_LVL": [],
        "CURRENT SEED": [],
        "CURRENT ADDRESS": [],
        "CURRENT ADD INDEX": [],
        "ADDRESS LIST": [],
        "PAST SEEDS": [],
        "PAST ADDRESSES": [],
        "PENDING TRANSACTIONS": [],
        "CONFIRMED TRANSACTIONS": [],
        "CREATE DATE": [],
    }
}''' 

basic = json.loads(user_template)