# closure basic usage
def outer_func(message):
    def inner_func(name):
        print(message + ' ' + name)

    return inner_func

out = outer_func('Hi')
out('John') # Hi John
