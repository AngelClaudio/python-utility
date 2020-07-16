for _ in range(5):
    people.append({'name' : 'John', 'gender' : 'male'})

for person in people[:3]:
    if  person['name'] == 'John':
        person['name'] = 'Jane'
        person['gender'] = 'female'

print(people)

# Example of list inside of a dictionary
person = {'name' : 'Angel Claudio', 'likes' : ['comics, pizza']}

print(person)

# Example of dictionary nested in dictionary
users = {
       'aeinstein': {
           'first': 'albert',
           'last': 'einstein',
           'location': 'princeton',
           },
        'mcurie': {
           'first': 'marie',
           'last': 'curie',
            'location': 'paris',
           },
       }

