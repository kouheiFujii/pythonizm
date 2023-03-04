# tuple type basic usage
a = (1, 2, 3)
print(a)

# does not support item assignment
# a[0] = 100 # TypeError: 'tuple' object does not support item assignment

# tuple unpacking
b = (4, 5, 6)
c, d, e = b
print(c) # 4
print(d) # 5
print(e) # 6

# nested tuple unpacking
f = ((7, 8), 9)
g, h = f
print(g) # (7, 8)
print(h) # 9
