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