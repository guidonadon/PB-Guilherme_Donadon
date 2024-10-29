import json

with open("person.json") as person_json:
    arquivo = json.load(person_json)
    
print(arquivo)
