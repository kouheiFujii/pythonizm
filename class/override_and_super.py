class Car(object):
    def __init__(self, model=None):
        self.model = model # インスタンス変数

    def run(self):
        print('run')

class ToyotaCar(Car):
    # override
    def run(self):
        print('fast')

class TeslaCar(Car):
    # 初期化
    def __init__(self, model='Model S', enable_auto_run=False):
        # super()で親クラスのメソッドを呼び出す
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    # override
    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')

car = Car('Prius')
car.run() # run
print(car.model) # Prius
print('---')
toyota_car = ToyotaCar('Lexus')
toyota_car.run() # fast
print(toyota_car.model) # Lexus
print('---')
testla_car = TeslaCar()
testla_car.run() # super fast
testla_car.auto_run() # auto run
print(testla_car.model) # Model S
print(testla_car.enable_auto_run) # False
