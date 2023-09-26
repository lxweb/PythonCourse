my_var=input("Enter a new Var: ")

# If the input is a number it works
# If not it fail and it returns 0 after handling the exception
try:
    my_new_var = int(my_var)
except:
    my_new_var = 0

print(my_new_var)

