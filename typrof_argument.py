def student_info(name, age):
    print(f'My name is {name}. My age is {age}.')

# positional rguments
student_info("kamal", 55)

print("--------------------")

#keyword arguments
student_info(age=20, name="Chandima")

print("--------------------")

def total_marks(*marks):
    total = 0
    for mark in marks:
        total = total + mark
    print(total)

total_marks(25,2,90,60)