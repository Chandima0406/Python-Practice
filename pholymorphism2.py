class calc:
    def add(self, a= None, b= None, c = None):
        sum = 0
        if a!= None and b!= None and c!=None:
            sum = a+b+c
            print(sum)

        elif a!=None and b!=None:
            sum = a+b
            print(sum)

        else:
            sum = a
            print(sum)

        

myobj = calc()
myobj.add(50, 25, 800)