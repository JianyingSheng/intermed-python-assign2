"""
The operations program
This is a program that demonstrate how to use number operations and Booleans
To use it, run 'python operations.py'. use python 3.x (7/2=3 in python 2.x and 3.5 in python 3.x)
To show this comment, run 'python -m pydoc ./operations.py'.
"""
print("I will now count my chickens:")
# Print the number of Hens is 30 devided by 6 then plus 23
print("Hens",(25 + 30 / 6))
# The number of Roosters is equal to substract the remaining part of 75 devided by 4 from 100
print("Roosters",(100 - 25 * 3 % 4))
print ("Now I will count the eggs:")
# The number of Eggs should equal to 6 mins 5 and plus 4 modulus 2 which is zero then substract 0.25
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# Test if  5 less than -2, will return true or false
print("Is is true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
# Return 3 add 2
print("What is 3 + 2?",3 + 2)
print("what is 5 - 7?",5 - 7)
# Python do plus and substraction operations before Booleans.
print("Oh, that's why it's false.")
print("How about some more.")
# If 5 is greater than -2
print("Is it greater?",(5 > -2))
# If 5 is greater equal than -2
print("Is it greater or equal?",(5 >= -2))
# If 5 is less equal than -2
print("Is it less or equal?",(5 <= -2))
