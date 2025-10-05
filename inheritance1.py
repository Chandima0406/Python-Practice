class parent:
    def func1(self):
        print("Hello")

class child(parent):
    def func2(self):
        #super().func1()
        print("Welcome")

    def func1(self):
        print("Hi")

myobject = child()
myobject.func2()


print("--------------------------")

myobject.func1()


print("--------------------------")

class Fruit:
    number_of_items = None
    unit_price = None
    def set_value(self,x,y):
        self.number_of_items = x
        self.unit_price = y

class Apple(Fruit):
    def price(self):
        print('For Apple ', self.number_of_items*self.unit_price)

class Orange(Fruit):
    def price(self):
        print('For Orange ', self.number_of_items*self.unit_price)

class Grapes(Fruit):
    def price(self):
        print('For Grapes ', self.number_of_items*self.unit_price)


object1 = Apple()
object2 = Orange()
object3 = Grapes()

object1.set_value(50, 10)
object2.set_value(6, 52)
object3.set_value(20, 23)

object1.price()
object2.price()
object3.price()
