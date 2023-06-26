""" 
Conditional 
"""

# if condition:
#    action

age = 19

if age > 18:
    print("you can pass")
else:
    print("you can not pass")
    
income  = 1000

if income > 10000:
    print("Group 1")
elif income > 5000:
    print("Group 2")
elif income > 2500:
    print("Group 3")
elif income > 1000:
    print("Group 4")    
else:
    print("No group")