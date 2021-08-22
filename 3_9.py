# mro - Method Resolution Order DFS

class A:
    num = 10


class B(A):
    num = 3


class C(A):
    num = 2


class D(B, C):
    pass


print(D.num)
print(D.mro())
print(A.mro())

D.__str__
