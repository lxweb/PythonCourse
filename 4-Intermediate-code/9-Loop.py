# Iteration needs an element that can be iterable. Those elements needs to be like lists
# lists, dict, tuples, string

my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
    
for i in my_list:
    print(f"My number is {i}")
    
for i in my_list:
    print(f"My number *100 is {i*100}") # using expresions inside loop
    
# iterate 2 list at the same time
# both lists needs to have the same size

my_team_names = ["Julia", "Mark", "Rolo"]
my_team_ages = [20, 30, 40]

for name, age in zip(my_team_names, my_team_ages):
    print(f"{name} is part of the team and is {age} years old")

# using ranges

for number in range(5, 10): # It starts on 5 and ends in 9 jumping from 1 to 1
    print(number)

for number in range(10): # It starts on 0 and ends in 9 jumping from 1 to 1
    print(number)

# the best way to iterate a list is using enumerate

for num in enumerate(my_list):
    print(num)

for index, num in enumerate(my_list):
    print(f"The index is {index} when the value is {num}.")
    
# Using else in the loop
for index, num in enumerate(my_list):
    print(f"The index is {index} when the value is {num}.")
else:
    print("The loop is finished")
    
# Loop on dict

my_dic = dict(ms1="value ms1", ms2="value ms2", ms3="value ms3")

for key in my_dic.keys():
    value = my_dic[key]
    print(value)



# short circuit with continue
my_dic2 = dict(ms1="continue ms1", ms2="continue ms2", ms3="continue ms3")
for key in my_dic2.keys():
    value = my_dic2[key]
    if value == "continue ms1":
        continue
    print(value)
    

# killing the loop with break
my_dic3 = dict(ms1="break ms1", ms2="break ms2", ms3="break ms3")
for key in my_dic3.keys():
    value = my_dic3[key]
    if value == "break ms2":
        break
    print(value)
# when using break the else closure does not run


# While loop
# it still execute while a conditios is true

num = 1
while num < 5:
    print(num)
    num  += 1