# A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.
# for example, 3 is a factor of 12 because 12 divided by 3 is 4 with no remainder. However, 5 is not a factor of 12
# because 5 goes into 12 twice with the remainder of 2.
# Write a program called factors.py that asks the user to input a positive integer and then prints out the factors of
# that number. Here's a sample run of the program with output:
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12

user_input = int(input("Enter a positive integer: "))

for i in range(1, user_input+1):
    if user_input % i == 0:
        print(f"{i} is a factor of {user_input}")
