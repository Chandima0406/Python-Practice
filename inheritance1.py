class parent:
    def func1(self):
        print("Hello")

class child(parent):
    def func2(self):
        super().func1()
        print("Welcome")

myobject = child()
myobject.func2()
