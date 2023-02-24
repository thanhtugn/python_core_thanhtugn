import json

#EX 1: 
def convert_dict_to_json():
    data = {
        'key1' :  'value 1',
        'key2' :  'value 2',
        'key3' :  'value 3',
        }
    json_data = json.dumps(data)
    print(json_data)
convert_dict_to_json()

#EX 2:
def access_to_value():
    json_str = """{"key1" :  "value 1", "key2":  "value 2", "key3" :  "value 3"}"""
    json_data = json.loads(json_str)
    print(f'Value wth key key 2 is: {json_data["key2"]}')
access_to_value()

#EX 3:
def pertty_json_data():
    json_data = {"key1" :  "value 1", "key2":  "value 2", "key3" :  "value 3"}
    pertty_json = json.dumps(json_data, indent=2, separators=(",","="))
    print(pertty_json)
pertty_json_data()

#EX 4:
def write_json():
    json_data = {"id": 10, "name": "PhamVanManh", "age": 31, "address": "HaNoi"}
    with open('sample_json.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2, sort_keys=True)
write_json()

#EX 5:
def json_nested_access():
    json_str = """{
        "company": {
            "employee1":{
                "name": "Pham Van Nam",
                "payble": {
                    "salary": "1200$",
                    "bonus": "300$"
                },
                "position": "Leader"
            },
            "employee2":{
                "name": "Pham Van Tan",
                "payble": {
                    "salary": "2200$",
                    "bonus": "600$"
                },
                "position": "Manager"
            }
        }
    }"""
    json_data = json.loads(json_str)
    salary_emp1 = json_data['company']['employee1']['payble']['salary']
    print(f'salary of employee 1 is: {salary_emp1}')
    with open('company.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2, sort_keys=True)
json_nested_access()

def read_json_file():
    with open('company.json', 'r') as json_file:
        json_data = json.load(json_file)