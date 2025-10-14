def new(func):
    def inside(a, b):
        if b==0:
            a,b = b,a
        return func(a, b)
    return inside

def divide(a, b):
    return a/b


divide = new(divide)
print(divide(4,3))