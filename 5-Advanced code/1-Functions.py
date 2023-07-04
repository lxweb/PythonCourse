# Creating our first function
def greet():
    print("Hello!")

greet()

# functions with parameters
def greet_with_params(name):
    print(f'Hello {name}!')

greet_with_params('Jack')

# Function with internal logic
def greet_with_logic(name, gender):
    if gender == 'man':
        print(f'Hello {name}, nice to meet you boy!')
    if gender == 'woman':
        print(f'Hello {name}, nice to meet you girl!')

greet_with_logic('Tomy', 'man') 
greet_with_logic('Kony', 'woman') 


# functions that returs values
import random
def return_a_random_number():
    return random.choice(range(0,10))

my_random_var = return_a_random_number()

print(my_random_var)

def return_a_tuple():
    value_1 = True
    value_2 = 2
    value_3 = 'returning a tuple in my function'
    return (value_1, value_2, value_3)

my_var_1, my_var_2, my_var_3 = return_a_tuple()

print(my_var_1, my_var_2, my_var_3)

# getting all the arguments
def sum_all_args(*numbers):
    return sum(numbers)

my_sum = sum_all_args(1,2,3,4,-9,-10)
print(my_sum)

# Using arguments by name 
def greet_with_arguments(first_name, last_name, age):
    return f'Hello dear {first_name} {last_name}, you are {age} years old'

print(greet_with_arguments('Mike', 'Smith', 50))
print(greet_with_arguments(age=40, first_name='Josh', last_name='Hilton'))


# lambda functions

my_lambda_function = lambda x : x*2

print(my_lambda_function(3))

nums = [1,2,3,4,5,6,7,8,9]

def is_even(nu):
    if nu%2==0:
        return True
    return False

even_nums = filter(is_even, nums)

print(list(even_nums))

# replacing with lambda functions

even_nums2 = filter(lambda x : x%2==0, nums)

print(list(even_nums2))