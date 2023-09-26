dividers = [1,3,6,7,9,0,3,5,2,7,5]

# We will devide 10 for each devicder and see if there is an error
for value in dividers:
    try:
        # print(10/value)
        print( int("Testing exceptions") ) # This line rise a ValueError 
    except ZeroDivisionError as e: # Here are the list of built in exceptions https://docs.python.org/3/library/exceptions.html
        print(str(e))
    
print("The exception was handled succesfuly")
    