import json
py_string='''
{
    "people":[
       {
        "name":"madhuri",
        "phone":9740281762,
        "emails":["madhuri@gmail.com","chilaka@ge.com"],
        "has_license":false
       } ,
       {
        "name":"chilaka",
        "phone":9740281762,
        "emails":["madhi@gmail.com","ma@ge.com"],
        "has_license":true
       }
    ]
}
'''

data=json.loads(py_string) #loads string to json object
print(data)
#json object is converted into dict
#array to list
for person in data['people']:
    del person['phone']

json_new=json.dumps(data,sort_keys=True,indent=2)
print(json_new)

with open('json_new.py','w') as f:
  json.dump(data,f,indent=2)