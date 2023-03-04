# dictionary type method
a = {'x': 1, 'y': 2, 'z': 3}

# return keys
print(a.keys()) # dict_keys(['x', 'y', 'z'])

# return values
print(a.values()) # dict_values([1, 2, 3])

# return items
print(a.items()) # dict_items([('x', 1), ('y', 2), ('z', 3)])

# return key-value pair
print(a.get('x')) # 1

# remove key-value pair
print(a.pop('x')) # 1
print(a) # {'y': 2, 'z': 3}

# add key-value pair
a.update({'w': 0})
print(a) # {'y': 2, 'z': 3, 'w': 0}
