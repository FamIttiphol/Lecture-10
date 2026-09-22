import json
date = {"name": "NongFamINE", "Age": "18"}
json_str = json.dumps(date)
print(json_str)

parsed_date = json.loads(json_str)
print(parsed_date)
print(parsed_date["name"])
print(parsed_date["Age"])
