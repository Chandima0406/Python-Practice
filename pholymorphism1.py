class parent:
    def func(self):
        print("Hello")

class child(parent):
    def func(self):
        print("Welcome")

myobj = child()

print(myobj.func())