# slicing in python means working with a specific group
# of items in a list

players = ['charles', 'martina', 'michael jordan', 'florence', 'eli']
print(players[0:3]) # Starts at 0 but ends at 3 (does nothing with 3, 
                    # if was 5 no error, just knows to stop before 5)

print(players[-2]) # Prints player before last

print(players[-2:]) # Prints players before last until end

print(players[2:]) # Colon alone will go to max

for p in players[2:]:
    print(p.title()) # title function will Title Case