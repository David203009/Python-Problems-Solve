# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.

def drink(n):
    if n < 14:
        return 'drink toddy'
    elif n < 18:
        return 'drink coke'
    elif n < 21:
        return 'drink beer'
    else:
        return 'drink whisky'

print(drink(21))