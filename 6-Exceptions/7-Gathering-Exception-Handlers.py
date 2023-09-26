import logging
dividers = [1,3,6,7,9,0,3,5,2,7,5, "hello"]

# We will devide 10 for each devicder and see if there is an error
for value in dividers:
    try:
        print(10/value)
        if value == 9:
            print( int("Testing exceptions") ) # This line rise a ValueError 
    except (ZeroDivisionError, ValueError) as e:
        pass
    except Exception as e:
        logging.exception(e)
    
print("The exception was handled succesfuly")
    