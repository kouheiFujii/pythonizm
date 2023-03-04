# initialize the class
class Person(object):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('hello, my name is {}'.format(self.name))

    def running(self):
        # クラス内でメソッドを呼び出す
        self.run(10)

    def run(self, num):
        print('run' * num)


person = Person('Mike')
person.say_hello() # hello, my name is Mike
person.running() # runrunrunrunrunrunrunrunrunrun
