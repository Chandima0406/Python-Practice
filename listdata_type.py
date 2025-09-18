list1 = [20, 30, 40, 50, 60]
list2 = list((12, 43, 4, 78, 32))
my_list = ['kamal', 20, 'kandy', False, 20, [1,2,3]]
my_list[2] = 'colombo'

print(list1)
print(list2)
print(my_list)
print(my_list[0])
print(my_list[2:])
print(my_list[::2])
print(my_list[5][0])
print(my_list)
print(type(list1))
print(type(list1))


my_list.append("saman")
print(my_list)

my_list.insert(5, 'hello')
print(my_list)

my_list.pop(0)
print(my_list)

my_list.remove("saman")
print(my_list)

print(my_list.count(20))