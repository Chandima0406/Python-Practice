name = "Chandima Wijerathna"

print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())


#find index
print(name.find('d'))
print(name.find('a', 3, 13))
print(name.rfind('a', 3, 13))

print(name.index('m'))


#center ljust rjust
print(name.center(30))
print(name.ljust(30))
print(name.rjust(30))

print(name.center(30, "-"))
print(name.ljust(30, "-"))
print(name.rjust(30, "-"))


name1 = "   rathnayake mudiyanselage   "
print(name1)
print(name1.strip()) #spacing nathuwa output eka ganna puluwan
print(name1.lstrip())
print(name1.rstrip())

