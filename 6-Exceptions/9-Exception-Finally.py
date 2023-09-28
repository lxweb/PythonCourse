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
        print(str(e))
        # Let en exceptio rise is useful when the error is coming from external resourses like 
        # Databases, API, the same OS, etc.
        #raise e # If we want the exception to follow the natural path we can use raise        
    finally:
        print("This line runs at the end it does not matter if there is an exception or not")
    
print("The exception was handled succesfuly") # This line will be not executed
    