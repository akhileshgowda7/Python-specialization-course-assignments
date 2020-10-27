import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Akhilesh"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Rama"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
