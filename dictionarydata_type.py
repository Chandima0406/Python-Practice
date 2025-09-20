my_dict = {"name":"kamal", "age":20, "city":"kandy"}
students = {80:"kamal", 81:"saman", 82:"nimal", 83:"sunil"}

print(my_dict)
print(type(my_dict))

print(my_dict['age'])
print(my_dict['name'])

my_dict['name'] = 'chandima'
my_dict['is_married'] = False
my_dict.update({'adress':'talawa', 'gender':'male'})
print(my_dict)

del my_dict['age']
print(my_dict)

my_dict.pop('name')
print(my_dict)

my_dict.clear()
print(my_dict)