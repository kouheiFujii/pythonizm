# dictionary type basic usage
a = {'x': 1, 'y': 2, 'z': 3}
print(a['x']) # 1
print(a['y']) # 2

# append to dictionary
a['w'] = 0
print(a) # {'x': 1, 'y': 2, 'z': 3, 'w': 0}

# create dictionary `dict`
b = dict(one=1, two=2, three=3)
print(b) # {'one': 1, 'two': 2, 'three': 3}

# create dictionary `dict` from sequence
c = dict([('one', 1), ('two', 2), ('three', 3)])
print(c) # {'one': 1, 'two': 2, 'three': 3}

# delete item from dictionary
c.pop('one')
print(c) # {'two': 2, 'three': 3}

# dictionary unpacking
e, f, g = {'x': 1, 'y': 2, 'z': 3}
print(e) # x
print(f) # y
print(g) # z

# for loop
for key in a:
    print(key, a[key])
