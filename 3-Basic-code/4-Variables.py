"""
Declaration
I tell python I will use that space in memory to save data
The declaration happend only 1 time

Definition
A variable can be redefined
"""
a = 15
b = 3
c = a*b
print(c)

sum = 3
sum += 5
print(sum)

#Python is Case sensitive, so Name and name are different variables

"""
Concat
"""
name = "Tom"

greet = "My name is " + name +  " so far"
print(greet)

greet2 = f"My name with F strings is {name} so far"
print(greet2)

greet3 = f"My number with F strings is {sum} so far"
print(greet3)

greet4 = f"My boolean with f strings is {True}"

"""
Delete variables
"""
DelName = "Jhon"
del DelName
#print(DelName) # Here we have an error because the variable does not exists


DelName2 = "Jhon2"
DelGreet =  f"Hello {DelName2}, nice to meet you!"
del DelName2
print(DelGreet)


"""
Variables naming conventions
camelCase: thisIsMyVariable
snake_case: this_is_my_variable (python recomendation)
"""