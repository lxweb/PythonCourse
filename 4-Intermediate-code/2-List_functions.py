my_list = ["test", 1, 4.5, True]

print(len(my_list)) # Returns the amount of elements that the list has

# Adding elements to the list - using append - It modify the original list

my_list.append("added")

print(my_list)

# Adding an item in an specific index
my_list.insert(2, "using insert")

print(my_list)

# assing many elements to the list

my_list.extend(["Extended new item", 9]) # it needs a list 

print(my_list)

# POP remove elements using index

print(my_list)
print(my_list[3])
print(len(my_list))
my_list.pop(3)
print(my_list[3])
print(len(my_list))
print(my_list)


print(my_list)
print(my_list[3])
print(len(my_list))
my_list.pop(-1) # this way we can remove the last element
print(my_list[3])
print(len(my_list))
print(my_list)



# Removing an element based on it's value
print(my_list)
my_list.remove("added") # if the value does not exists in the list it throws an exeption
print(my_list)

# Removing all the items from the list
# my_list.clear()

# Sorting a list
# All the values needs to have a numerical representation
# In case of False is 0
# Incase of True is 1

my_numeric_list = [3,2,1, 0, 2.5, -1, -5, True,  False]
my_numeric_list.sort()
print(my_numeric_list)

my_numeric_list.sort(reverse=True)
print(my_numeric_list)


# Reverse - chanve the order of the list without sorting
my_numeric_list_2 = [3,2,1, 0, 2.5, -1, -5, True,  False]
my_numeric_list_2.reverse()
print(my_numeric_list_2)