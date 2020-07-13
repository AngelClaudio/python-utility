# Function definition starts with "def"
def greet_user():
    """Display a simple greeting."""
    print("Wassup home slice!")

# Asterisk on a parameter tells Python make an empty tuple
# and pack whatever values it receives into it.
# *Note parameters taking arbitrary arguments need to be placed last
# in the argument list.
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Use double asterisk to to create an empty dictionary that will
# accept an arbitrary number of keyword arguments
def build_profile(first, last, **user_info):
       """Build a dictionary containing everything we know about a user."""
       user_info['first_name'] = first
       user_info['last_name'] = last
       return user_info

user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)

