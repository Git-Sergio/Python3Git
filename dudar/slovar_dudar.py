d = {'test' : 1, 'test_2' : "TEst"}
print (d['test'])


d = dict (short='dict', longer='dictionary')
d['short'] = 234
print (d)


d = dict ([(23, 34), (56, 87)])
print(d)


d = dict.fromkeys (['a', 'b',], 1)
print('dict.fromkeys', d)

d = {a : a ** 2 for a in range(7)}
print(d)
print('range:', d)

person = {'name' : {'last_name' : 'Petrov', 'first_name' : 'Ivan', 'middle_name': 'Ivanych'}, 'adress': ['s.Wroclaw' , 'ul.Zabubnom', 'd. 57', 'kv.15'], 'phone' : {'home_phone' : '55-42-42', 'mobile_phone' : '8-888-8888-8888'}} 
print(person)
print(person['name'])
print(person['name']['first_name'])
print(person['adress'][1])
print(person['phone']['mobile_phone'])


# person.fromkeys([seq], value)
# person.items()
# person.keys()
# person.popitem()
# # KeyError
# person.setdefault(key, default)
# person.update([other])
# person.values()
# person.clear()
# person.copy()
