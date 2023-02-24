# Chapter 5.3 Python Basics by The Real Python Team
# Write a program called exponent.py that receives two numbers from the user and displays the first number raised to the
# power of the second number.
# Here's sample run of what the program should look like, including example input from the user:
# Enter a base: 1.2
# Enter an exponent: 3
# 1.2 to the power of 3 = 1.7279999999998
# Keep the following in mind:
# 1. Before you can do anything with the user's input, you'll have to assign both calls to input () to new variables.
# 2. input() returns a string, so you'll need to convert the user's input into numbers to do arithmetic.
# 3. You can use an f-string to print the result.
# 4. You can assume that the user will enter actual number as input.

num1 = float(input("Enter a base: "))
num2 = float(input("Enter an exponent: "))
print(f"{num1} to the power of {num2} = {num1 ** num2}")