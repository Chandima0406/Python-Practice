number = [1,2,3,4,5,6,7,8]

def even_num(x):
    return x % 2 == 0

y = list(filter(even_num, number))

print(y)


from functools import reduce
number = [1,2,3,4,5,6,7,8,9]

reduce(lambda x, y:x+y, number)