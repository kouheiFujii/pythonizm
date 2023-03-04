s = list('abcdefg')
print("s: ", s)
s[2] = 'C'
print("s[2] = 'C'")
print("s: ", s)
s[3:6] = ['D', 'E', 'F']
print("s[3:6] = ['D', 'E', 'F']")
print("s: ", s)
s[3:6] = []
print("s[3:6] = []")
print("s: ", s)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print("")
print(a)
print(b)

x = a + b
print("x = a + b")
print("x: ", x)
a += b
print("a += b")
print("a: ", a)

a.append(100)
print("a.append(100)")
print("a: ", a)

a.insert(0, 200) # 場所指定
print("a.insert(0, 200)")
print("a: ", a)

c = a.pop()
print("c = a.pop()")
print("c: ", c)
print("a: ", a)

d = a.pop(0)
print("d = a.pop(0)")
print("d: ", d)
print("a: ", a)

print("")
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print("x: ", x)
print("y: ", y)
x.extend(y)
print("x.extend(y)")
print("x: ", x)
