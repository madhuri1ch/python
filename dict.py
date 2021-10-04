d={'name':'madhuri','age':25,'phone':123}

print(d['name']) #madhuri
#print(d['address']) #error: KeyError: 'address'
print(d.get('address'))# none
print(d.get('address','not found')) # if key is not found then it returns not found
d['address']='himaja'
print(d.get('address'))# himaja


d.update({'name':'madhuri_updated','age':30}) #{'name': 'madhuri_updated', 'age': 30, 'phone': 123, 'address': 'himaja'}
print(d)

del d['address']
print(d) #{'name': 'madhuri_updated', 'age': 30, 'phone': 123}

age=d.pop('age')
print(age)#30

print(len(d)) #2
print(d.keys())#dict_keys(['name', 'phone'])

print(d.values()) #dict_values(['madhuri_updated', 123])

print(d.items())# dict_items([('name', 'madhuri_updated'), ('phone', 123)])

for key in d:
    print(key)

for key,value in d.items():
    print(key,value)