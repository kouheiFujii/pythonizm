# set type basic usage
a = {1, 2, 3}
print(a) # {1, 2, 3}
b = {3, 4, 5}
print(b) # {3, 4, 5}

# disjunction
print(a | b) # {1, 2, 3, 4, 5}

# intersection
print(a & b) # {3}

# difference
print(a - b) # {1, 2}
print(b - a) # {4, 5}

# symmetric difference
print(a ^ b) # {1, 2, 4, 5}

# set is unique
b = {3, 3, 3, 4, 5}
print(b) # {3, 4, 5}

# set is mutable
b.add(6)
print(b) # {3, 4, 5, 6}v
