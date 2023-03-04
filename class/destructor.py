# オブジェクトが使用されなくなったときに呼び出されるデストラクタを定義する
class Person(object):
    def __init__(self, name):
        self.name = name

    def __del__(self): # デストラクタ
        print('Good bye')

    def say_hello(self):
        print('hello')

person = Person('Mike') # インスタンス生成
person.say_hello() # hello
# インスタンスが使用されなくなったときにデストラクタが呼び出される
# Good bye
