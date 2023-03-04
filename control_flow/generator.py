# generator function
def gen_func():
    yield 1
    name = "bobby"
    yield name
    yield 3
    return "imooc"

g = gen_func()
print(next(g)) # 1
print(next(g)) # bobby
print(next(g)) # 3
print(next(g)) # StopIteration: imooc
