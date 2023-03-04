# ダックタイピングの例
class Person(object):
    def __init__(self, age=1):
        self.age = age

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
          raise ValueError('Age must be greater than 1')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError('Age must be less than 18')

# PersonとCarの関係を表現するクラス
class PersonCar(object):
    def drive(self, person):
        # 18歳以上の場合はドライブできる
        # 18歳未満の場合はドライブできない(raiseする)
        if person.age >= 18:
            return 'ok'
        else:
          raise ValueError('No drive')

baby = Baby()
adult = Adult()
person_car = PersonCar()
print(person_car.drive(adult)) # ok
# print(person_car.drive(baby)) # ValueError: No drive
