class phone1:
    def feature1(self):
        print("camera")

class phone3(phone1):
    def feature3(self):
        print("Blutooth")

class phone2(phone3):
    def feature2(self):
        print("internet")

myobject = phone2()
myobject.feature2()
myobject.feature1()
myobject.feature3()