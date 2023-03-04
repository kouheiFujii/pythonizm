# クラス変数はインスタンス内で共有される
class Person(object):
    kind = 'human' # クラス変数

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

person1 = Person('Mike')
person1.who_are_you() # Mike human
person2 = Person('Nancy')
person2.who_are_you() # Nancy human

class T(object):
    words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
print(c.words) # ['add 1']
d = T()
d.add_word('add 2') # 共通のwordsを参照している
print(c.words) # ['add 1', 'add 2']
print('---')
print(d.words) # ['add 1', 'add 2']
