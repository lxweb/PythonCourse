dividers = [1,3,6,7,9,0,3,5,2,7,5]

# We will devide 10 for each devicder and see if there is an error
for value in dividers:
    try:
        print(10/value)
        if value == 9:
            print( int("Testing exceptions") ) # This line rise a ValueError 
    except ZeroDivisionError as zde:
        print("Zero division exception: on 10 / ", str(value))
    except ValueError as ve:
        print("Value exception: ", str(ve))
    except Exception as e:
        pass # We will see the best practice here on the next example
    
print("The exception was handled succesfuly")
    