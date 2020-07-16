
message = input('Tell me something, and I will repeat it back to you: ')

print(message)
age = ""


while not isinstance(age,int):
    try:
        age = int(input('How old are you?'))
    except ValueError:
        print('Age is a number, try again?')

print(f"System as successfully set your age to {age}")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
           continue     #Only print if not even

    print(current_number)
