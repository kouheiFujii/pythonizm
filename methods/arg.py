# Positional Arguments
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


r = menu('chardonnay', 'chicken', 'cake')
print(r) # {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}

# error
# r = menu('chardonnay', 'chicken') # TypeError: menu() missing 1 required positional argument: 'dessert'

# Keyword Arguments
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

r = menu(entree='beef', dessert='bagel', wine='bordeaux')
print(r) # {'wine': 'bordeaux', 'entree': 'beef', 'dessert': 'bagel'}

r = menu('frontenac', entree='fish', dessert='flan')
print(r) # {'wine': 'frontenac', 'entree': 'fish', 'dessert': 'flan'}

# Default Argument Values
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

r = menu('chardonnay', 'chicken')
print(r) # {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}

# Tuple Unpacking
def print_args(*args):
    print('Positional argument tuple:', args)

print_args() # Positional argument tuple: ()
print_args('a', 'b') # Positional argument tuple: ('a', 'b')
d = (1, 2, 3)
print_args(d) # Positional argument tuple: ((1, 2, 3),)
print_args(*d) # Positional argument tuple: (1, 2, 3)

# Dictionary Unpacking
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs() # Keyword arguments: {}
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon') # Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
k = {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
print_kwargs(**k) # Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
