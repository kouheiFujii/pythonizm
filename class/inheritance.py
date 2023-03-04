class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run() # run
print('---')
toyota_car = ToyotaCar()
toyota_car.run() # run
print('---')
testla_car = TeslaCar()
testla_car.run() # run
testla_car.auto_run() # auto run
