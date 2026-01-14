"""
Number-Checker Program

This program takes a number as input from the user
and checks whether the number is even or odd.
"""

# Ask the user to enter a number and convert it to an integer
user_num = int(input("Enter a number: "))

# Check if the number is divisible by 2
if user_num % 2 == 0:
    # If remainder is 0, the number is even
    print("Even number")
else:
    # If remainder is not 0, the number is odd
    print("Odd number")
