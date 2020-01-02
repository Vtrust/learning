import json
with open('./a.json','r') as f:
    data = json.load(f)
    print(data['name'])