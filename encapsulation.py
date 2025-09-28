class myclass:
    x = 10
    __y = 25
    def display(self):
        return self.__y

myobject = myclass()
print(myobject.x)
# print(myobject.__y)  privet variable ekk kelinma assess krnna ba function ekk hadala puluwan 

print(myobject.display()) #function ekk hadala puluwan access krnna 


class myclass1:
    def meth1(self):
        print("Hello chandima")
        self.__meth2()

    def __meth2(self):
        print("Welcome")

myobject1 = myclass1()
myobject1.meth1()
#myobject1.__meth2() privet method ekk me widiyata access krnna ba 
