class A:
    def __init__(self):
        print('new object is created')
    def info(self):
        print('no instance variable to print')
class D(A):
    def info(self):
        print('hi from inherited object...')
Aobject=A()
print(Aobject.info())
Dobject=D()
print(Dobject.info())