def greet_with_logic(name, gender):
    if gender == 'man':
        print(f'Hello {name}, nice to meet you boy!')
    if gender == 'woman':
        print(f'Hello {name}, nice to meet you girl!')
        
import random
def return_a_random_number():
    return random.choice(range(0,10))