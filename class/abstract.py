import abc
# 抽象クラスを作成する
# Pythonにはもともとなかった機能
# コードスタイル的には使わない方がいいとされているっぽい

class Person(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say_hello(self):
        pass

    @abc.abstractmethod
    def say_goodbye(self):
        pass

class Student(Person):
    def say_hello(self):
        print('hello')

    def say_goodbye(self):
        print('goodbye')

# 継承したクラスで抽象メソッドを実装していない
class Teacher(Person):
    def say_hello(self):
        print('hello')

student = Student()
student.say_hello() # hello
student.say_goodbye() # goodbye
# 抽象クラスを全て実装していないのでインスタンス化できない
teacher = Teacher() # TypeError: Can't instantiate abstract class Teacher with abstract methods say_goodbye
