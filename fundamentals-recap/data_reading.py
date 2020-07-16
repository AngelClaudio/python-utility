# Reading physical file

with open(file='fundamentals-recap/pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''

# Concatenate 3 lines and remove spaces
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))