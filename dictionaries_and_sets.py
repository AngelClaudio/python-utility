# Dictionaries made using curly braces.
new_dict = {3 : 2, 'name' : 'Angel Claudio'}

print(new_dict)
print (new_dict['name'])

# Add new value using brackets.
new_dict['GOAT'] = 'Michael Jordan'
print(new_dict)



# Use "del" key work to move a pair from a dictionary
del new_dict[3]
print(new_dict)

# get function is good for not producing an error
# if a value doesn't exist, will return "None"
# Note None is a special value indicating absence of a value.
print(new_dict.get(3))

# Using get you can put an alternative value when none is available.
print(new_dict.get(3, 'nothing here buddy!\n'))

# You can for loop and unpack multiple items in a dictionary.
for x, y in new_dict.items():
    print(f"Key is {x} \nValue is {y} \n")

# Looping through keys is default behavior
for cash in new_dict:
    print(cash)

new_dict['homie'] = 'Angel Claudio'

# Set will only bring back unique values
for unique_values in set(new_dict.values()):
    print(unique_values)

print('\n')

for unique_values in set(new_dict):
    print(unique_values)

print('\n')

# Set are unique unordered values, defined with brackets as well.
my_exclusive_list = {'yes', 1, 2, 'hey'}

print(my_exclusive_list)

people = []

