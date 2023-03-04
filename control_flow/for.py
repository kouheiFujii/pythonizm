# basic usage of for
print("basic usage of for")
a = [1, 2, 3]
for i in a:
    print(i)
print("")

# break
print("break")
for i in a:
  if i == 2:
    break
  print(i)
print("")

# continue
print("continue")
for i in a:
  if i == 2:
    continue
  print(i)
print("")

# enumerate
print("enumerate")
fluits = ["apple", "banana", "orange"]
for i, fluit in enumerate(fluits):
  print(i, fluit)
print("")

# range
print("range")
for i in range(10):
  print(i)
print("")
