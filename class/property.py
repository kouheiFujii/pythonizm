# プロパティを使用した変数のアクセス制御
# 実際にはゴニョゴニョすればアクセスできるので、使わないでほしいということを伝えるために使う

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('getter')
        return self._name

    @name.setter
    def name(self, value):
        print('setter')
        print('{}'.format(value))
        self._name = value

    @name.deleter
    def name(self):
        print('deleter')
        del self._name

person = Person('Mike')
person.name # getter
person.name = 'Nancy' # setter

print('---')
# アクセス可能
print(person._name) # Nancy

del person.name # deleter

print('---')

# アンダースコア2つでアクセス不可
class Car:
    def __init__(self, model=None):
        self.__model = model

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @model.deleter
    def model(self):
        del self._model

    # クラス内であればアクセス可能
    def run(self):
        print('{} run'.format(self.__model))

car = Car('Lexus')
# print(car.model) # AttributeError: 'Car' object has no attribute '_model'. Did you mean: 'model'?
car.run() # Lexus run
