# ジェネレータ内包表記
def gen():
    for i in range(10):
        yield i
g = gen()
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2

# ワンライナーで書く
g = (i for i in range(10))
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
