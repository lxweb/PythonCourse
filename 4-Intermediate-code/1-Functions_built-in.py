# Show as output the value of a given variable or xpression
print("test")

# type - show the tyoe of the given variable
my_var = "Test ABC  "
type(my_var)

# get all the attrubutes of the given object
print( dir(my_var) )


"""
List methods
"""
numbers = [-3, 0, 5, 7, 100, 8.9, -8]

maximum_number = max(numbers)

print(maximum_number)

minimum_number = min(numbers)

print(minimum_number)

print( round(999.999) )
print( round(999.999, 1) )
print( round(999.999, 2) )
print( round(999.999, 3) )


# The all function test all the items in an iterable and return True only if every item is Truly
print(all([True, "yes", 0]))
print(all([True, "yes", 1]))

# sum all the items - Needs to be numeric - Receives an iterable

print(sum([3, 3, 3]))
print(sum([3, 3.78]))
print(sum([3, -5]))