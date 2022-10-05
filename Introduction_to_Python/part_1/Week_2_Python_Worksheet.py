#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:52:46 2020

@author: stephen
"""

# =============================================================================
# [1] Carry out basic mathematic operations using python
# =============================================================================
#%%
# [i]    addition
5 + 5

# [ii]  subtraction
7 - 5

# [iii] multiplication
5 * 5

# [iv]  division
5 / 5

# [v]   exponent
5** 5

#%%

# =============================================================================
# [2] Assign and update a variable
# =============================================================================

# [i]    Assign a value to a variable
x = 5

# [ii]   Print that variable 
print(x)

# [iii]  Update that variable to make it a new value
x = 7

# [iv]   Print the variable to see if it updated
print(x)

#%%

# =============================================================================
# [3] Working with strings
# =============================================================================

# [i]   Assign your name, in string format, to an aptly named variable
my_name = "Josemari"

# [ii]  Check to see that the value in your variable is a string
type(my_name)

# [iii] Change all of the characters in the variable to lower case
my_name.lower()

# [iv]  Use f strings to create a message which includes your name variable
print(f"My name is {my_name}")

# [v]   Create a string of ten numbers separated by commas
numbers = "1,2,3,4,5,6,7,8,9,10"

#%%
# =============================================================================
#  [4] Working with lists
# =============================================================================

# [i]   Take the string you created in [3][v] and turn it into a list
numbers_list = numbers.split(",")
numbers_list

# [ii]  Get the value of the third item in the list
numbers_list[2]

# [iii] Get the same value but use negative indexing
numbers_list[-8]

# [iv]  Get the first two items in the list using slice notation
numbers_list[0:2]

# [v]   Get every second item from the list
numbers_list[0::2]

# [vi]  Update item at index 5 to a new value
numbers_list[5] = "12"

# [vii] Update item at index 6 to a new value which is the sum of
#       the value of item index 2 and item index 3 together
numbers_list[6] = str(int(numbers_list[2]) + int(numbers_list[3]))

# [viii] Add a new value to the end of the list
numbers_list.append("11")

# [ix]  Delete the value at item index 5
numbers_list.remove(numbers_list[5])
    #other option
    #del numbers_list[5]

#%%

# =============================================================================
# [5] Working with dictionaries
# =============================================================================

# [i]   Create a dictionary with two keys, have the first key contain
#       a list of integers and the second key contain a list of strings
first_dict = {"integers":[1, 3, 5, 7, 9],
              "strings":["January", "February", "March", "April", "May"]}

# [ii]  Print out only the second keys values
first_dict["strings"]

# [iii] Get the value of the first item in the first keys values
first_dict["integers"][0]

#%%
# =============================================================================
#  [6] Conditional statements
# =============================================================================

x = 100
y = 200

# [i]   Does x equal y?
if (x == y):
    print("True")
else:
    print("False")
    
# [ii]  Does either x or y equal 200?
if (x or y == 200):
    print("True")
else:
    print("False")

# [iii] Does x and y equal 50?
if (x and y == 50):
    print("True")
else:
    print("False")

# [iv]  Does half of y equal x?
if (y / 2 == x):
    print("True")
else:
    print("False")
    
# [v]    Does half of y equal x and does double x equal y
if (y / 2 == x and x * 2 == y):
    print("True")
else:
    print("False")

#%%
# =============================================================================
#  [7]  For loops
# =============================================================================

# [i]   Create a for loop which loops over the list you created in [3][v]
#       and prints each item into a f string.
for element in numbers_list:
    print(f"The current element is {element}")


#%%


# [ii]  Create a for loop which will only print the value of the item
#       in the list if it is greater than or equal to the last item in the list
last_item = 0
for element in numbers_list:
    if int(element) >= int(last_item):
        print(f"The element {element} is bigger or equal than {last_item}")
        last_item = element


#%%
# [iii] Create a for loop which will loop over your list and append each item to
#       a new list
new_list = []
for element in numbers_list:
    new_list.append(element)


#%%
# =============================================================================
#  [8] Create a function
# =============================================================================

# [i] Create a function which asks for the users details and returns a dictionary
#     with the keys 'Name', 'Date of birth', and 'Nationality'.
#     Assign the output to a variable.
def personal_details(): 
   
    name = input("Please enter your name: \n")
    date_of_birth = input("Please enter your date of birth: \n")
    nationality = input("Please enter your nationality: \n")
    
    return {"Name":name, "Date of birth":date_of_birth, "Nationality":nationality}
    
josemari_details= personal_details()
print(josemari_details)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#%%