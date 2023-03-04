l = [1, 20, 3, 49, 58, 22, 10]

print("list basic =================")
print("l: ",l)
print("l[0]: ",l[0])
print("l[2]: ",l[2])
print("l[-1]: ",l[-1])
print("l[-2]: ",l[-2])
print("end =================")

print("")

print("list select =================")
print("l[0:2]: ",l[0:2])
print("l[2:4]: ",l[2:4])
print("l[:3]: ",l[:3])
print("l[1:]: ",l[1:])
print("l[:]: ",l[:])
print("end =================")

print("")

print("list string =================")
s = list("abcdefg")
print("s = list('abcdefg')")
print("s: ", s)
print("end =================")

print("")


print("nest =======================")
a = [1, 2, 3, 4, 5]
n = list('hijklmn')
print("a: ", a)
print("n: ", n)
x = [a, n]
print("x = [a, n]: ", x)
print("x[0]: ", x[0])
print("x[1]: ", x[1])
print("x[0][2]: ", x[0][2])
print("end =================")
