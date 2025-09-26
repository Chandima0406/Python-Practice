class Student:
    name = "Chandima"
    age = "24"

student1 = Student()
print(student1.name)

student2 = Student()
student2.name = "Wijerathna"
print(student2.name)


print("--------------------------------------")

class students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu1 = students("kamal", 50)
stu2 = students("nimal", 65)
print(stu1.name)
print(stu2.name)
        