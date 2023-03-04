# Class basic difinition
class Person(object): # (object) はPython3から省略可能。コードスタイル的に書いたほうがいいとされている。
    def say_hello(self): # selfはインスタンス自身を指す
        print('hello')

person = Person()
person.say_hello() # hello
