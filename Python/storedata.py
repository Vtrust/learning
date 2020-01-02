import json
data = {
    "name":"hello",
    "age":17
}
with open("./a.json",'w',encoding='utf-8') as json_file:
    json.dump(data,json_file,ensure_ascii=False)