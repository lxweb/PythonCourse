
def my_funct(arg1, arg2, arg3):
    '''
    The arguments passed on to the function exists only during the execution
    '''
    print("My function is running")
    print("My first argument is:", arg1)
    print("My first argument is:", arg2)
    if arg3:
        print("The 3 value is True")

my_funct("test", 123, True)