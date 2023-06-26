# Show as output the value of a given variable or xpression
print("test")

# type - show the tyoe of the given variable
my_var = "Test ABC  "
type(my_var)

# get all the attrubutes of the given object
print( dir(my_var) )

# Methods 
print( my_var.upper() )
print( my_var.lower() )
print( my_var.capitalize() )
print( my_var.find("st") ) # returns the position(index) of the occurency - It returns -1 if there is no occurencies - Remember it is case sensitive 
print( my_var.index("st") ) # Same than .find but if it does not find an occurency it throws an exeption

my_num = "123"
my_alph = "ABC"

print( my_num.isnumeric() ) # True

print( my_alph.isalpha() ) # True - This method does not support special characters or SPACES - only characters from a-z

# Count occurencies in a string 

my_string_to_count = "This is our string to test"

print( my_string_to_count.count("i") )

# Count the amount of characters

print(len(my_string_to_count))

#verify if a string starts or ends with a sub string
print(my_string_to_count.startswith("This"))
print(my_string_to_count.startswith("out"))
print(my_string_to_count.endswith("test"))
print(my_string_to_count.endswith("string"))


# replace a part of a given string with another sub string

print(my_string_to_count.replace("This", "Those"))
print(my_string_to_count.replace("cat", "Those")) # if the given string is not present it returns the original string

#  Turn a String into a list
print( my_string_to_count.split() ) # by default it separates by spaces ['This', 'is', 'our', 'string', 'to', 'test']
print( my_string_to_count.split("") ) # by default it separates by spaces ['This', 'is', 'our', 'string', 'to', 'test']


"""
List methods
"""



