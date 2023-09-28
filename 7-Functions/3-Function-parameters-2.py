
def my_funct(arg1, arg2, arg3=True): # The 3 argument is optional now
    '''
    The arguments passed on to the function exists only during the execution
    '''
    print("My arguments are:", arg1, arg2, arg3)
    

my_funct(arg2="test", arg1=123, arg3=True) # Specify the arguments regardles the order

my_funct(123, arg2="Test",  arg3=True) # It works because the positional arguments are aligned with the 
my_funct(123, arg2="Test")

# ERRORS
# my_funct("test", arg1=123, arg3=True) # This raise an error because there are 2 values for argument 1

# my_funct(arg2="test", arg1=123, arg3) # This raise en error because positional arguments 
# cannot appear after keyword arguments