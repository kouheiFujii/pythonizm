# 複数のクラスを多重継承できる
class A(object):
    def method(self):
        print("A")

class B(object):
    def method(self):
        print("B")

    def b_method(self):
        print("b")

class C(A, B):
    pass

c = C()
c.method() # A
c.b_method() # b
# 継承しているクラスに同じメソッドがある場合、左側のクラスのメソッドが優先される
# class C(A, B) ならば A のメソッドが優先される
c.method() # A
