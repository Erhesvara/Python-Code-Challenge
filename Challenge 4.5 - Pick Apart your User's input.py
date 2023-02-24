# Chapter 4.5 Python Basics by The Real Python Team
# Write a program named first_letter.py that prompts the user for input with the string "tell me your password:".
# The program should then determine the first letter of the user's input, convert that letter to uppercase, and display
# it back.
# For example, if the user input is "no" then the program should display the following output:
# The first letter you entered was: N

user_input = input("tell me your password: ")
print("Your input is: " + user_input[0].upper())
