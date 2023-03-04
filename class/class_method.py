class Person(object):
    kind = 'human' # クラス変数
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    def dont_call_me(self):
        print('don\'t call me')

# クラスから直接メソッドは呼び出せない
# print(Person.dont_call_me()) # TypeError: dont_call_me() missing 1 required positional argument: 'self'

# インスタンスにすることで呼び出せる
person = Person()
print(person.dont_call_me()) # don't call me

# クラスから直接メソッドを呼び出す
print(Person.what_is_your_kind()) # human
print('---')
