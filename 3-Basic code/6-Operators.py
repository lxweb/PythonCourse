"""
Basic operators
Ref: https://www.w3schools.com/python/python_operators.asp
"""

# Arithmetic operators
sum = 5 + 5 # 10
rest = 10 - 2 # 2
mult = 5 * 5 # 25
div = 9 / 3 # 3
pow = 2 ** 3 # 8
low_div = 12 // 5 # Return int rounded to floor 2
mod = 12 % 5 # 2

# Comparison operators 
# All of them return boolean
is_equal = 3 == 3 # True
is_equal = 3 == 8 # False

is_diff = 3 != 3 # False
is_diff = 3 != 8 # True

min = 3 < 6 # True 
min = 3 < 2 # False
min = 3 < 3 # False

min_equ = 2 <= 6 # True
min_equ = 2 <= 2 # True
min_equ = 2 <= 1 # False

ma = 8 > 9 # False
ma = 8 > 5 # True
ma = 8 > 8 # False

ma_equ = 9 >= 7 # True
ma_equ = 9 >= 19 # False
ma_equ = 9 >= 9 # True


# Logical operators

# AND
case_1 = True & True # Returns True
case_2 = True & False # Returns False
case_3 = False & False # Returns False
case_4 = False & True # Returns False

# OR
case_1 = True & True # Returns True
case_2 = True & False # Returns True
case_3 = False & False # Returns False
case_4 = False & True # Returns True

# NOT

case_1 = not True # Returns False
case_2 = not False # Returns True