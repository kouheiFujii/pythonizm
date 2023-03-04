# 静的メソッド
# インスタンス化をせずにメソッドを呼び出せる
class Calculator(object):
    @staticmethod
    def add(a, b):
        print(a + b)

print(Calculator.add(10, 100)) # 110
