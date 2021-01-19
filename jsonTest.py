"""
author:Yuegb
date:2021,01,17
"""
import json

# python dict -> json string
person = {'name': 'ketty', 'age': 2, 'color': 'white', 'food': ['meat', 'vegetables']}
print(person)
print(type(person))
jsonStr = json.dumps(person)
print(jsonStr)
print(type(jsonStr))
jsonStr = json.dumps(person, indent=4, sort_keys=True)
print(jsonStr)

json.dump(person, open('data.json', 'w'), indent=4)

# json string -> python
strDict = '{"age": 1}'  # 格式需要外单内双
pythonOjb = json.loads(strDict)
print(pythonOjb)
print(type(pythonOjb))
strList = '["a", {"name": "ketty"}]'
pythonOjb = json.loads(strList)
print(pythonOjb)
print(type(pythonOjb))

pythonOjb = json.load(open('data.json', 'r'))
print(pythonOjb)
print(type(pythonOjb))
