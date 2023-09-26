dividers = [1,3,6,7,9,0,3,5,2,7,5]

# We will devide 10 for each devicder and see if there is an error
for value in dividers:
    try:
        print(10/value)
    except:
        pass # This statement just let the program run
        # continue ## continue is an alternative if you  are in a loop that jump the next iteration
    
print("The exception was handled succesfuly")
    