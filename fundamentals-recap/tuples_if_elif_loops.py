# Tuples may be created using parentheses, they are immutable
my_facts = ("brooklyn", 1) 
print(my_facts)

# Tuples are technically defined by a comma (need at least one).
# Parentheses just makes them look neater.
still_a_tuple = 5,  

print(still_a_tuple)

still_a_tuple = 'yo momma', 'son'
print(still_a_tuple)

# parentheses not needed
if 'yo' in still_a_tuple :
    print('yes')
else:
    print('nope')

if 'yo momma' not in still_a_tuple:
    print('yes')
elif 'dad' in still_a_tuple:
    print('yes')
else:
    print('the end')