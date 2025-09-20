my_list = ["kamal",20,"kandy",False]
my_tuple = ("kamal",20,"kandy",False)

my_set = {"kamal",20,"kandy",False}

print(my_set)
my_set.add(455)
my_set.remove("kamal")
my_set.update(("saman","sunil"))
my_set.discard(10) #methanadi thiyanawa nm ain wenawa nathi nm ain wenne na error ekk enneth na element eka nathi unata 
my_set.pop()
print(my_set)

my_set.clear()

print(my_set)
print(type(my_set))


A = {1,2,3,4,5}
B = {4,5,6,7,8,9}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))