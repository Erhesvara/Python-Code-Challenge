# Chapter 4.9 Python Basics by the Real Python team
# Write a program called translate.py that asks the user for some input with the following prompt:
# Enter some text:
# Use .replace() to convert the text entered by the user into leetspeak by making the following changes to lowercase
# letters:
# The letter a becomes 4
# The Letter b becomes 8
# The letter e becomes 3
# The letter l becomes 1
# The letter o becomes 0
# The letter s becomes 5
# the letter t becomes 7
# Your program should then display the resulting string as output. Below is a sample run of the program:
# Enter some text: I like to eat eggs and spam.
# I 1ik3 70 347 3gg5 4nd 5p4m

users_input = input("Enter some text: ")
users_input = users_input.lower()
users_input = users_input.replace("a", "4")
users_input = users_input.replace("b", "8")
users_input = users_input.replace("e", "3")
users_input = users_input.replace("l", "1")
users_input = users_input.replace("o", "0")
users_input = users_input.replace("s", "5")
users_input = users_input.replace("t", "7")
print(users_input)
