import json 



basic_template = '''{
    "USER": {
        "ID": [],
        "SEC_LVL": 0,
        "CURRENT SEED": [],
        "CURRENT ADDRESS":[],
        "PAST SEEDS": [],
        "PAST ADDRESSES": []
    }
}'''

basic = json.loads(basic_template)