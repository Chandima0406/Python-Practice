name, age, score = "Kamal", 22, 43.5656

# He is kamal. He is 22 years old, and his score is 5656
print("He is "+name+", He is "+str(age)+" years old, and his score is "+str(score))

print("He is %s. He is %d years old, and his score is %.2f"  %(name, age, score))

print("He is {}. He is {} years old, and his score is {}".format(name, age, score))

print("He is {2}. He is {1} years old, and his score is {0}".format(score, age, name))

print(f"He is {name}. He is {age} years old, and his score is {score}")