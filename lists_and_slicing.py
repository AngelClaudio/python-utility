# slicing in python means working with a specific group
# of items in a list

players = ['charles', 'martina', 'michael jordan', 'florence', 'eli']
print(players[0:3]) 
# Starts at 0 but ends at 3 (does nothing with 3, 
# if was 5 no error, just knows to stop before 5)

# Prints player before last
print(players[-2]) 

# Prints players before last until end
print(players[-2:]) 

# Colon alone will go to max
print(players[2:]) 

for p in players[2:]:
    # title function will Title Case
    print(p.title()) 

players_still_reference_other_one = players
players_still_reference_other_one.append('George Foreman')
print(players) 
# notice the new variable is referencing the same values as 
# the original variable

really_new_players = players[:]
really_new_players.append("Bruce Wayne")
print(players) 
# not updated since reference doesn't exist