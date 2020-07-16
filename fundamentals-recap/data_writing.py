filename = 'programming.txt'

# Must use argument 'w' for mode to write (read only is default)
with open(filename, mode='w') as file_object:
    file_object.write("I love programming.")

