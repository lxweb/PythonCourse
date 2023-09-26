"""
Lists
"""
my_list = ["first", 2, True, 3.4]

print(my_list)

# List has base 0 index
print(my_list[3])

my_list[3] = "My new value"

print(my_list[3])

"""
Touple
"""
my_touple = ("first", 2, True, 3.4)

print(my_touple[3])
# my_touple[3] = "My new value" # Touples does not support item assignments
#print(my_touple[3])

"""
Set
"""
my_set = {"first", 2, True, 3.4}
# print(my_set[0]) # dont have acces to index
# Does not support duplicated values
# Does not have order
print(my_set)

"""
Dictionary
"""

my_dict = {
    'name': 'My new name',
    'age': 23,
    'isDev': True
}

print( my_dict['name'] )
