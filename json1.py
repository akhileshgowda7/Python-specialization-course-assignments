import json

data = '''
{
  "name" : "Akhilesh",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4786"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
